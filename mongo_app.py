import qdarkstyle
import pymongo

import sys
import math

from PyQt4 import QtGui
from PyQt4 import QtCore


import mongo_app_ui
import mongo_app_addUser_ui

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, mymongo, header, *args):
        super(MyTableModel, self).__init__()
        self.mymongo = mymongo
        self.header = header

    def rowCount(self, parent):
        return self.mymongo.get_users_count()

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.mymongo.get_row_column(index.row(), index.column())
        else:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            if role == QtCore.Qt.EditRole:
                # node = index.internalPointer()
                # node.setName(value)
                # print index
                # print dir(index)
                # print 8888888
                # print dir(value)
                # x = value.toPyObject()
                # print type(x)
                # print x
                # print index.row()
                # print index.column()
                # print dir(index)
                self.mymongo.set_row_column(index.row(), index.column(), value.toPyObject())
                return True
        return False


    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    # def sort(self, col, order):
    #     """sort table by given column number col"""
    #     self.emit(SIGNAL("layoutAboutToBeChanged()"))
    #     self.mylist = sorted(self.mylist,
    #         key=operator.itemgetter(col))
    #     if order == QtCore.Qt.DescendingOrder:
    #         self.mylist.reverse()
    #     self.emit(SIGNAL("layoutChanged()"))

class MyMongo(QtCore.QObject):
    warning_signal = QtCore.pyqtSignal(str, str)

    def __init__(self, ip, port):
        super(MyMongo, self).__init__()
        self._client = pymongo.MongoClient(ip, port)
        self._db = None
        self._collection = None

    def database_exists(self, database_name):
        for db_name in self._client.database_names():
            if database_name == db_name:
                return True
        return False

    def set_database(self, database_name):
        if self.database_exists(database_name):
            self._db = self._client[database_name]

    def get_user(self, name):
        # return a 'dict' or None if not found
        return self._collection.find_one({'name':name})

    def set_collection(self, collection_name):
        if self._db != None:
            try:
                self._db.validate_collection(collection_name)
                self._collection = self._db[collection_name]
            except:
                pass

    def collection(self):
        return self._collection

    def warning(self, caption, text):
        self.warning_signal.emit(caption, text)

    def add_user(self, name="", gender="", department="", contact=""):
        if self._db != None and self._collection != None:
            if name == '':
                self.warning("Error", "User name is blank")
                return False
            if self.get_user(name) == None:
                new_user = {"name": name, "gender": gender, "department": department, "contact": contact}
                self._collection.insert(new_user)
                return True
            else:
                self.warning("Error", "Fail to add user. The user already exists")
                return False

    def delete_user(self, id):
        # `id` can be type: int or str
        # if type:str, it is assumed <name> being passed
        # if type:int, it is assumed <row column> being passed
        if self._collection != None:
            name = ''
            if type(id) == str:
                name = id
            elif type(id) == int:
                name = self.get_row_column(id, 0)
            self._collection.remove({"name": name})

    def print_users(self):
        if self._collection != None:
            cursor = self._collection.find().sort('name', pymongo.ASCENDING)
            for doc in cursor:
                print doc

    def get_users_count(self):
        if self._collection != None:
            return self._collection.count()

    def get_row_column(self, row, column):
        # row is userid, column is the field
        # return a dict
        cursor = self._collection.find().sort('name', pymongo.ASCENDING)
        if row < cursor.count() and row >= 0:
            doc = cursor[row] # doc => type:dict
            column_to_fieldname = {0:'name', 1:'gender', 2:'department', 3:'contact'}
            key = column_to_fieldname[column]
            if key in doc.keys():
                return doc[key]
            else:
                return ''
        return ''

    def set_row_column(self, row, column, value):
        cursor = self._collection.find().sort('name', pymongo.ASCENDING)
        if row < cursor.count() and row >= 0:
            doc = cursor[row]  # doc => type:dict
            column_to_fieldname = {0: 'name', 1: 'gender', 2: 'department', 3: 'contact'}
            key = column_to_fieldname[column]
            if key in doc.keys():
                self._collection.update({'name':doc['name']}, {"$set": {key:str(value)}}, upsert=False)
            else:
                return None
        return None

header = ['Name', ' Gender', ' Department', ' Contact']

class AddUserDialog(QtGui.QDialog, mongo_app_addUser_ui.Ui_Dialog):
    data_signal = QtCore.pyqtSignal(dict)
    close_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(AddUserDialog, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.add_user)

    def add_user(self):
        # return signal to main window
        name = str(self.name_lineEdit.text())
        # gender = str(self.gender_lineEdit.text())
        gender = str(self.gender_comboBox.currentText())
        # department = str(self.department_lineEdit.text())
        department = str(self.department_comboBox.currentText())
        contact = str(self.contact_lineEdit.text())
        self.data_signal.emit({"name":name, "gender":gender, "department":department, "contact":contact})

    def closeEvent(self, event):
        self.close_signal.emit()
        super(AddUserDialog, self).closeEvent(event)

    def close(self):
        self.close_signal.emit()
        super(AddUserDialog, self).close()

class MainUiClass(QtGui.QMainWindow, mongo_app_ui.Ui_MainWindow):
    add_user_success_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)

        self.add_user_dialog = None

        self.mongo = MyMongo('192.168.4.190', 60080)

        # lets work on <sample> db
        self.mongo.set_database('sample')
        self.mongo.set_collection('v001')

        self.mongo.warning_signal.connect(self.display_warning)

        self.table_model = MyTableModel(self, self.mongo, header)
        self.tableView.setModel(self.table_model)

        self.tableView.delete_row_signal.connect(self.delete_row)

        self.connect(self.add_user_button, QtCore.SIGNAL("clicked()"), self.show_add_user_dialog)

    def display_warning(self, caption, text):
        QtGui.QMessageBox.about(self, caption, text)

    def delete_row(self, int):
        self.mongo.delete_user(int)
        self.table_model.layoutChanged.emit()

    def add_user(self, new_user_dict):
        name = new_user_dict['name']
        gender = new_user_dict['gender']
        department = new_user_dict['department']
        contact = new_user_dict['contact']

        ret = self.mongo.add_user(name, gender, department, contact)
        if ret:
            self.table_model.layoutChanged.emit()
            self.add_user_success_signal.emit()

    def show_add_user_dialog(self):
        if self.add_user_dialog == None:
            self.add_user_dialog = AddUserDialog(self)
            self.add_user_dialog.data_signal.connect(self.add_user)
            self.add_user_dialog.close_signal.connect(self.user_dialog_closed)
            self.add_user_success_signal.connect(self.add_user_dialog.close)
            self.add_user_dialog.show()

    def user_dialog_closed(self):
        self.add_user_dialog = None

    def closeEvent(self, *args, **kwargs):
        self.deleteLater()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    win = MainUiClass()
    win.show()
    sys.exit(app.exec_())