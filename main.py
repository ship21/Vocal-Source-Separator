#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
"""
Created on Thu Nov 15 19 00:16:39 2018

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess 

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("Vocal Source Separator")
        Dialog.resize(784, 531)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-80, 0, 881, 201))
        self.frame.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.511, y1:0.886364, x2:0.125545, y2:0.086, stop:0.204545 rgba(21, 150, 91, 255), stop:1 rgba(21, 88, 152, 255))")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 10, 551, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: transparent;\n"
"border-image: none;\n"
"")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(-20, 180, 821, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setGeometry(QtCore.QRect(500, 10, 291, 331))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 291, 331))
        self.plainTextEdit.setStyleSheet("color:rgb(0, 124, 0)")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(340, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("icon-large")
        font.setPointSize(12)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.039, y1:0.0623636, x2:0, y2:0, stop:0.204545 rgba(124, 212, 74, 194), stop:1 rgba(21, 88, 152, 255))")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("icon-large")
        font.setPointSize(12)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.039, y1:0.0623636, x2:0, y2:0, stop:0.204545 rgba(124, 212, 74, 194), stop:1 rgba(21, 88, 152, 255))")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("icon-large")
        font.setPointSize(12)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.039, y1:0.0623636, x2:0, y2:0, stop:0.204545 rgba(124, 212, 74, 194), stop:1 rgba(21, 88, 152, 255))")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 300, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        Dialog.setFixedSize(784, 531)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.Browse)
        self.pushButton_2.clicked.connect(self.Convert)
        self.pushButton_3.clicked.connect(self.ShowGraphs)
        self.filePath=()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Vocal Source Separator</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">Vocal Source Separator is a Lyrics Generator Software</span></p></body></html>"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Your Lyrics will be shown here."))
        self.pushButton.setText(_translate("Dialog", " Browse "))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#007c00;\">Input Audio File</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", " Convert "))
        self.pushButton_3.setText(_translate("Dialog", "Get Graphs"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#007c00;\">Developed by: Saksham, Shipra &amp; Kareenah</span></p></body></html>"))

    def Browse(self):
        _translate = QtCore.QCoreApplication.translate
        self.filePath=QtWidgets.QFileDialog.getOpenFileName(self.frame,'Single File','/Users/shipra/Desktop','*.wav')
        print(self.filePath)
        
        x= len(self.filePath[0])
        i=x-1
        while i>=0:
            if(self.filePath[0][i]=='/'):
                break
            i=i-1
        filename=''.join(self.filePath[0][i+1:])
        self.lineEdit.setText(filename)
        
            
    def Convert(self):
        self.plainTextEdit.setPlainText('Your Lyrics will be shown here')
        x= len(self.filePath[0])
        i=x-1
        while i>=0:
            if(self.filePath[0][i]=='/'):
                break
            i=i-1
            
        os.chdir(self.filePath[0][:i+1])
        filename=self.filePath[0][i+1:]
        print(filename)
        subprocess.call('ffmpeg -i '+filename+' -f segment -segment_time 30 -c copy /Users/shipra/Desktop/Minor\ project\ Data/speech-to-text-master/parts/out%09d.wav' ,shell=True)
        os.chdir('/Users/shipra/Desktop/Minor project Data/speech-to-text-master/')
        os.system('python fast.py')
        with open("/Users/shipra/Desktop/Minor project Data/speech-to-text-master/transcript.txt", "r") as f:
            transcript=f.read()
            self.plainTextEdit.setPlainText(transcript)
            
    def ShowGraphs(self):
        os.chdir('/Users/shipra/Desktop/Minor project Data/speech-to-text-master/source')
        os.system('python plot_vocal_separation.py')
        
import ab_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

