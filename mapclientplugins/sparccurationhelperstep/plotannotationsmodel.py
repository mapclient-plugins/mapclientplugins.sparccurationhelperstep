import os

from PySide6 import QtCore

_HEADERS = ['Annotations']


class PlotAnnotationItem(object):
    def __init__(self, data):
        self._children = []
        self._data = data
        self._parent_item = None

    def set_parent(self, parent_item):
        self._parent_item = parent_item

    def append_child(self, child):
        self._children.append(child)
        child.set_parent(self)

    def index_of(self, item):
        return self._children.index(item)

    def child(self, row):
        if 0 <= row < len(self._children):
            return self._children[row]

        return None

    def child_count(self):
        return len(self._children)

    def column_count(self):
        return len(self._data)

    def data(self, column):
        if 0 <= column < len(self._data):
            return self._data[column]

        return None

    def row(self):

        if self._parent_item is not None:
            return self._parent_item.index_of(self)

        return 0

    def parent_item(self):
        return self._parent_item


class PlotAnnotationsModelTree(QtCore.QAbstractItemModel):
    def __init__(self, common_path, parent=None):
        super(PlotAnnotationsModelTree, self).__init__(parent)
        self._root_item = None
        self._common_path = common_path

        self.reset_internal_data()

    def reset_internal_data(self):
        self._root_item = PlotAnnotationItem(_HEADERS)

    def reset_data(self, manifest):
        self.beginResetModel()
        self.reset_internal_data()
        plot_filenames = manifest.scaffold_get_plot_files()
        for plot_filename in plot_filenames:
            item = PlotAnnotationItem([plot_filename])
            self._root_item.append_child(item)
            thumbnail_filenames = manifest.get_source_of(plot_filename)
            for thumbnail_filename in thumbnail_filenames:
                thumbnail_item = PlotAnnotationItem([thumbnail_filename])
                item.append_child(thumbnail_item)
        self.endResetModel()

    def _get_item_from_index(self, index):
        return self._data[index.row()]

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parent_item = self._root_item
        else:
            parent_item = parent.internalPointer()

        return parent_item.child_count()

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().column_count()

        return self._root_item.column_count()

    def data(self, index, role):
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole:
            return item.data(index.column()).replace(self._common_path, '')

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parent_item = self._root_item
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        # print("PlotAnnotationsModel index child_item ", child_item)
        if child_item:
            return self.createIndex(row, column, child_item)

        # print("PlotAnnotationsModel index 2 ", row)

        return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parent_item()

        if parent_item == self._root_item:
            return QtCore.QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def flags(self, index):
        if index.isValid():
            parent_index = self.parent(index)
            if parent_index.isValid():
                grandparent_index = self.parent(parent_index)
                if grandparent_index.isValid():
                    return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
            return QtCore.Qt.ItemIsEnabled

        return QtCore.Qt.NoItemFlags

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._root_item.data(section)

        return None


class PlotAnnotationsModel(QtCore.QAbstractTableModel):
    def __init__(self, common_path, parent=None):
        super(PlotAnnotationsModel, self).__init__(parent)
        self._headers = ['Plot Metadata', 'Associated View', 'Associated Thumbnail']

        self._data = []
        self._common_path = common_path
        self._row_count = 0

    def resetData(self, data):
        self.beginResetModel()
        self._data.clear()
        filenames = data.get_metadata_filenames()
        for filename in filenames:
            thumbnail_filename = data.get_derived_filenames(filename)
            self._data.append([filename, ",".join(thumbnail_filename)])
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
