from PySide6 import QtWidgets, QtGui, QtCore
from sparc.curation.tools.definitions import DERIVED_FROM_COLUMN, SOURCE_OF_COLUMN, FILE_LOCATION_COLUMN
from sparc.curation.tools.errors import AnnotationDirectoryNoWriteAccess

import sparc.curation.tools.plot_annotations as plot_annotations

from mapclientplugins.sparccurationhelperstep.helpers.ui_plotannotationwidget import Ui_PlotAnnotationWidget
from mapclientplugins.sparccurationhelperstep.plotannotationsmodel import PlotAnnotationsModelTree


class PlotAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(PlotAnnotationWidget, self).__init__(parent)
        self._ui = Ui_PlotAnnotationWidget()
        self._ui.setupUi(self)

        self._location = None
        self._plot_list = []
        self._plot_annotations_model_tree = None

        self._make_connections()

    def _make_connections(self):
        self._ui.pushButtonAnnotatePlots.clicked.connect(self._annotate_plots_button_clicked)
        self._ui.pushButtonApply.clicked.connect(self._apply_button_clicked)
        self._ui.pushButtonAddPlot.clicked.connect(self._add_plot_clicked)
        self._ui.pushButtonAddAllPlot.clicked.connect(self._add_all_plot_clicked)
        self._ui.pushButtonRemovePlot.clicked.connect(self._remove_plot_clicked)
        self._ui.listViewPlots.model()

    def update_annotations(self, location):

        self._location = location
        plot_files = plot_annotations.get_all_plots_path()
        thumbnail_files = plot_annotations.get_plot_thumbnails()
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

        self._plot_annotations_model_tree = PlotAnnotationsModelTree(location)
        self._ui.treeViewPlotAnnotations.setModel(self._plot_annotations_model_tree)
        selection_model = self._ui.treeViewPlotAnnotations.selectionModel()
        selection_model.selectionChanged.connect(self._annotation_selection_changed)

        fileBrowserModel = QtWidgets.QFileSystemModel()
        fileBrowserModel.setRootPath(QtCore.QDir.rootPath())
        self._ui.treeViewFileBrowser.setModel(fileBrowserModel)
        self._ui.treeViewFileBrowser.setRootIndex(fileBrowserModel.index(self._location))

        self._update_ui()

    def _update_ui(self):
        # Force refresh
        self._plot_annotations_model_tree.reset_data(plot_annotations.get_annotated_plot_dictionary())
        plots_model = _build_list_model(self._plot_list)
        self._ui.listViewPlots.setModel(plots_model)

    def _annotation_selection_changed(self):
        indexes = [self._ui.treeViewPlotAnnotations.currentIndex()]
        if len(indexes) == 1:
            selection = indexes[0]
            thumbnail_file = self._plot_annotations_model_tree.data(selection, QtCore.Qt.UserRole)
            pixmap = QtGui.QPixmap(thumbnail_file)
            pixmap = pixmap.scaled(512, 512, QtCore.Qt.KeepAspectRatio)
            self._ui.labelThumbnailPreview.setPixmap(pixmap)
        else:
            self._ui.labelThumbnailPreview.clear()

    def _add_plot_clicked(self):
        # Get path for current selected file in the file tree view
        index = self._ui.treeViewFileBrowser.currentIndex()
        filePath = self._ui.treeViewFileBrowser.model().filePath(index)

        # Add the selected file to the plot list view
        if filePath not in self._plot_list:
            self._plot_list.append(filePath)
        self._update_ui()

    def _add_all_plot_clicked(self):
        self._plot_list = plot_annotations.get_all_plots_path()
        self._update_ui()

    def _remove_plot_clicked(self):
        # Remove the selected file to the plot list view
        index = self._ui.listViewPlots.currentIndex()
        item = self._ui.listViewPlots.model().itemFromIndex(index)
        if item:
            selected_plot = self._ui.listViewPlots.model().itemFromIndex(index).text()
            self._plot_list.remove(selected_plot)
            self._update_ui()

    def _errors_item_clicked(self, model_index):
        """
        Changes current step and possibly changes checked/run status.
        """
        model = model_index.model()
        item = model.itemFromIndex(model_index)
        error = item.data()
        if error != self._currentError:
            self._currentError = error

    def _apply_button_clicked(self):
        subject_text = self._ui.comboBoxAnnotationSubject.currentText()
        object_text = self._ui.comboBoxAnnotationObject.currentText()
        predicate_text = self._ui.comboBoxSAnnotationPredicate.currentText()

        if object_text != "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            result = plot_annotations.get_manifest().get_matching_entry(FILE_LOCATION_COLUMN, object_text)
            object_value = result[0] if result else None
        elif object_text == "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            object_value = ""
        else:
            raise NotImplementedError(f"Support for {predicate_text} is not implemented.")

        append = False
        if object_value and predicate_text == SOURCE_OF_COLUMN:
            append = True

        plot_annotations.get_manifest().update_column_content(subject_text, predicate_text, object_value, append)
        self._update_ui()

    def _annotate_plots_button_clicked(self):
        confirmationMessage = plot_annotations.get_confirmation_message()
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            try:
                plot_annotations.annotate_plot_from_plot_paths(self._plot_list)
            except AnnotationDirectoryNoWriteAccess:
                QtWidgets.QMessageBox.critical(self, "Error", "No write access to directory.")

            self._update_ui()


def _build_list_model(annotation_items):
    model = QtGui.QStandardItemModel()
    for i in annotation_items:
        # if isinstance(i, PlotAnnotation):
        #     item = QtGui.QStandardItem(i.get_filename())
        # else:
        item = QtGui.QStandardItem(str(i))

        item.setData(i, QtCore.Qt.UserRole)
        item.setEditable(False)
        model.appendRow(item)

    return model
