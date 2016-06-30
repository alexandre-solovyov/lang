
from PyQt4.QtCore import QAbstractListModel, QVariant, Qt

class ListModel(QAbstractListModel):
    def __init__(self, model, parent=None):
        super(ListModel, self).__init__(parent)
        self.model = model
        
    def rowCount(self, index):
        if index.isValid():
            return 0
        else:
            return len(self.model.lines)
            
    def data(self, index, role):
        row = index.row()
        if role==Qt.DisplayRole and index.column()==0:
            item_text = self.model.lines[row].text
            return item_text
        return QVariant()
        