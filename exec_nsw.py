# Made by Grellik
from PyQt5 import QtWidgets, QtCore, QtGui
from start_dial import Ui_Dialog
import sys


class Ui_MainWindow():

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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
        self.pushButton_test.setText(
            _translate("MainWindow", "Parameters"))
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


class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_test.clicked.connect(self.openDialog)

    def openDialog(self):
        dialog = dialog_window(self)
        dialog.exec()


class dialog_window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(dialog_window, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.lineEdit.text() == "" or self.ui.lineEdit_2.text() == "" or self.ui.lineEdit_3.text() == "":
            self.ui.label_test.setText("One of fields is not completed")
            self.ui.label_test.adjustSize()
        else:
            grid_size = self.ui.lineEdit.text()
            num_species = self.ui.lineEdit_2.text()
            food_gen = self.ui.lineEdit_3.text()
            handle = open("config.txt", "w")
            l = [grid_size, num_species, food_gen]
            for i in l:
                handle.write(i + '\n')
            handle.close()
            self.close()


app = QtWidgets.QApplication(sys.argv)
application = main_window()
application.show()

sys.exit(app.exec())
