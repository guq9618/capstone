# -*- coding: cp949 -*-
import sys
import os
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("interface.ui")[0]   
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        data_alllist=self.load_data()


        
        self.nh_btn.clicked.connect(self.nh_btn_clicked)
        self.ssg_btn.clicked.connect(self.ssg_btn_clicked)
        self.jjd_btn.clicked.connect(self.jjd_btn_clicked)
        self.log_btn.clicked.connect(self.log_btn_clicked)
        self.ys_btn.clicked.connect(self.ys_btn_clicked)
        self.del_btn.clicked.connect(self.del_btn_clicked)
        
    

        self.detail_text_lab.setText(data_alllist[0][1])


        parent_img="test"
        pixmap=QtGui.QPixmap(parent_img+".jpg")
        self.detail_image_lab1.setPixmap(pixmap)
        self.detail_image_lab1.setScaledContents(True)

        
        self.la1=QtGui.QLabel()
        self.la1.setPixmap(pixmap)
        self.la2=QtGui.QLabel('qweqwe')
        
        
        self.scro.setBackgroundRole(QtGui.QPalette.Dark)
        self.scro.setWidget(self.la1)
        self.scro.setWidget(self.la2)
        
        

    def load_data(self):
        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/feature")
        a=os.getcwd()
        b=os.listdir(a)
        
        

        for i in range(len(b)):
            data=open(b[i],"r")
            data_line=data.readline().split()
            data_list=[]

            while data_line!=[]:
                data_list.append(data_line)
                data_line=data.readline().split()
            data.close()

            if i==0:
                data_alllist=data_list
            else:
                data_alllist=data_alllist+data_list
        
        os.chdir(base_dir)
        return data_alllist

        
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
myWindow.showMaximized()                      
app.exec_()                          
