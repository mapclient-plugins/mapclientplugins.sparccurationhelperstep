from PySide2 import QtCore, QtGui, QtWidgets

from mapclientplugins.sparccurationhelperstep.ui_sparccurationhelperwidget import Ui_SparcCurationHelperWidget
# from sparc.curation.tools.scaffold_annotations import ScaffoldAnnotation
import sparc.curation.tools.scaffold_annotations as sa

class SparcCurationHelperWidget(QtWidgets.QWidget):
    
    def __init__(self, model, location, parent=None):
        super(SparcCurationHelperWidget, self).__init__(parent)
        self._ui = Ui_SparcCurationHelperWidget()
        self._ui.setupUi(self)

        self._callback = None
        # sa = ScaffoldAnnotation(location)
        # scrape_manifest_entries(location)
        # self._fileDir = r"c:\users\ywan787\neondata\curationdata\Pennsieve-dataset-76-version-3"
        self._fileDir = location

        self._currentError = None

        self._makeConnections()
        self._updateUI()


    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._ui.fixError_btn.clicked.connect(self._fixErrorButtonClicked)
        self._ui.fixAllErrors_btn.clicked.connect(self._fixAllErrorsButtonClicked)
        self._ui.errors_listView.clicked[QtCore.QModelIndex].connect(self._errorsListItemClicked)


    def _updateUI(self):
        self.scaffold_annotations = sa.scrape_manifest_entries(self._fileDir)
        self.scaffold_metadata = sa.search_for_metadata_files(self._fileDir, 10000000)
        self.errors = sa.check_scaffold_annotations(self.scaffold_annotations)
        self.errors.extend(sa.check_scaffold_metadata_annotated(self.scaffold_metadata, self.scaffold_annotations))

        self._buildListView(self._ui.scaffold_annotations_listView, self.scaffold_annotations)
        self._buildListView(self._ui.scaffold_metadata_listView, self.scaffold_metadata)
        self._buildListView(self._ui.errors_listView, self.errors)
        self._ui.scaffold_annotation_label.setText("There are %d files are annotated as scaffold in manifest files."%len(self.scaffold_annotations))
        self._ui.scaffold_metadata_label.setText("There are %d files are detected as scaffold file by programming."%len(self.scaffold_metadata))

    def _buildListView(self, listview, itemList):
        """
        Rebuilds the list of items in the Listview from the material module
        """
        selectedIndex = None
        itemModel = QtGui.QStandardItemModel(listview)
        for i in itemList:
            if isinstance(i, sa.ScaffoldAnnotation):
                item = QtGui.QStandardItem(i.file())
            else:
                item = QtGui.QStandardItem(i.get_error_message()[7:])
            print(i)
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
        print(error)
        if error != self._currentError:
            self._currentError = error
            print("Set self._currentError", self._currentError)
        print(self._currentError)
        #    self._updateFitterStepWidgets()


    def _fixErrorButtonClicked(self):
        confirmationMessage = sa.get_confirmation_message(self._currentError)
        result = QtWidgets.QMessageBox.question(self, "Confirmation", confirmationMessage, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            print("YES!!!")
            sa.fix_error(self._currentError, self._fileDir)
            self._updateUI()
        # sa.annotate_scaffold_file()


    def _fixAllErrorsButtonClicked(self):
        pass



    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        # self._model.done()
        self._callback()