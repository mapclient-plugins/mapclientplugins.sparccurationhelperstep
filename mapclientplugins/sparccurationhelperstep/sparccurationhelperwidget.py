
from PySide2 import QtWidgets

from mapclientplugins.sparccurationhelperstep.ui_sparccurationhelperwidget import Ui_SparcCurationHelperWidget


class SparcCurationHelperWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(SparcCurationHelperWidget, self).__init__(parent)
        self._ui = Ui_SparcCurationHelperWidget()
        self._ui.setupUi(self)
        self._ui.tabPlotAnnotation.setVisible(False)

        self._callback = None

        self._make_connections()

    def _make_connections(self):
        self._ui.pushButtonDone.clicked.connect(self._done_button_clicked)

    def set_dataset_location(self, location):
        self._ui.tabContextAnnotation.update_info(location)
        self._ui.tabScaffoldAnnotation.update_annotations(location)

    def register_done_execution(self, callback):
        self._callback = callback

    def _done_button_clicked(self):
        self._callback()
