
from PySide6 import QtWidgets, QtGui, QtCore
from sparc.curation.tools.definitions import DERIVED_FROM_COLUMN, SOURCE_OF_COLUMN
from sparc.curation.tools.errors import ScaffoldAnnotationError, AnnotationDirectoryNoWriteAccess

from mapclientplugins.sparccurationhelperstep.helpers.ui_scaffoldannotationwidget import Ui_ScaffoldAnnotationWidget
from mapclientplugins.sparccurationhelperstep.scaffoldannotationsmodel import ScaffoldAnnotationsModelTree
import sparc.curation.tools.scaffold_annotations as scaffold_annotations


class ScaffoldAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ScaffoldAnnotationWidget, self).__init__(parent)
        self._ui = Ui_ScaffoldAnnotationWidget()
        self._ui.setupUi(self)
        self._ui.pushButtonFixError.setEnabled(False)

        self._location = None
        self._current_error = None

        self._scaffold_annotations_model_tree = None

        self._make_connections()

    def _make_connections(self):
        self._ui.pushButtonFixError.clicked.connect(self._fix_error_button_clicked)
        self._ui.pushButtonFixAllErrors.clicked.connect(self._fix_all_errors_button_clicked)
        self._ui.pushButtonApply.clicked.connect(self._apply_button_clicked)
        self._ui.comboBoxSAnnotationPredicate.currentTextChanged.connect(self._annotation_predicate_changed)
        self._ui.listViewErrors.model()

    def update_annotations(self, location):
        self._location = location

        metadata_files = scaffold_annotations.get_on_disk_metadata_files()
        view_files = scaffold_annotations.get_on_disk_view_files()
        thumbnail_files = scaffold_annotations.get_on_disk_thumbnail_files()

        subject_list = [*metadata_files, *view_files, *thumbnail_files]
        subject_model = _build_list_model(subject_list)

        object_list = [*view_files, *thumbnail_files, "--"]
        object_model = _build_list_model(object_list)

        # Make sure that _apply_button_clicked can handle any predicates listed here.
        predicate_list = [DERIVED_FROM_COLUMN, SOURCE_OF_COLUMN]
        predicate_model = _build_list_model(predicate_list)

        self._ui.comboBoxAnnotationSubject.setModel(subject_model)
        self._ui.comboBoxAnnotationObject.setModel(object_model)
        self._ui.comboBoxSAnnotationPredicate.setModel(predicate_model)

        self._scaffold_annotations_model_tree = ScaffoldAnnotationsModelTree(location)
        self._ui.treeViewScaffoldAnnotations.setModel(self._scaffold_annotations_model_tree)
        selection_model = self._ui.treeViewScaffoldAnnotations.selectionModel()
        selection_model.selectionChanged.connect(self._annotation_selection_changed)

        self._update_ui()

    def _update_ui(self):
        # Force refresh
        self._scaffold_annotations_model_tree.reset_data(scaffold_annotations.get_annotated_scaffold_dictionary())

        self._errors = scaffold_annotations.get_errors()
        errors_model = _build_list_model(self._errors)
        self._ui.pushButtonFixAllErrors.setEnabled(errors_model.rowCount())
        self._ui.listViewErrors.setModel(errors_model)
        errors_selection_model = self._ui.listViewErrors.selectionModel()
        errors_selection_model.selectionChanged.connect(self._error_selection_changed)

    def _error_selection_changed(self, i):
        self._ui.pushButtonFixError.setEnabled(len(i))

    def _annotation_selection_changed(self):
        indexes = self._ui.treeViewScaffoldAnnotations.selectedIndexes()
        if len(indexes) == 1:
            selection = indexes[0]
            thumbnail_file = self._scaffold_annotations_model_tree.data(selection, QtCore.Qt.ItemDataRole.UserRole)
            pixmap = QtGui.QPixmap(thumbnail_file)
            if pixmap:
                pixmap = pixmap.scaled(256, 256, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                self._ui.labelThumbnailPreview.setPixmap(pixmap)
            else:
                self._ui.labelThumbnailPreview.clear()
        else:
            self._ui.labelThumbnailPreview.clear()

    def _errors_item_clicked(self, model_index):
        """
        Changes current step and possibly changes checked/run status.
        """
        model = model_index.model()
        item = model.itemFromIndex(model_index)
        error = item.data()
        if error != self._current_error:
            self._current_error = error

    def _fix_error(self, error):
        success = False
        try:
            scaffold_annotations.fix_error(error)
            success = True
        except AnnotationDirectoryNoWriteAccess:
            QtWidgets.QMessageBox.critical(self, "Error", "No write access to directory.")

        return success

    def _annotation_predicate_changed(self):
        self._ui.checkBoxAnnotationMode.setEnabled(self._ui.comboBoxSAnnotationPredicate.currentText() == SOURCE_OF_COLUMN)

    def _apply_button_clicked(self):
        subject_text = self._ui.comboBoxAnnotationSubject.currentText()
        object_text = self._ui.comboBoxAnnotationObject.currentText()
        predicate_text = self._ui.comboBoxSAnnotationPredicate.currentText()

        if object_text != "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            result = scaffold_annotations.get_filename_by_location(object_text)
            object_value = result[0] if result else ""
        elif object_text == "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            object_value = ""
        else:
            raise NotImplementedError(f"Support for {predicate_text} is not implemented.")

        append = False
        if object_value and predicate_text == SOURCE_OF_COLUMN:
            append = self._ui.checkBoxAnnotationMode.isChecked()

        scaffold_annotations.update_column_content(subject_text, predicate_text, object_value, append)
        self._update_ui()

    def _fix_error_button_clicked(self):
        index = self._ui.listViewErrors.currentIndex()
        current_error = self._ui.listViewErrors.model().data(index, QtCore.Qt.ItemDataRole.UserRole)
        confirmationMessage = scaffold_annotations.get_confirmation_message(current_error)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self._fix_error(current_error)
            self._update_ui()

    def _fix_all_errors_button_clicked(self):
        confirmationMessage = scaffold_annotations.get_confirmation_message()
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            for e in self._errors:
                if not self._fix_error(e):
                    break

            self._update_ui()


def _build_list_model(annotation_items):
    model = QtGui.QStandardItemModel()
    for i in annotation_items:
        if isinstance(i, ScaffoldAnnotationError):
            item = QtGui.QStandardItem(i.get_error_message()[7:])
        # elif isinstance(i, ScaffoldAnnotation):
        #     item = QtGui.QStandardItem(i.get_filename())
        else:
            item = QtGui.QStandardItem(str(i))

        item.setData(i, QtCore.Qt.ItemDataRole.UserRole)
        item.setEditable(False)
        model.appendRow(item)

    return model
