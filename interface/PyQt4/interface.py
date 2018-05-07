# -*- coding: cp949 -*-
import clickable
import sys
import os
from functools import partial
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
        self.search_btn.clicked.connect(self.search_btn_clicked)

        
        parent_img="test"
        pixmap=QtGui.QPixmap(parent_img+".jpg")
        self.detail_image_lab1.setPixmap(pixmap)
        self.detail_image_lab1.setScaledContents(True)

        
        
        
        
        self.scro.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)        
        self.scro.setWidget(self.scrollAreaWidgetContents)

        
        
        


    def show_result(self):
        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/image")

        test_result=['red flower','desert','animal','castle','penghin','yellow flower','white flower','white flower','white flower','white flower']
        
        count=0
        self.la=[]

     

        
        for i in range(len(test_result)/3+1):
            for j in range(3):
                pixmap=QtGui.QPixmap("test"+str(count)+".jpg")
                self.la.append(QtGui.QLabel())
                pixmap=pixmap.scaledToWidth(150)
                self.la[count].setPixmap(pixmap)
                self.la[count].setScaledContents(True)
                self.gridLayout.addWidget(self.la[count], i, j)
                clickable.clickable(self.la[count]).connect(lambda x=count: self.show_detail(x,test_result[x]))
                if count==len(test_result):
                    break
                count=count+1
             
        os.chdir(base_dir)
        


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
        self.detail_text_lab.setText('qwe')

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

    def search_btn_clicked(self):
        self.show_result()

    def show_detail(self,index,detail):
        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/image")
        pixmap=QtGui.QPixmap("test"+str(index)+".jpg")
        self.detail_image_lab1.setPixmap(pixmap)
        os.chdir(base_dir)
        self.detail_text_lab.setText(detail)
                                     
app = QtGui.QApplication(sys.argv)   
myWindow = MyWindowClass()           
myWindow.showMaximized()                      
app.exec_()                          
