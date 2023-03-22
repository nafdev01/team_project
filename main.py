# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_files/mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 10, 751, 531))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageConnect = QtWidgets.QWidget()
        self.pageConnect.setObjectName("pageConnect")
        self.buttonConnServer = QtWidgets.QPushButton(self.pageConnect)
        self.buttonConnServer.setGeometry(QtCore.QRect(230, 220, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.buttonConnServer.setFont(font)
        self.buttonConnServer.setObjectName("buttonConnServer")
        self.stackedWidget.addWidget(self.pageConnect)
        self.pageAuth = QtWidgets.QWidget()
        self.pageAuth.setObjectName("pageAuth")
        self.authTabs = QtWidgets.QTabWidget(self.pageAuth)
        self.authTabs.setGeometry(QtCore.QRect(50, 50, 651, 451))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.authTabs.setFont(font)
        self.authTabs.setObjectName("authTabs")
        self.tabLogin = QtWidgets.QWidget()
        self.tabLogin.setObjectName("tabLogin")
        self.inputNickLog = QtWidgets.QLineEdit(self.tabLogin)
        self.inputNickLog.setGeometry(QtCore.QRect(310, 110, 161, 31))
        self.inputNickLog.setObjectName("inputNickLog")
        self.labelNickLog = QtWidgets.QLabel(self.tabLogin)
        self.labelNickLog.setGeometry(QtCore.QRect(140, 110, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelNickLog.setFont(font)
        self.labelNickLog.setObjectName("labelNickLog")
        self.inputPassLog = QtWidgets.QLineEdit(self.tabLogin)
        self.inputPassLog.setGeometry(QtCore.QRect(310, 160, 161, 31))
        self.inputPassLog.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassLog.setObjectName("inputPassLog")
        self.labelPassLog = QtWidgets.QLabel(self.tabLogin)
        self.labelPassLog.setGeometry(QtCore.QRect(140, 160, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPassLog.setFont(font)
        self.labelPassLog.setObjectName("labelPassLog")
        self.input2FALog = QtWidgets.QLineEdit(self.tabLogin)
        self.input2FALog.setGeometry(QtCore.QRect(310, 210, 161, 31))
        self.input2FALog.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input2FALog.setObjectName("input2FALog")
        self.label2FALog = QtWidgets.QLabel(self.tabLogin)
        self.label2FALog.setGeometry(QtCore.QRect(140, 210, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label2FALog.setFont(font)
        self.label2FALog.setObjectName("label2FALog")
        self.buttonLogin = QtWidgets.QPushButton(self.tabLogin)
        self.buttonLogin.setGeometry(QtCore.QRect(270, 300, 101, 31))
        self.buttonLogin.setObjectName("buttonLogin")
        self.labelTitleLog = QtWidgets.QLabel(self.tabLogin)
        self.labelTitleLog.setGeometry(QtCore.QRect(280, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitleLog.setFont(font)
        self.labelTitleLog.setObjectName("labelTitleLog")
        self.authTabs.addTab(self.tabLogin, "")
        self.tabSignup = QtWidgets.QWidget()
        self.tabSignup.setObjectName("tabSignup")
        self.inputNickSign = QtWidgets.QLineEdit(self.tabSignup)
        self.inputNickSign.setGeometry(QtCore.QRect(190, 90, 161, 31))
        self.inputNickSign.setObjectName("inputNickSign")
        self.labelNickSign = QtWidgets.QLabel(self.tabSignup)
        self.labelNickSign.setGeometry(QtCore.QRect(40, 90, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelNickSign.setFont(font)
        self.labelNickSign.setObjectName("labelNickSign")
        self.inputPassSign = QtWidgets.QLineEdit(self.tabSignup)
        self.inputPassSign.setGeometry(QtCore.QRect(190, 140, 161, 31))
        self.inputPassSign.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassSign.setObjectName("inputPassSign")
        self.labelPassSign = QtWidgets.QLabel(self.tabSignup)
        self.labelPassSign.setGeometry(QtCore.QRect(40, 140, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPassSign.setFont(font)
        self.labelPassSign.setObjectName("labelPassSign")
        self.labelQRCode = QtWidgets.QLabel(self.tabSignup)
        self.labelQRCode.setGeometry(QtCore.QRect(410, 90, 161, 161))
        self.labelQRCode.setObjectName("labelQRCode")
        self.inputPassConfSign = QtWidgets.QLineEdit(self.tabSignup)
        self.inputPassConfSign.setGeometry(QtCore.QRect(190, 190, 161, 31))
        self.inputPassConfSign.setText("")
        self.inputPassConfSign.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassConfSign.setObjectName("inputPassConfSign")
        self.labelPassConfSign = QtWidgets.QLabel(self.tabSignup)
        self.labelPassConfSign.setGeometry(QtCore.QRect(40, 190, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPassConfSign.setFont(font)
        self.labelPassConfSign.setObjectName("labelPassConfSign")
        self.buttonSign = QtWidgets.QPushButton(self.tabSignup)
        self.buttonSign.setGeometry(QtCore.QRect(180, 310, 101, 31))
        self.buttonSign.setObjectName("buttonSign")
        self.input2FASign = QtWidgets.QLineEdit(self.tabSignup)
        self.input2FASign.setGeometry(QtCore.QRect(190, 240, 161, 31))
        self.input2FASign.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input2FASign.setObjectName("input2FASign")
        self.label2FASign = QtWidgets.QLabel(self.tabSignup)
        self.label2FASign.setGeometry(QtCore.QRect(40, 240, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label2FASign.setFont(font)
        self.label2FASign.setObjectName("label2FASign")
        self.button2FAGen = QtWidgets.QPushButton(self.tabSignup)
        self.button2FAGen.setGeometry(QtCore.QRect(420, 310, 141, 31))
        self.button2FAGen.setObjectName("button2FAGen")
        self.labelTitleSign = QtWidgets.QLabel(self.tabSignup)
        self.labelTitleSign.setGeometry(QtCore.QRect(260, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitleSign.setFont(font)
        self.labelTitleSign.setObjectName("labelTitleSign")
        self.authTabs.addTab(self.tabSignup, "")
        self.stackedWidget.addWidget(self.pageAuth)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.authTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonConnServer.clicked.connect(self.connect_to_server)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonConnServer.setText(_translate("MainWindow", "CONNECT"))
        self.labelNickLog.setText(_translate("MainWindow", "Nickname"))
        self.labelPassLog.setText(_translate("MainWindow", "Password"))
        self.label2FALog.setText(_translate("MainWindow", "2FA Code"))
        self.buttonLogin.setText(_translate("MainWindow", "Log In"))
        self.labelTitleLog.setText(_translate("MainWindow", "LOG IN"))
        self.authTabs.setTabText(
            self.authTabs.indexOf(self.tabLogin), _translate("MainWindow", "Login")
        )
        self.labelNickSign.setText(_translate("MainWindow", "Nickname"))
        self.labelPassSign.setText(_translate("MainWindow", "Password"))
        self.labelQRCode.setText(_translate("MainWindow", "QRCode"))
        self.labelPassConfSign.setText(_translate("MainWindow", "Confirm Password"))
        self.buttonSign.setText(_translate("MainWindow", "Sign Up"))
        self.label2FASign.setText(_translate("MainWindow", "2FA Code"))
        self.button2FAGen.setText(_translate("MainWindow", "Generate QRCode"))
        self.labelTitleSign.setText(_translate("MainWindow", "SIGN UP"))
        self.authTabs.setTabText(
            self.authTabs.indexOf(self.tabSignup), _translate("MainWindow", "Signup")
        )

    def connect_to_server(self):
        self.stackedWidget.setCurrentIndex(1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
