
from PyQt4 import QtCore, QtGui

class mongoTableView(QtGui.QTableView):
    delete_row_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(mongoTableView, self).__init__(parent)

    def contextMenuEvent(self, event):
        self.menu = QtGui.QMenu(self)
        deleteAction = QtGui.QAction('Delete user', self)
        deleteAction.triggered.connect(lambda: self.deleteSlot(event))
        self.menu.addAction(deleteAction)
        # add other required actions
        self.menu.popup(QtGui.QCursor.pos())

    def deleteSlot(self, event):
         self.delete_row_signal.emit(self.selectionModel().currentIndex().row())
