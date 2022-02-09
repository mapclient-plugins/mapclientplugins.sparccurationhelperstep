
from PySide2 import QtCore, QtGui, QtWidgets

from sparc.curation.tools.annotations.scaffold import ScaffoldAnnotationError, ScaffoldAnnotation
from sparc.curation.tools.definitions import SCAFFOLD_FILE_MIME, SCAFFOLD_THUMBNAIL_MIME, SCAFFOLD_VIEW_MIME
from sparc.curation.tools.errors import AnnotationDirectoryNoWriteAccess
from sparc.curation.tools.ondisk import OnDiskFiles
from sparc.curation.tools.scaffold_annotations import ManifestDataFrame
from sparc.curation.tools.utilities import convert_to_bytes

from mapclientplugins.sparccurationhelperstep.scaffoldannotationsmodel import ScaffoldAnnotationsModel, ScaffoldAnnotationsModelTree
from mapclientplugins.sparccurationhelperstep.ui_sparccurationhelperwidget import Ui_SparcCurationHelperWidget

import sparc.curation.tools.scaffold_annotations as sa


class SparcCurationHelperWidget(QtWidgets.QWidget):

    def __init__(self, location, parent=None):
        super(SparcCurationHelperWidget, self).__init__(parent)
        self._ui = Ui_SparcCurationHelperWidget()
        self._ui.setupUi(self)
        self._ui.tabPlotAnnotation.setVisible(False)

        self._callback = None
        self._fileDir = location

        max_size = convert_to_bytes('3MiB')

        self._manifestDF = None
        self._onDiskFiles = OnDiskFiles().setup_dataset(self._fileDir, max_size)

        self._currentError = None
        self._errors = None
        self._scaffold_annotation_selected = None
        self._scaffold_metadata = None

        self._scaffold_annotations_model_tree = ScaffoldAnnotationsModelTree(location)
        self._scaffold_annotations_model = ScaffoldAnnotationsModel(location)
        # self._ui.tableViewScaffoldAnnotations.setModel(self._scaffold_annotations_model)
        # self._ui.treeViewScaffoldAnnotations.setModel(self._scaffold_annotations_model_tree)
        # self._ui.tableViewScaffoldAnnotations.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # self._ui.tableViewScaffoldAnnotations.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self._make_connections()
        self._update_ui()

    def _make_connections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        # self._ui.buttonFixError.clicked.connect(self._fixErrorButtonClicked)
        # self._ui.buttonFixAllErrors.clicked.connect(self._fixAllErrorsButtonClicked)

        # self._ui.tableViewScaffoldAnnotations.clicked.connect(self._scaffold_annotation_clicked)
        # self._ui.listViewErrors.clicked[QtCore.QModelIndex].connect(self._errorsListItemClicked)

        # self._ui.annotate_scaffold_button.setVisible(False)
        # self._ui.pushButton_3.setVisible(False)

        # self._ui.pushButtonApply.clicked.connect(self._apply_button_clicked)

    def _update_ui(self):
        # Force refresh
        self._manifestDF = ManifestDataFrame().setup_dataframe(self._fileDir)
        self._scaffold_annotations_model.resetData(self._manifestDF.get_scaffold_data())
        self._scaffold_annotations_model_tree.reset_data(self._manifestDF.get_scaffold_data())
        # self._ui.tableViewScaffoldAnnotations.resizeColumnsToContents()

        self._errors = sa.get_errors()

        # self._ui.buttonFixAllErrors.setEnabled(len(self._errors) > 0)
        # self._ui.buttonFixError.setEnabled(len(self._errors) > 0)

        errors_model = _build_list_model(self._errors)
        # self._ui.listViewErrors.setModel(errors_model)

        annotations = ManifestDataFrame().get_scaffold_data().get_scaffold_annotations()
        meta_items = []
        view_items = []
        thumb_items = []
        for a in annotations:
            if a.get_additional_type() == SCAFFOLD_FILE_MIME:
                meta_items.append(a)
            elif a.get_additional_type() == SCAFFOLD_VIEW_MIME:
                view_items.append(a)
            elif a.get_additional_type() == SCAFFOLD_THUMBNAIL_MIME:
                thumb_items.append(a)

        # self._ui.pushButtonApply.setEnabled(len(meta_items) and len(view_items) and len(thumb_items))

        meta_model = _build_list_model(meta_items)
        view_model = _build_list_model(view_items)
        thumb_model = _build_list_model(thumb_items)

        # self._ui.comboBoxScaffoldMeta.setModel(meta_model)
        # self._ui.comboBoxScaffoldView.setModel(view_model)
        # self._ui.comboBoxScaffoldThumbnail.setModel(thumb_model)

    def _scaffold_annotation_clicked(self, model_index):
        if self._scaffold_annotation_selected is not None and model_index.row() == self._scaffold_annotation_selected:
            # selection_model = self._ui.tableViewScaffoldAnnotations.selectionModel()
            # selection_model.clearSelection()
            self._scaffold_annotation_selected = None
            # self._ui.labelThumbnailPreview.clear()
        else:
            self._scaffold_annotation_selected = model_index.row()
            thumbnail_index = self._scaffold_annotations_model.index(model_index.row(), 2, QtCore.QModelIndex())
            thumbnail = self._scaffold_annotations_model.data(thumbnail_index, QtCore.Qt.UserRole)
            pixmap = QtGui.QPixmap(thumbnail)
            pixmap = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
            # self._ui.labelThumbnailPreview.setPixmap(pixmap)

    def _errorsListItemClicked(self, modelIndex):
        """
        Changes current step and possibly changes checked/run status.
        """
        model = modelIndex.model()
        item = model.itemFromIndex(modelIndex)
        error = item.data()
        if error != self._currentError:
            self._currentError = error

    def _fixError(self, error):
        success = False
        try:
            sa.fix_error(error)
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

    def _fixErrorButtonClicked(self):
        confirmationMessage = sa.get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self._fixError(self._currentError)
            self._update_ui()

    def _fixAllErrorsButtonClicked(self):
        confirmationMessage = sa.get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            for e in self._errors:
                if not self._fixError(e):
                    break

            self._update_ui()

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        self._callback()


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
