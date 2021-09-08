from PySide2 import QtCore, QtGui, QtWidgets

import os
from mapclientplugins.sparccurationhelperstep.ui_sparccurationhelperwidget import Ui_SparcCurationHelperWidget
from sparc.curation.tools.scaffold_annotations import ManifestDataFrame
import sparc.curation.tools.scaffold_annotations as sa

class SparcCurationHelperWidget(QtWidgets.QWidget):
    
    def __init__(self, model, location, parent=None):
        super(SparcCurationHelperWidget, self).__init__(parent)
        self._ui = Ui_SparcCurationHelperWidget()
        self._ui.setupUi(self)

        self._callback = None
        # sa = ScaffoldMetadata(location)
        # scrape_manifest_entries(location)
        # self._fileDir = r"c:\users\ywan787\neondata\curationdata\Pennsieve-dataset-76-version-3"
        self._fileDir = location

        self._manifestDF = ManifestDataFrame().setup_dataframe(self._fileDir, 10000000)

        self._currentError = None
        self._errors = None
        self._scaffold_annotations = None
        self._scaffold_metadata = None

        self._makeConnections()
        self._updateUI()


    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._ui.fixError_btn.clicked.connect(self._fixErrorButtonClicked)
        self._ui.fixAllErrors_btn.clicked.connect(self._fixAllErrorsButtonClicked)

        self._ui.scaffold_annotations_listView.clicked[QtCore.QModelIndex].connect(self._scaffoldAnnotationsListItemClicked)
        self._ui.scaffold_views_listView.clicked[QtCore.QModelIndex].connect(self._scaffoldViewsListItemClicked)
        self._ui.errors_listView.clicked[QtCore.QModelIndex].connect(self._errorsListItemClicked)

        self._ui.annotate_scaffold_button.setVisible(False)
        self._ui.pushButton_3.setVisible(False)

    def _updateUI(self):
        # self.errors = sa.check_scaffold_annotations()
    
        # Force refresh
        self._manifestDF = ManifestDataFrame().setup_dataframe(self._fileDir, 10000000)

        self._errors = sa.get_errors()

        self._scaffold_annotations = self._manifestDF.get_annotated_scaffold()
        self._scaffold_metadata = self._manifestDF.get_real_scaffold()
        self._buildListView(self._ui.scaffold_annotations_listView, self._scaffold_annotations)
        self._buildListView(self._ui.scaffold_metadata_listView, self._scaffold_metadata)
        self._buildListView(self._ui.errors_listView, self._errors)
        self._ui.scaffold_annotation_label.setText("There are %d files are annotated as scaffold in manifest files."%len(self._scaffold_annotations))
        self._ui.scaffold_metadata_label.setText("There are %d files are detected as scaffold file by programming."%len(self._scaffold_metadata))

    def _buildListView(self, listview, itemList):
        """
        Rebuilds the list of items in the Listview from the material module
        """
        selectedIndex = None
        itemModel = QtGui.QStandardItemModel(listview)
        for i in itemList:
            if isinstance(i, sa.ScaffoldAnnotationError):
                item = QtGui.QStandardItem(i.get_error_message()[7:])
            elif isinstance(i, sa.ScaffoldAnnotation):
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

    def _scaffoldAnnotationsListItemClicked(self, modelIndex):
        """
        Show view list of selected scaffold.
        """
        model = modelIndex.model()
        item = model.itemFromIndex(modelIndex)
        scaffoldAnnotation = item.data()
        # print(scaffoldAnnotation.thumbnail())
        viewList = []
        for i in self._manifestDF.get_annotated_view():
            for j in scaffoldAnnotation.get_children():
                if os.path.samefile(i.get_location(), j):
                    viewList.append(i)
        self._buildListView(self._ui.scaffold_views_listView, viewList)

    def _scaffoldViewsListItemClicked(self, modelIndex):
        """
        Show thumbnail of selected view
        """
        model = modelIndex.model()
        item = model.itemFromIndex(modelIndex)
        scaffoldView= item.data()
        previewPixmap = QtGui.QPixmap(scaffoldView.get_thumbnail())
        previewPixmap = previewPixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio) 
        self._ui.thumbnail_preview_label.setScaledContents(True) 
        self._ui.thumbnail_preview_label.setPixmap(previewPixmap)


    def _fixErrorButtonClicked(self):
        confirmationMessage = sa.get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            print("YES!!!")
            sa.fix_error(self._currentError)
            self._updateUI()
        # sa.annotate_scaffold_file()

    def _fixAllErrorsButtonClicked(self):
        confirmationMessage = sa.get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            print("YES!!!")
            for i in self._errors:
                sa.fix_error(i)
            self._updateUI()
        # sa.annotate_scaffold_file()


    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        # self._model.done()
        self._callback()