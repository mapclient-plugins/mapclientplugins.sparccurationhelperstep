from PySide2 import QtCore, QtGui, QtWidgets

from mapclientplugins.sparccurationhelperstep.ui_sparccurationhelperwidget import Ui_SparcCurationHelperWidget
from sparc.curation.tools.scaffold_annotations import ScaffoldAnnotation
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
        
        print(location)
        print(sa)
        print(sa.scrape_manifest_entries(location))
        
        self.scaffold_annotations = sa.scrape_manifest_entries(location)
        self.scaffold_metadata = sa.search_for_metadata_files(self._fileDir, 10000000)
        self.errors = sa.check_scaffold_annotations(self.scaffold_annotations)

        self.errors.extend(sa.check_scaffold_metadata_annotated(self.scaffold_metadata, self.scaffold_annotations))

        self._makeConnections()


    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._buildListView(self._ui.scaffold_annotations_listView, self.scaffold_annotations)
        self._buildListView(self._ui.scaffold_metadata_listView, self.scaffold_metadata)
        self._buildListView(self._ui.errors_listView, self.errors)

    def _buildListView(self, listview, itemList):
        """
        Rebuilds the list of items in the Listview from the material module
        """
        selectedIndex = None
        itemModel = QtGui.QStandardItemModel(listview)
        for i in itemList:
            if isinstance(i, ScaffoldAnnotation):
                item = QtGui.QStandardItem(i.file())
            else:
                item = QtGui.QStandardItem(i.__str__()[7:])
            item.setData(i)
            item.setEditable(False)
            itemModel.appendRow(item)
        listview.setModel(itemModel)
        if selectedIndex:
            listview.setCurrentIndex(selectedIndex)
        listview.show()

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        # self._model.done()
        self._callback()