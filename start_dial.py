# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_dial.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 250)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 30, 80, 240))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 230, 20))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 100, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 230, 16))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 230, 21))
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 110, 100, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_test = QtWidgets.QLabel(Dialog)
        self.label_test.setGeometry(QtCore.QRect(10, 130, 230, 16))
        self.label_test.setObjectName("label_test")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Starting parameters"))
        self.label.setText(_translate("Dialog", "Size of the grid :"))
        self.label_2.setText(_translate("Dialog", "Number of species :"))
        self.label_3.setText(_translate(
            "Dialog", "Number of food units per day :"))
