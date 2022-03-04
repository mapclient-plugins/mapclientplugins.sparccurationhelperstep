
from PySide2 import QtWidgets, QtGui, QtCore
from sparc.curation.tools.annotations.scaffold import ScaffoldAnnotation
from sparc.curation.tools.errors import ScaffoldAnnotationError, AnnotationDirectoryNoWriteAccess

from sparc.curation.tools.manifests import ManifestDataFrame
from sparc.curation.tools.ondisk import OnDiskFiles
from sparc.curation.tools.utilities import convert_to_bytes
from sparc.curation.tools.scaffold_annotations import get_errors, fix_error, get_confirmation_message

from mapclientplugins.sparccurationhelperstep.helpers.ui_scaffoldannotationwidget import Ui_ScaffoldAnnotationWidget
from mapclientplugins.sparccurationhelperstep.scaffoldannotationsmodel import ScaffoldAnnotationsModelTree


class ScaffoldAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ScaffoldAnnotationWidget, self).__init__(parent)
        self._ui = Ui_ScaffoldAnnotationWidget()
        self._ui.setupUi(self)

        self._manifest_dataframe = None
        self._location = None

        self._scaffold_annotations_model_tree = None
        self._model_mapper = QtWidgets.QDataWidgetMapper()
        self._scaffold_annotation_selected = None

        self._make_connections()

    def _make_connections(self):
        pass
        # self._ui.treeViewScaffoldAnnotations.clicked.connect(self._scaffold_annotation_clicked)

    def update_annotations(self, location):
        max_size = convert_to_bytes('3MiB')

        self._location = location
        OnDiskFiles().setup_dataset(location, max_size)
        self._reset_dataframe()
        self._scaffold_annotations_model_tree = ScaffoldAnnotationsModelTree(location)
        self._model_mapper.setModel(self._scaffold_annotations_model_tree)
        self._model_mapper.addMapping(self._ui.labelThumbnailPreview, 3)
        self._ui.treeViewScaffoldAnnotations.setModel(self._scaffold_annotations_model_tree)
        selection_model = self._ui.treeViewScaffoldAnnotations.selectionModel()
        selection_model.selectionChanged.connect(self._selection_changed)
        self._update_ui()

    def _reset_dataframe(self):
        self._manifest_dataframe = ManifestDataFrame().setup_dataframe(self._location)

    def _update_ui(self):
        # Force refresh
        self._scaffold_annotations_model_tree.reset_data(self._manifest_dataframe.get_scaffold_data())

        self._errors = get_errors()
        errors_model = _build_list_model(self._errors)
        self._ui.listViewErrors.setModel(errors_model)

        # annotations = ManifestDataFrame().get_scaffold_data().get_scaffold_annotations()
        # meta_items = []
        # view_items = []
        # thumb_items = []
        # for a in annotations:
        #     if a.get_additional_type() == SCAFFOLD_META_MIME:
        #         meta_items.append(a)
        #     elif a.get_additional_type() == SCAFFOLD_VIEW_MIME:
        #         view_items.append(a)
        #     elif a.get_additional_type() == SCAFFOLD_THUMBNAIL_MIME:
        #         thumb_items.append(a)

        # self._ui.pushButtonApply.setEnabled(len(meta_items) and len(view_items) and len(thumb_items))

        # meta_model = _build_list_model(meta_items)
        # view_model = _build_list_model(view_items)
        # thumb_model = _build_list_model(thumb_items)

        # self._ui.comboBoxScaffoldMeta.setModel(meta_model)
        # self._ui.comboBoxScaffoldView.setModel(view_model)
        # self._ui.comboBoxScaffoldThumbnail.setModel(thumb_model)

    def _selection_changed(self):
        indexes = self._ui.treeViewScaffoldAnnotations.selectedIndexes()
        if len(indexes) == 1:
            selection = indexes[0]
            thumbnail_file = self._scaffold_annotations_model_tree.data(selection, QtCore.Qt.DisplayRole)
            thumbnail_filepath = ManifestDataFrame().get_filepath_on_disk(thumbnail_file)
            pixmap = QtGui.QPixmap(thumbnail_filepath)
            pixmap = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
            self._ui.labelThumbnailPreview.setPixmap(pixmap)
        else:
            self._ui.labelThumbnailPreview.clear()

    def _scaffold_annotation_clicked(self, model_index):
        if self._scaffold_annotation_selected is not None and model_index.row() == self._scaffold_annotation_selected:
            selection_model = self._ui.treeViewScaffoldAnnotations.selectionModel()
            selection_model.clearSelection()
            self._scaffold_annotation_selected = None
            self._ui.labelThumbnailPreview.clear()
        else:
            self._scaffold_annotation_selected = model_index.row()
            thumbnail_index = self._ui.treeViewScaffoldAnnotations.model().index(model_index.row(), 2, QtCore.QModelIndex())
            thumbnail = self._scaffold_annotations_model.data(thumbnail_index, QtCore.Qt.UserRole)
            pixmap = QtGui.QPixmap(thumbnail)
            pixmap = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
            self._ui.labelThumbnailPreview.setPixmap(pixmap)

    def _errors_item_clicked(self, model_index):
        """
        Changes current step and possibly changes checked/run status.
        """
        model = model_index.model()
        item = model.itemFromIndex(model_index)
        error = item.data()
        if error != self._currentError:
            self._currentError = error

    def _fix_error(self, error):
        success = False
        try:
            fix_error(error)
            success = True
        except AnnotationDirectoryNoWriteAccess:
            QtWidgets.QMessageBox.critical(self, "Error", "No write access to directory.")

        return success

    def _apply_button_clicked(self):
        meta_annotation = self._ui.comboBoxScaffoldMeta.currentData(QtCore.Qt.UserRole)
        view_annotation = self._ui.comboBoxScaffoldView.currentData(QtCore.Qt.UserRole)
        thumb_annotation = self._ui.comboBoxScaffoldThumbnail.currentData(QtCore.Qt.UserRole)
        sa.update_source_of(meta_annotation.get_location(), meta_annotation.get_additional_type())
        sa.update_derived_from(view_annotation.get_location(), view_annotation.get_additional_type())
        sa.update_derived_from(thumb_annotation.get_location(), thumb_annotation.get_additional_type())
        self._update_ui()

    def _fix_error_button_clicked(self):
        confirmationMessage = get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self._fix_error(self._currentError)
            self._reset_dataframe()
            self._update_ui()

    def _fix_all_errors_button_clicked(self):
        confirmationMessage = get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            for e in self._errors:
                if not self._fix_error(e):
                    break

            self._reset_dataframe()
            self._update_ui()


def _build_list_model(annotation_items):
    model = QtGui.QStandardItemModel()
    for i in annotation_items:
        if isinstance(i, ScaffoldAnnotationError):
            item = QtGui.QStandardItem(i.get_error_message()[7:])
        elif isinstance(i, ScaffoldAnnotation):
            item = QtGui.QStandardItem(i.get_filename())
        else:
            item = QtGui.QStandardItem(str(i))

        item.setData(i, QtCore.Qt.UserRole)
        item.setEditable(False)
        model.appendRow(item)

    return model
