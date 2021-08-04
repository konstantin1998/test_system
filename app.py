import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from test_dialog import TestDialog
from main_window_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()


    def connectSignalsSlots(self):
        self.commandLinkButton_3.clicked.connect(self.show_questions)


    def show_questions(self):
        dialog = TestDialog(self)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())