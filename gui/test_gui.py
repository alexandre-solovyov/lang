
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from datamodel.model import Model
from list_model import ListModel
from filter_model import FilterModel

app = QApplication(sys.argv)

model = Model()
model.load('testdata/test1.lang')

lmodel = ListModel(model)
fmodel = FilterModel()
fmodel.substring = 'p'
fmodel.setSourceModel(lmodel)
fmodel.setSortRole(Qt.DisplayRole)
fmodel.sort(0, Qt.AscendingOrder)

list_view = QListView()
list_view.setModel(fmodel)

list_view.show()
app.exec_()
