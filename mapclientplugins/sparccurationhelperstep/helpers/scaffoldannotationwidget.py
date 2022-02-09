
from PySide2 import QtWidgets
from mapclientplugins.sparccurationhelperstep.helpers.ui_scaffoldannotationwidget import Ui_ScaffoldAnnotationWidget


class ScaffoldAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ScaffoldAnnotationWidget, self).__init__(parent)
        self._ui = Ui_ScaffoldAnnotationWidget()
        self._ui.setupUi(self)
