# Made by Grellik
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow():

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(-5, -7, 500, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setGeometry(QtCore.QRect(690, 90, 75, 23))
        self.pushButton_test.setObjectName("pushButton_test")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        self.menuStart_simulation = QtWidgets.QMenu(self.menubar)
        self.menuStart_simulation.setObjectName("menuStart_simulation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart_new_simulation = QtWidgets.QAction(MainWindow)
        self.actionStart_new_simulation.setObjectName(
            "actionStart_new_simulation")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionChange_parameters = QtWidgets.QAction(MainWindow)
        self.actionChange_parameters.setObjectName("actionChange_parameters")
        self.actionAdd_species = QtWidgets.QAction(MainWindow)
        self.actionAdd_species.setObjectName("actionAdd_species")
        self.actionEnd_simulation = QtWidgets.QAction(MainWindow)
        self.actionEnd_simulation.setObjectName("actionEnd_simulation")
        self.menuStart_simulation.addAction(self.actionStart_new_simulation)
        self.menuStart_simulation.addAction(self.actionChange_parameters)
        self.menuStart_simulation.addAction(self.actionAdd_species)
        self.menuStart_simulation.addAction(self.actionEnd_simulation)
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuStart_simulation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next day"))
        self.pushButton_2.setText(_translate("MainWindow", "Statistics"))
        self.pushButton_test.setText(_translate("MainWindow", "test_button"))
        self.menuQuit.setTitle(_translate("MainWindow", "Quit"))
        self.menuStart_simulation.setTitle(
            _translate("MainWindow", "Simulation"))
        self.actionStart_new_simulation.setText(
            _translate("MainWindow", "Start new simulation"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionChange_parameters.setText(
            _translate("MainWindow", "Change parameters"))
        self.actionAdd_species.setText(_translate("MainWindow", "Add species"))
        self.actionEnd_simulation.setText(
            _translate("MainWindow", "End simulation"))
