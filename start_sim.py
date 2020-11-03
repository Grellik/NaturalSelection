# Made by Grellik
def start_sim():
    from start_dial import Ui_Dialog
    from PyQt5 import QtWidgets
    import sys

    class app_dialog(QtWidgets.QMainWindow):
        def __init__(self):
            super(app_dialog, self).__init__()
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

                return grid_size, num_species, food_gen

    app = QtWidgets.QApplication([])
    application = app_dialog()
    application.show()

    sys.exit(app.exec())


start_sim()
