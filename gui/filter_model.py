
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QSortFilterProxyModel

class FilterModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super(FilterModel, self).__init__(parent)
        self.substring = ''
    
    def getText(self, index):
        text = index.data(Qt.DisplayRole).toString()
        return text
        
    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        text = self.getText(index)
        if len(self.substring)==0:
            return True
        else:
            return text.contains(self.substring)

    def lessThan(self, source_left, source_right):
        text_left = self.getText(source_left)
        text_right = self.getText(source_right)
        return text_left.compare(text_right) < 0
        