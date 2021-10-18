from PySide2 import QtCore


class ScaffoldAnnotationsModel(QtCore.QAbstractTableModel):
    def __init__(self, common_path, parent=None):
        super(ScaffoldAnnotationsModel, self).__init__(parent)
        self._headers = ['Scaffold Metadata', 'Associated View', 'Associated Thumbnail']

        self._data = []
        self._common_path = common_path
        self._row_count = 0

    def resetData(self, data):
        self.beginResetModel()
        self._data.clear()
        filenames = data.get_metadata_filenames()
        for filename in filenames:
            view_filename = data.get_derived_filenames(filename)
            thumbnail_filename = data.get_derived_filenames(view_filename)
            self._data.append([filename, view_filename, thumbnail_filename])

        self._row_count = len(self._data)
        self.endResetModel()

    def add_model_row(self):
        index = self.index(self._row_count, 0)
        self.beginInsertRows(index, self._row_count, self._row_count)
        self._data[self._row_count] = 'string'
        self._row_count = len(self._data)
        self.endInsertRows()

    def _get_item_from_index(self, index):
        return self._data[index.row()]

    def rowCount(self, parent):
        return self._row_count

    def columnCount(self, parent):
        return 3

    def data(self, index, role):
        if not index.isValid():
            return None

        item = self._get_item_from_index(index)

        if role == QtCore.Qt.DisplayRole:
            return item[index.column()].replace(self._common_path, '')

        if role == QtCore.Qt.UserRole:
            return item[index.column()]

        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            item = self._get_item_from_index(index)
            if role == QtCore.Qt.EditRole:
                self.dataChanged.emit(index, index)
                return True

        return False

    def flags(self, index):
        if index.isValid():
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

        return QtCore.Qt.NoItemFlags

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._headers[section]
