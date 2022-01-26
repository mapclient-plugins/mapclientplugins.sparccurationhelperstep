
from PySide2 import QtCore, QtGui, QtWidgets
from mapclientplugins.sparccurationhelperstep.helpers.ui_sampleswidget import Ui_SamplesWidget


class SamplesWidget(QtWidgets.QWidget):

    view_changed = QtCore.Signal(str)

    def __init__(self, views, parent=None):
        super(SamplesWidget, self).__init__(parent)
        self._ui = Ui_SamplesWidget()
        self._ui.setupUi(self)
        m = self._ui.comboBoxView.model()
        for view in views:
            m.appendRow(QtGui.QStandardItem(view))

        self._make_connections()

    def _make_connections(self):
        self._ui.comboBoxView.currentTextChanged.connect(self.view_changed)

    def set_view(self, view):
        self._ui.comboBoxView.blockSignals(True)
        self._ui.comboBoxView.setCurrentText(view)
        self._ui.comboBoxView.blockSignals(False)

    def as_dict(self, header):
        return {
            "annotation": self._ui.lineEditAnnotation.text(),
            "description": self._ui.plainTextEditDescription.toPlainText(),
            "doi": self._ui.lineEditDOI.text(),
            "heading": self._ui.lineEditHeading.text(),
            "id": header,
            "path": self._ui.lineEditPath.text(),
            "view": self._ui.comboBoxView.currentText(),
        }

    def add_view(self, sample):
        m = self._ui.comboBoxView.model()
        item = QtGui.QStandardItem(sample)
        m.appendRow(item)

    def remove_view(self, sample):
        m = self._ui.comboBoxView.model()
        remove_row = None
        for r in range(m.rowCount()):
            item = m.item(r)
            if item.text() == sample:
                remove_row = r

        if remove_row is not None:
            if self._ui.comboBoxView.currentIndex() == remove_row:
                self._ui.comboBoxView.setCurrentIndex(0)
            m.takeRow(remove_row)
