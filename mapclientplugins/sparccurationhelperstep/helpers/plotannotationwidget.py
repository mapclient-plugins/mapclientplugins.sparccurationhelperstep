from PySide2 import QtWidgets, QtGui, QtCore
from sparc.curation.tools.annotations.plot import PlotAnnotation
from sparc.curation.tools.definitions import DERIVED_FROM_COLUMN, SOURCE_OF_COLUMN, FILE_LOCATION_COLUMN
from sparc.curation.tools.errors import ScaffoldAnnotationError, AnnotationDirectoryNoWriteAccess

from sparc.curation.tools.manifests import ManifestDataFrame
from sparc.curation.tools.ondisk import OnDiskFiles
from sparc.curation.tools.utilities import convert_to_bytes
from sparc.curation.tools.plot_annotations import annotate_plot

from mapclientplugins.sparccurationhelperstep.helpers.ui_plotannotationwidget import Ui_PlotAnnotationWidget
from mapclientplugins.sparccurationhelperstep.plotannotationsmodel import PlotAnnotationsModelTree


class PlotAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(PlotAnnotationWidget, self).__init__(parent)
        self._ui = Ui_PlotAnnotationWidget()
        self._ui.setupUi(self)
        self._ui.pushButtonFixError.setEnabled(False)

        self._manifest_dataframe = None
        self._location = None

        self._plot_annotations_model_tree = None

        self._make_connections()

    def _make_connections(self):
        self._ui.pushButtonFixError.clicked.connect(self._fix_error_button_clicked)
        self._ui.pushButtonFixAllErrors.clicked.connect(self._fix_all_errors_button_clicked)
        self._ui.pushButtonApply.clicked.connect(self._apply_button_clicked)
        self._ui.listViewErrors.model()
        # self._ui.treeViewPlotAnnotations.clicked.connect(self._plot_annotation_clicked)

    def update_annotations(self, location):
        max_size = convert_to_bytes('3MiB')

        self._location = location
        # OnDiskFiles().setup_dataset(location, max_size)
        plot_files = OnDiskFiles().get_plot_data()
        thumbnail_files = OnDiskFiles().get_plot_data()

        subject_list = [*plot_files, *thumbnail_files]
        subject_model = _build_list_model(subject_list)

        object_list = [*plot_files, *thumbnail_files, "--"]
        object_model = _build_list_model(object_list)

        # Make sure that _apply_button_clicked can handle any predicates listed here.
        predicate_list = [DERIVED_FROM_COLUMN, SOURCE_OF_COLUMN]
        predicate_model = _build_list_model(predicate_list)

        self._ui.comboBoxAnnotationSubject.setModel(subject_model)
        self._ui.comboBoxAnnotationObject.setModel(object_model)
        self._ui.comboBoxSAnnotationPredicate.setModel(predicate_model)

        self._reset_dataframe()
        self._plot_annotations_model_tree = PlotAnnotationsModelTree(location)
        self._ui.treeViewPlotAnnotations.setModel(self._plot_annotations_model_tree)
        selection_model = self._ui.treeViewPlotAnnotations.selectionModel()
        selection_model.selectionChanged.connect(self._annotation_selection_changed)

        self._update_ui()

    def _reset_dataframe(self):
        self._manifest_dataframe = ManifestDataFrame()

    def _update_ui(self):
        # Force refresh
        self._plot_annotations_model_tree.reset_data(self._manifest_dataframe.get_plot_data())

    def _error_selection_changed(self, i):
        self._ui.pushButtonFixError.setEnabled(len(i))

    def _annotation_selection_changed(self):
        indexes = self._ui.treeViewPlotAnnotations.selectedIndexes()
        indexes = [self._ui.treeViewPlotAnnotations.currentIndex()]
        # print("selected indexes", indexes)
        # print("current indexes", self._ui.treeViewPlotAnnotations.currentIndex())
        if len(indexes) == 1:
            selection = indexes[0]
            thumbnail_file = self._plot_annotations_model_tree.data(selection, QtCore.Qt.DisplayRole)
            thumbnail_filepath = ManifestDataFrame().get_filepath_on_disk(thumbnail_file)
            # print(thumbnail_file)
            # print(thumbnail_filepath)

            pixmap = QtGui.QPixmap(thumbnail_filepath)
            pixmap = pixmap.scaled(512, 512, QtCore.Qt.KeepAspectRatio)
            self._ui.labelThumbnailPreview.setPixmap(pixmap)
        else:
            self._ui.labelThumbnailPreview.clear()

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
        subject_text = self._ui.comboBoxAnnotationSubject.currentText()
        object_text = self._ui.comboBoxAnnotationObject.currentText()
        predicate_text = self._ui.comboBoxSAnnotationPredicate.currentText()

        if object_text != "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            result = self._manifest_dataframe.get_matching_entry(FILE_LOCATION_COLUMN, object_text)
            object_value = result[0]
        elif object_text == "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            object_value = ""
        else:
            raise NotImplementedError(f"Support for {predicate_text} is not implemented.")

        append = False
        if object_value and predicate_text == SOURCE_OF_COLUMN:
            append = True

        self._manifest_dataframe.update_column_content(subject_text, predicate_text, object_value, append)
        self._reset_dataframe()
        self._update_ui()

    def _fix_error_button_clicked(self):
        index = self._ui.listViewErrors.currentIndex()
        current_error = self._ui.listViewErrors.model().data(index, QtCore.Qt.UserRole)
        print(current_error)
        confirmationMessage = get_confirmation_message("Something")
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self._fix_error(current_error)
            self._reset_dataframe()
            self._update_ui()

    def _fix_all_errors_button_clicked(self):
        confirmationMessage = get_confirmation_message()
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
        if isinstance(i, PlotAnnotation):
            item = QtGui.QStandardItem(i.get_filename())
        else:
            item = QtGui.QStandardItem(str(i))

        item.setData(i, QtCore.Qt.UserRole)
        item.setEditable(False)
        model.appendRow(item)

    return model
