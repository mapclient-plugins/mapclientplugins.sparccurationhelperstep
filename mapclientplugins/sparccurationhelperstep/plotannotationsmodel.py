import os

from PySide6 import QtCore

from mapclientplugins.sparccurationhelperstep.scaffoldannotationsmodel import ScaffoldAnnotationItem

_HEADERS = 'Annotations'


class PlotAnnotationsModelTree(QtCore.QAbstractItemModel):
    def __init__(self, common_path, parent=None):
        super(PlotAnnotationsModelTree, self).__init__(parent)
        self._root_item = None
        self._common_path = common_path

        self.reset_internal_data()

    def reset_internal_data(self):
        self._root_item = ScaffoldAnnotationItem('', _HEADERS)

    def reset_data(self, annotated_plot_dictionary):
        self.beginResetModel()
        self.reset_internal_data()
        for plot, thumbnails in annotated_plot_dictionary.items():
            item = ScaffoldAnnotationItem(plot, os.path.relpath(plot, self._common_path))
            self._root_item.append_child(item)
            for thumbnail in thumbnails:
                thumbnail_item = ScaffoldAnnotationItem(thumbnail, os.path.relpath(thumbnail, self._common_path))
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

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        item = index.internalPointer()

        return item.data(index.column(), role)

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parent_item = self._root_item
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)

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
                return self._root_item.data(section, role)

        return None
