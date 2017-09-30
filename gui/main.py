
from PyQt4.QtGui import *
from datamodel.model import Model
from gui.filter_model import FilterModel
from gui.list_model import ListModel
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.model = Model()
        self.model.load('test_asl')   #TODO: not necessary for final version

        frame = QFrame(self)
        self.setCentralWidget(frame)
        layout = QGridLayout(frame)

        self.phrase = QLineEdit(frame)
        layout.addWidget(self.phrase, 0, 0)

        self.list_view = QListView(frame)
        layout.addWidget(self.list_view, 1, 0)

        list_model = ListModel(self.model, self)
        filter_model = FilterModel(self)
        filter_model.setSourceModel(list_model)
        self.list_view.setModel(filter_model)
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.resize(480, 320)
    wnd.show()
    app.exec_()
