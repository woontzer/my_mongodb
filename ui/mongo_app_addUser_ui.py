# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\LSA_Pipeline\Mongo\ui\mongo_app_addUser_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 172)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.name_lineEdit = QtGui.QLineEdit(Dialog)
        self.name_lineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.horizontalLayout.addWidget(self.name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gender_comboBox = QtGui.QComboBox(Dialog)
        self.gender_comboBox.setObjectName(_fromUtf8("gender_comboBox"))
        self.gender_comboBox.addItem(_fromUtf8(""))
        self.gender_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.gender_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.department_comboBox = QtGui.QComboBox(Dialog)
        self.department_comboBox.setObjectName(_fromUtf8("department_comboBox"))
        self.department_comboBox.addItem(_fromUtf8(""))
        self.department_comboBox.addItem(_fromUtf8(""))
        self.department_comboBox.addItem(_fromUtf8(""))
        self.department_comboBox.addItem(_fromUtf8(""))
        self.department_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.department_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.contact_lineEdit = QtGui.QLineEdit(Dialog)
        self.contact_lineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.contact_lineEdit.setObjectName(_fromUtf8("contact_lineEdit"))
        self.horizontalLayout_4.addWidget(self.contact_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add New User", None))
        self.label.setText(_translate("Dialog", "Name", None))
        self.label_2.setText(_translate("Dialog", "Gender", None))
        self.gender_comboBox.setItemText(0, _translate("Dialog", "male", None))
        self.gender_comboBox.setItemText(1, _translate("Dialog", "female", None))
        self.label_3.setText(_translate("Dialog", "Department", None))
        self.department_comboBox.setItemText(0, _translate("Dialog", "modeling", None))
        self.department_comboBox.setItemText(1, _translate("Dialog", "animation", None))
        self.department_comboBox.setItemText(2, _translate("Dialog", "developer", None))
        self.department_comboBox.setItemText(3, _translate("Dialog", "managing", None))
        self.department_comboBox.setItemText(4, _translate("Dialog", "concept art", None))
        self.label_4.setText(_translate("Dialog", "Contact", None))
        self.pushButton.setText(_translate("Dialog", "Add", None))

