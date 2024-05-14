import os.path

from PySide6 import QtCore

_HEADER = 'Annotations'


class ScaffoldAnnotationItem:
    def __init__(self, location, display):
        self._children = []
        self._location = location
        self._display = display
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

    @staticmethod
    def column_count():
        return 1

    def data(self, column, role):
        if column == 0:
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return self._display
            elif role == QtCore.Qt.ItemDataRole.UserRole:
                return self._location

        return None

    def row(self):

        if self._parent_item is not None:
            return self._parent_item.index_of(self)

        return 0

    def parent_item(self):
        return self._parent_item


class ScaffoldAnnotationsModelTree(QtCore.QAbstractItemModel):
    def __init__(self, common_path, parent=None):
        super(ScaffoldAnnotationsModelTree, self).__init__(parent)
        self._root_item = None
        self._common_path = common_path

        self.reset_internal_data()

    def reset_internal_data(self):
        self._root_item = ScaffoldAnnotationItem('', _HEADER)

    def reset_data(self, annotated_scaffold_dictionary):
        self.beginResetModel()
        self.reset_internal_data()
        for metadata, views in annotated_scaffold_dictionary.items():
            item = ScaffoldAnnotationItem(metadata, os.path.relpath(metadata, self._common_path))
            self._root_item.append_child(item)
            for view, view_children in views.items():
                view_item = ScaffoldAnnotationItem(view, os.path.relpath(view, self._common_path))
                item.append_child(view_item)
                for entry in view_children:
                    view_child_item = ScaffoldAnnotationItem(entry, os.path.relpath(entry, self._common_path))
                    view_item.append_child(view_child_item)

        self.endResetModel()

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

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        item = index.internalPointer()

        return item.data(index.column(), role)

    def index(self, row, column, parent=None):
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
                    return QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable
            return QtCore.Qt.ItemFlag.ItemIsEnabled

        return QtCore.Qt.ItemFlag.NoItemFlags

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self._root_item.data(section, role)

        return None
