# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\learn\pyQt\firstui.ui'
#
# Created: Mon May 13 14:41:46 2013
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_MainBoard(object):
    def setupUi(self, MainBoard):
        MainBoard.setObjectName(_fromUtf8("MainBoard"))
        MainBoard.resize(224, 369)
        self.tabs = QtGui.QTabWidget(MainBoard)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 231, 371))
        self.tabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.user = QtGui.QLineEdit(self.tab1)
        self.user.setGeometry(QtCore.QRect(70, 140, 113, 20))
        self.user.setObjectName(_fromUtf8("user"))
        self.label = QtGui.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(10, 140, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.exitButton = QtGui.QPushButton(self.tab1)
        self.exitButton.setGeometry(QtCore.QRect(80, 290, 75, 23))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.loginButton = QtGui.QPushButton(self.tab1)
        self.loginButton.setGeometry(QtCore.QRect(30, 250, 75, 23))
        self.loginButton.setDefault(False)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.pswd = QtGui.QLineEdit(self.tab1)
        self.pswd.setGeometry(QtCore.QRect(70, 180, 113, 20))
        self.pswd.setEchoMode(QtGui.QLineEdit.Password)
        self.pswd.setObjectName(_fromUtf8("pswd"))
        self.savebox = QtGui.QCheckBox(self.tab1)
        self.savebox.setGeometry(QtCore.QRect(70, 220, 101, 16))
        self.savebox.setObjectName(_fromUtf8("savebox"))
        self.infobox = QtGui.QTextBrowser(self.tab1)
        self.infobox.setGeometry(QtCore.QRect(10, 20, 201, 71))
        self.infobox.setObjectName(_fromUtf8("infobox"))
        self.logoutButton = QtGui.QPushButton(self.tab1)
        self.logoutButton.setGeometry(QtCore.QRect(130, 250, 75, 23))
        self.logoutButton.setDefault(False)
        self.logoutButton.setFlat(False)
        self.logoutButton.setObjectName(_fromUtf8("logoutButton"))
        self.tabs.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.tabs.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.label_3 = QtGui.QLabel(self.tab3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab3)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabs.addTab(self.tab3, _fromUtf8(""))

        self.retranslateUi(MainBoard)
        self.tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainBoard.close)
        QtCore.QMetaObject.connectSlotsByName(MainBoard)

    def retranslateUi(self, MainBoard):
        MainBoard.setWindowTitle(_translate("MainBoard", "Dialog", None))
        self.label_2.setText(_translate("MainBoard", "PassWord", None))
        self.label.setText(_translate("MainBoard", "UserName", None))
        self.exitButton.setText(_translate("MainBoard", "Exit", None))
        self.loginButton.setText(_translate("MainBoard", "Login", None))
        self.savebox.setText(_translate("MainBoard", "Save Password", None))
        self.logoutButton.setText(_translate("MainBoard", "Logout", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab1), _translate("MainBoard", "login", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab2), _translate("MainBoard", "config", None))
        self.label_3.setText(_translate("MainBoard", "Author: GingerWine", None))
        self.label_4.setText(_translate("MainBoard", "Version: 0.1 alpha", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab3), _translate("MainBoard", "about", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainBoard = QtGui.QDialog()
    ui = Ui_MainBoard()
    ui.setupUi(MainBoard)
    MainBoard.show()
    sys.exit(app.exec_())

