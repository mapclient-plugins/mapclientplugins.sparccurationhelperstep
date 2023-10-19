import os

from PySide6 import QtWidgets, QtGui, QtCore
from sparc.curation.tools.definitions import DERIVED_FROM_COLUMN, SOURCE_OF_COLUMN, FILE_LOCATION_COLUMN
from sparc.curation.tools.errors import AnnotationDirectoryNoWriteAccess

import sparc.curation.tools.plot_annotations as plot_annotations

from mapclientplugins.sparccurationhelperstep.helpers.ui_plotannotationwidget import Ui_PlotAnnotationWidget
from mapclientplugins.sparccurationhelperstep.plotannotationsmodel import PlotAnnotationsModelTree


def parse_y_columns_input(user_input):
    y_columns = []
    for part in user_input.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            y_columns.extend(range(start, end + 1))
        else:
            y_columns.append(int(part))
    return y_columns


def format_y_columns(y_columns):
    if not y_columns:
        return ""

    indices = sorted(y_columns)

    ranges = []
    start = indices[0]
    end = indices[0]

    for index in indices[1:]:
        if index == end + 1:
            end = index
        else:
            ranges.append((start, end))
            start = index
            end = index

    ranges.append((start, end))

    formatted = ",".join(f"{start}-{end}" if start != end else str(start) for start, end in ranges)
    return formatted


class PlotAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(PlotAnnotationWidget, self).__init__(parent)
        self._ui = Ui_PlotAnnotationWidget()
        self._ui.setupUi(self)

        self._location = None
        self._plot_list = []
        self._plot_plot_list = []
        self._current_plot = None
        self._plot_annotations_model_tree = None

        self._make_connections()

    def _make_connections(self):
        self._ui.pushButtonAnnotateCurrentPlot.clicked.connect(self._annotate_current_plot_button_clicked)
        self._ui.pushButtonAnnotateAllPlots.clicked.connect(self._annotate_plots_button_clicked)
        self._ui.pushButtonApply.clicked.connect(self._apply_button_clicked)
        self._ui.pushButtonAddPlot.clicked.connect(self._add_plot_clicked)
        self._ui.pushButtonAddAllPlot.clicked.connect(self._add_all_plot_clicked)
        self._ui.pushButtonRemovePlot.clicked.connect(self._remove_plot_clicked)

        plots_model = _build_list_model(self._plot_list)
        self._ui.listViewPlots.setModel(plots_model)
        self._ui.listViewPlots.selectionModel().selectionChanged.connect(self._plot_listView_clicked)

        self._ui.comboBoxPlotType.currentTextChanged.connect(self._plot_type_changed)
        self._ui.lineEditXColumn.textEdited.connect(self._plot_x_column_edit)
        self._ui.lineEditYColumns.editingFinished.connect(self._plot_y_columns_edit)
        self._ui.checkBoxHasHeader.stateChanged.connect(self._plot_has_header_checked)
        self._ui.comboBoxDelimiter.currentTextChanged.connect(self._delimiter_changed)

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
        self._plot_annotations_model_tree.reset_data(plot_annotations.get_annotated_plot_dictionary())

        fileBrowserModel = QtWidgets.QFileSystemModel()
        fileBrowserModel.setRootPath(QtCore.QDir.rootPath())
        self._ui.treeViewFileBrowser.setModel(fileBrowserModel)
        self._ui.treeViewFileBrowser.setRootIndex(fileBrowserModel.index(self._location))

    def _update_plot_ui(self):
        index = self._ui.listViewPlots.currentIndex()
        self._current_plot = self._plot_plot_list[index.row()]
        if self._current_plot:
            self._ui.PlotEditorsContainer.setEnabled(True)
            self._ui.comboBoxPlotType.setCurrentText(self._current_plot.plot_type)
            self._ui.lineEditXColumn.setText(str(self._current_plot.x_axis_column))
            self._ui.lineEditYColumns.setText(format_y_columns(self._current_plot.y_axes_columns))
            self._ui.checkBoxHasHeader.setChecked(self._current_plot.has_header())
            self._ui.comboBoxDelimiter.setCurrentText(self._current_plot.delimiter)
        else:
            self._ui.PlotEditorsContainer.setEnabled(False)

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
        filePath = os.path.normpath(self._ui.treeViewFileBrowser.model().filePath(index))

        if filePath in self._plot_list:
            currentIndex = self._ui.listViewPlots.model().index(self._plot_list.index(filePath), 0)
            self._ui.listViewPlots.setFocus()
            self._ui.listViewPlots.setCurrentIndex(currentIndex)
        else:
            # Add the selected file to the plot list view
            plot = plot_annotations.get_plot_from_path(filePath)
            if not plot:
                QtWidgets.QMessageBox.critical(self, "Error", f"{filePath} is not a valid plot file.")
            else:
                self._plot_list.append(filePath)
                self._plot_plot_list.append(plot)
                item = QtGui.QStandardItem(str(filePath))
                item.setEditable(False)
                self._ui.listViewPlots.model().appendRow(item)
        self._update_plot_ui()

    def _add_all_plot_clicked(self):
        self._plot_list, self._plot_plot_list = plot_annotations.get_all_plots()
        plots_model = _build_list_model(self._plot_list)
        self._ui.listViewPlots.setModel(plots_model)
        self._ui.listViewPlots.selectionModel().selectionChanged.connect(self._plot_listView_clicked)

    def _remove_plot_clicked(self):
        # Remove the selected file to the plot list view
        index = self._ui.listViewPlots.currentIndex()
        item = self._ui.listViewPlots.model().itemFromIndex(index)
        if item:
            selected_plot = self._ui.listViewPlots.model().itemFromIndex(index).text()
            self._plot_list.remove(selected_plot)
            self._plot_plot_list.pop(index.row())
            self._ui.listViewPlots.model().removeRows(index.row(), 1)
            self._update_plot_ui()

    def _plot_type_changed(self, plot_type):
        index = self._ui.listViewPlots.currentIndex()
        self._plot_plot_list[index.row()].plot_type = plot_type

    def _plot_x_column_edit(self):
        index = self._ui.listViewPlots.currentIndex()
        self._plot_plot_list[index.row()].x_axis_column = int(self._ui.lineEditXColumn.text())

    def _plot_y_columns_edit(self):
        index = self._ui.listViewPlots.currentIndex()
        self._plot_plot_list[index.row()].set_y_columns(parse_y_columns_input(self._ui.lineEditYColumns.text()))

    def _plot_has_header_checked(self, checked):
        index = self._ui.listViewPlots.currentIndex()
        self._plot_plot_list[index.row()].set_has_header(checked)

    def _delimiter_changed(self, delimiter):
        index = self._ui.listViewPlots.currentIndex()
        self._plot_plot_list[index.row()].delimiter = delimiter

    def _plot_listView_clicked(self, selected, deselected):
        self._update_plot_ui()

    def _apply_button_clicked(self):
        subject_text = self._ui.comboBoxAnnotationSubject.currentText()
        object_text = self._ui.comboBoxAnnotationObject.currentText()
        predicate_text = self._ui.comboBoxSAnnotationPredicate.currentText()

        if object_text != "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            result = plot_annotations.get_filename_by_location(object_text)
            object_value = result[0] if result else None
        elif object_text == "--" and (predicate_text == DERIVED_FROM_COLUMN or predicate_text == SOURCE_OF_COLUMN):
            object_value = ""
        else:
            raise NotImplementedError(f"Support for {predicate_text} is not implemented.")

        append = False
        if object_value and predicate_text == SOURCE_OF_COLUMN:
            append = True

        plot_annotations.update_column_content(subject_text, predicate_text, object_value, append)
        self._plot_annotations_model_tree.reset_data(plot_annotations.get_annotated_plot_dictionary())

    def _prepare_progress_dialog(self, label_text, button_text, total):
        progress = QtWidgets.QProgressDialog(label_text, button_text, 0, total, self)
        progress.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        return progress

    def _annotate_current_plot_button_clicked(self):
        try:
            plot_annotations.annotate_one_plot(self._current_plot)
        except AnnotationDirectoryNoWriteAccess:
            QtWidgets.QMessageBox.critical(self, "Error", "No write access to directory.")

        self._plot_annotations_model_tree.reset_data(plot_annotations.get_annotated_plot_dictionary())

    def _annotate_plots_button_clicked(self):
        self._progress_dialog = self._prepare_progress_dialog("Annotate plot files", "Cancel", len(self._plot_list))
        count = 0
        try:
            for plot in self._plot_plot_list:
                plot_annotations.annotate_one_plot(plot)
                count += 1
                self._progress_dialog.setValue(count)
                if self._progress_dialog.wasCanceled():
                    break
        except AnnotationDirectoryNoWriteAccess:
            QtWidgets.QMessageBox.critical(self, "Error", "No write access to directory.")

        self._plot_annotations_model_tree.reset_data(plot_annotations.get_annotated_plot_dictionary())


def _build_list_model(annotation_items):
    model = QtGui.QStandardItemModel()
    for i in annotation_items:
        item = QtGui.QStandardItem(str(i))
        item.setEditable(False)
        model.appendRow(item)
    return model
