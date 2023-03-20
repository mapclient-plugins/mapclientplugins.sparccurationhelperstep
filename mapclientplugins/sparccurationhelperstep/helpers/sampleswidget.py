
import os

from PySide2 import QtCore, QtGui, QtWidgets

from mapclientplugins.sparccurationhelperstep.helpers.common import relative_to_dataset_dir
from mapclientplugins.sparccurationhelperstep.helpers.ui_sampleswidget import Ui_SamplesWidget


class SamplesWidget(QtWidgets.QWidget):

    view_changed = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(SamplesWidget, self).__init__(parent)
        self._ui = Ui_SamplesWidget()
        self._ui.setupUi(self)

        self._parent = parent

        self._make_connections()

    def _make_connections(self):
        self._ui.comboBoxView.currentTextChanged.connect(self.view_changed)
        self._ui.pushButtonPathFile.clicked.connect(self._open_path_to_file)

    def populate_views(self, views):
        m = self._ui.comboBoxView.model()
        for view in views:
            m.appendRow(QtGui.QStandardItem(view))

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

    def from_dict(self, data):
        self._ui.lineEditAnnotation.setText(data["annotation"])
        self._ui.plainTextEditDescription.setPlainText(data["description"])
        self._ui.lineEditDOI.setText(data["doi"])
        self._ui.lineEditHeading.setText(data["heading"])
        self._ui.lineEditPath.setText(data["path"])
        self._ui.comboBoxView.blockSignals(True)
        self._ui.comboBoxView.setCurrentText(data["view"])
        self._ui.comboBoxView.blockSignals(False)

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

    def _open_path_to_file(self):
        result = QtWidgets.QFileDialog.getOpenFileName(self, "Locate the target file", self._parent.previous_location())
        file_name = result[0]
        if file_name:
            self._parent.set_previous_location(os.path.dirname(file_name))
            self._ui.lineEditPath.setText(self._parent.to_serialisable_path(file_name))
