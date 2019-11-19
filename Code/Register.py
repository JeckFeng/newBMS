# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '注册界面.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

"""
*------------------------------------------------*
注册界面UI设计

UI转py
*------------------------------------------------*
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPalette, QIcon, QBrush

class Ui_Form2(object):
    def setupUi(self, Form):
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('F:/pycharm项目/图书管理系统NEW/BackGroundPicture/RegisterBackG.jpg')))  # 设置背景图片
        self.setPalette(palette1)

        Form.setObjectName("Form")
        Form.resize(914, 549)
        Form.setStyleSheet("*\n"
"{\n"
"font-size:16px;\n"
"font-family:sans-serif;\n"
"}\n"
"#Form{\n"
"background:url(picture/RegisterBackG.jpg);\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"color:#1C86EE;\n"
"\n"
"}\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(230, 150, 431, 311))
        self.frame.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.5)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ButtonSubmit = QtWidgets.QPushButton(self.frame)
        self.ButtonSubmit.setGeometry(QtCore.QRect(100, 260, 231, 28))
        self.ButtonSubmit.setStyleSheet("QPushButton\n"
"{\n"
"background:#A3A3A3;\n"
"border-radius:10px;\n"
"    font: 9pt \"Microsoft Sans Serif\";\n"
"}")
        self.ButtonSubmit.setObjectName("ButtonSubmit")
        self.linePassword2 = QtWidgets.QLineEdit(self.frame)
        self.linePassword2.setGeometry(QtCore.QRect(40, 110, 361, 41))
        self.linePassword2.setStyleSheet("QLineEdit{\n"
"background:    #FFFFFF;\n"
"border-style: solid;\n"
"border-radius:15px;\n"
"color:#1C86EE;\n"
"}")
        self.linePassword2.setText("")
        self.linePassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword2.setObjectName("linePassword2")
        self.lineUsername2 = QtWidgets.QLineEdit(self.frame)
        self.lineUsername2.setGeometry(QtCore.QRect(40, 30, 361, 41))
        self.lineUsername2.setStyleSheet("QLineEdit{\n"
"background:    #FFFFFF;\n"
"border-style: solid;\n"
"border-radius:15px;\n"
"color:#1C86EE;\n"
"}")
        self.lineUsername2.setText("")
        self.lineUsername2.setObjectName("lineUsername2")
        self.linePasswordR2 = QtWidgets.QLineEdit(self.frame)
        self.linePasswordR2.setGeometry(QtCore.QRect(40, 180, 361, 41))
        self.linePasswordR2.setStyleSheet("QLineEdit{\n"
"background:    #FFFFFF;\n"
"border-style: solid;\n"
"border-radius:15px;\n"
"color:#1C86EE;\n"
"}")
        self.linePasswordR2.setText("")
        self.linePasswordR2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePasswordR2.setObjectName("linePasswordR2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册界面"))
        self.ButtonSubmit.setText(_translate("Form", "Subimit"))
        self.linePassword2.setPlaceholderText(_translate("Form", "Password"))
        self.lineUsername2.setPlaceholderText(_translate("Form", "UserName"))
        self.linePasswordR2.setPlaceholderText(_translate("Form", "Password"))


