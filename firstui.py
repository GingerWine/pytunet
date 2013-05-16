# -*- coding: utf-8 -*-

"""
Module implementing PyTunet.
"""
import PyQt4, PyQt4.QtGui, sys
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_firstui import Ui_MainBoard
from wintunet import *
from getpass import getpass
from hashlib import md5

class PyTunet(QDialog, Ui_MainBoard):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_loginButton_clicked(self):
        """
        Slot documentation goes here.
        """
        userName = self.user.text()
        passWord = self.pswd.text() # this function returns a QString type
        userName = str(userName)
        passWord = str(passWord) # convert it to normal string to avoid md5 calculating error
     
        m = md5()
        m.update(passWord)
        pswdMD5 = m.hexdigest()
        (status, text) = login(userName, pswdMD5)
        self.infobox.setText(text)
        return
        
    @pyqtSignature("")
    def on_logoutButton_clicked(self):
        logoutInfo = logout()
        print logoutInfo
        self.infobox.setText(logoutInfo)
        
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    dlg = PyTunet()
    dlg.show()
    sys.exit(app.exec_()) 
    
