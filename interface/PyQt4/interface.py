import sys
import os
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("interface.ui")[0]   

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.nh_btn.clicked.connect(self.nh_btn_clicked)
        self.ssg_btn.clicked.connect(self.ssg_btn_clicked)
        self.jjd_btn.clicked.connect(self.jjd_btn_clicked)
        self.log_btn.clicked.connect(self.log_btn_clicked)
        self.ys_btn.clicked.connect(self.ys_btn_clicked)
        self.del_btn.clicked.connect(self.del_btn_clicked)
        
        lab=QtGui.QLabel(self)
        lab.setGeometry(500,420,200,170)
        parent_img="test"
        pixmap=QtGui.QPixmap(parent_img+".jpg")
        lab.setPixmap(pixmap)
        lab.setScaledContents(True)
        lab.show()


    def nh_btn_clicked(self):
        parent_avi="test"

    def ssg_btn_clicked(self):
        parent_avi="test"
        
    def jjd_btn_clicked(self):
        parent_avi="test"

    def log_btn_clicked(self):
        parent_avi="test"

    def ys_btn_clicked(self):
        parent_avi="test"
        os.system(parent_avi+".avi")
        
    def del_btn_clicked(self):
        parent_avi="test"
        
app = QtGui.QApplication(sys.argv)   
myWindow = MyWindowClass()           
myWindow.show()                      
app.exec_()                          
