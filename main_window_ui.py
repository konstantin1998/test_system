# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 591, 431))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout.addWidget(self.commandLinkButton_3)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout.addWidget(self.commandLinkButton_2)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.verticalLayout.addWidget(self.commandLinkButton_4)
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.verticalLayout.addWidget(self.commandLinkButton_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Вариант1"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Вариант2"))
        self.commandLinkButton.setText(_translate("MainWindow", "Вариант3"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "Вариант4"))
        self.commandLinkButton_5.setText(_translate("MainWindow", "Вариант5"))
