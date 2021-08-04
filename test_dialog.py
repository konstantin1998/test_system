import sys
import test_window_ui
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi


class TestDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("C:/Users/galpe/anaconda3/envs/test_system/test_window.ui", self)
