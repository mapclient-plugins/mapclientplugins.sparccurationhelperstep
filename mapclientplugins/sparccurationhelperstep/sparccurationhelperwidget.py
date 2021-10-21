
from PySide2 import QtCore, QtGui, QtWidgets

from sparc.curation.tools.annotations.scaffold import ScaffoldAnnotationError, ScaffoldAnnotation
from sparc.curation.tools.errors import AnnotationDirectoryNoWriteAccess
from sparc.curation.tools.ondisk import OnDiskFiles
from sparc.curation.tools.scaffold_annotations import ManifestDataFrame
from sparc.curation.tools.utilities import convert_to_bytes

from mapclientplugins.sparccurationhelperstep.scaffoldannotationsmodel import ScaffoldAnnotationsModel
from mapclientplugins.sparccurationhelperstep.ui_sparccurationhelperwidget import Ui_SparcCurationHelperWidget

import sparc.curation.tools.scaffold_annotations as sa


class SparcCurationHelperWidget(QtWidgets.QWidget):

    def __init__(self, location, parent=None):
        super(SparcCurationHelperWidget, self).__init__(parent)
        self._ui = Ui_SparcCurationHelperWidget()
        self._ui.setupUi(self)

        self._callback = None
        # sa = ScaffoldMetadata(location)
        # scrape_manifest_entries(location)
        # self._fileDir = r"c:\users\ywan787\neondata\curationdata\Pennsieve-dataset-76-version-3"
        self._fileDir = location

        max_size = convert_to_bytes('3MiB')

        self._manifestDF = None
        self._onDiskFiles = OnDiskFiles().setup_dataset(self._fileDir, max_size)

        self._currentError = None
        self._errors = None
        self._scaffold_annotation_selected = None
        self._scaffold_metadata = None

        self._scaffold_annotations_model = ScaffoldAnnotationsModel(location)
        self._ui.tableViewScaffoldAnnotations.setModel(self._scaffold_annotations_model)
        self._ui.tableViewScaffoldAnnotations.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self._ui.tableViewScaffoldAnnotations.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self._makeConnections()
        self._updateUI()

    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._ui.buttonFixError.clicked.connect(self._fixErrorButtonClicked)
        self._ui.buttonFixAllErrors.clicked.connect(self._fixAllErrorsButtonClicked)

        # self._ui.tableViewScaffoldAnnotations.selectionModel().selectionChanged.connect(self._scaffold_annotation_clicked)
        self._ui.tableViewScaffoldAnnotations.clicked.connect(self._scaffold_annotation_clicked)
        # self._ui.tableViewScaffoldAnnotations.clicked.connect()
        # self._ui.scaffold_annotations_listView.clicked[QtCore.QModelIndex].connect(self._scaffoldAnnotationsListItemClicked)
        # self._ui.scaffold_views_listView.clicked[QtCore.QModelIndex].connect(self._scaffoldViewsListItemClicked)
        self._ui.listViewErrors.clicked[QtCore.QModelIndex].connect(self._errorsListItemClicked)

        self._ui.annotate_scaffold_button.setVisible(False)
        self._ui.pushButton_3.setVisible(False)

    def _updateUI(self):
        # Force refresh
        self._manifestDF = ManifestDataFrame().setup_dataframe(self._fileDir)
        self._scaffold_annotations_model.resetData(self._manifestDF.get_scaffold_data())
        self._ui.tableViewScaffoldAnnotations.resizeColumnsToContents()

        self._errors = sa.get_errors()

        self._ui.buttonFixAllErrors.setEnabled(len(self._errors) > 0)
        self._ui.buttonFixError.setEnabled(len(self._errors) > 0)

        self._buildListView(self._ui.listViewErrors, self._errors)

    def _buildListView(self, listview, itemList):
        """
        Rebuilds the list of items in the Listview from the material module
        """
        selectedIndex = None
        itemModel = QtGui.QStandardItemModel(listview)
        for i in itemList:
            if isinstance(i, ScaffoldAnnotationError):
                item = QtGui.QStandardItem(i.get_error_message()[7:])
            elif isinstance(i, ScaffoldAnnotation):
                item = QtGui.QStandardItem(i.get_filename())
            else:
                item = QtGui.QStandardItem(str(i))
            item.setData(i)
            item.setEditable(False)
            itemModel.appendRow(item)
        listview.setModel(itemModel)
        if selectedIndex:
            listview.setCurrentIndex(selectedIndex)
        listview.show()

    def _scaffold_annotation_clicked(self, model_index):
        if self._scaffold_annotation_selected is not None and model_index.row() == self._scaffold_annotation_selected:
            selection_model = self._ui.tableViewScaffoldAnnotations.selectionModel()
            selection_model.clearSelection()
            self._scaffold_annotation_selected = None
            self._ui.labelThumbnailPreview.clear()
        else:
            self._scaffold_annotation_selected = model_index.row()
            thumbnail_index = self._scaffold_annotations_model.index(model_index.row(), 2, QtCore.QModelIndex())
            thumbnail = self._scaffold_annotations_model.data(thumbnail_index, QtCore.Qt.UserRole)
            pixmap = QtGui.QPixmap(thumbnail)
            pixmap = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
            self._ui.labelThumbnailPreview.setPixmap(pixmap)

    def _errorsListItemClicked(self, modelIndex):
        """
        Changes current step and possibly changes checked/run status.
        """
        model = modelIndex.model()
        item = model.itemFromIndex(modelIndex)
        error = item.data()
        if error != self._currentError:
            self._currentError = error
            # self._updateWidgets()

    def _fixError(self, error):
        success = False
        try:
            sa.fix_error(error)
            success = True
        except AnnotationDirectoryNoWriteAccess:
            QtWidgets.QMessageBox.critical(self, "Error", "No write access to directory.")

        return success

    def _fixErrorButtonClicked(self):
        confirmationMessage = sa.get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self._fixError(self._currentError)
            self._updateUI()

    def _fixAllErrorsButtonClicked(self):
        confirmationMessage = sa.get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            for e in self._errors:
                if not self._fixError(e):
                    break

            self._updateUI()
        # sa.annotate_scaffold_file()

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        # self._model.done()
        self._callback()
