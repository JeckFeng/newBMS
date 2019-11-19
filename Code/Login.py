# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登录界面.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

"""
*------------------------------------------------*
登陆界面UI设计
UI转py
*------------------------------------------------*
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPalette, QIcon, QBrush

class Ui_Form(object):

    def setupUi(self, Form):
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('F:/pycharm项目/图书管理系统NEW/BackGroundPicture/LoginBackG.jpg')))  # 设置背景图片
        self.setPalette(palette1)
        Form.setObjectName("Form")
        Form.resize(914, 507)
        Form.setStyleSheet("*\n"
                           "{\n"
                       "font-size:16px;\n"
                           "font-family:sans-serif;\n"
                           "}\n"
                           "#Form{\n"
                           "background:url(F:/pycharm项目/图书管理系统NEW/BackGroundPicture/LoginBackG.jpg);\n"
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
        self.frame.setGeometry(QtCore.QRect(230, 80, 431, 311))
        self.frame.setStyleSheet(
                                "QFrame{\n"
                                 "background:rgba(0,0,0,0.5)\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ButtonLogin = QtWidgets.QPushButton(self.frame)
        self.ButtonLogin.setGeometry(QtCore.QRect(90, 240, 93, 28))
        self.ButtonLogin.setStyleSheet("QPushButton\n"
                                       "{\n"
                                       "background:#A3A3A3;\n"
                                       "border-radius:10px;\n"
                                       "    font: 9pt \"Microsoft Sans Serif\";\n"
                                       "}")
        self.ButtonLogin.setObjectName("ButtonLogin")
        self.ButtonRegister = QtWidgets.QPushButton(self.frame)
        self.ButtonRegister.setGeometry(QtCore.QRect(260, 240, 93, 28))
        self.ButtonRegister.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "background:#A3A3A3;\n"
                                          "border-radius:10px;\n"
                                          "    font: 9pt \"Microsoft Sans Serif\";\n"
                                          "}")
        self.ButtonRegister.setObjectName("ButtonRegister")
        self.linePassword = QtWidgets.QLineEdit(self.frame)
        self.linePassword.setGeometry(QtCore.QRect(40, 110, 361, 41))
        self.linePassword.setStyleSheet("QLineEdit{\n"
                                        "background:    #FFFFFF;\n"
                                        "border-style: solid;\n"
                                        "border-radius:15px;\n"
                                        "color:#1C86EE;\n"
                                        "}")
        self.linePassword.setText("")
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setObjectName("linePassword")
        self.lineUser = QtWidgets.QLineEdit(self.frame)
        self.lineUser.setGeometry(QtCore.QRect(40, 30, 361, 41))
        self.lineUser.setStyleSheet("QLineEdit{\n"
                                    "background:    #FFFFFF;\n"
                                    "border-style: solid;\n"
                                    "border-radius:15px;\n"
                                    "color:#1C86EE;\n"
                                    "}")
        self.lineUser.setText("")
        self.lineUser.setObjectName("lineUser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录界面"))
        self.ButtonLogin.setText(_translate("Form", "Login"))
        self.ButtonRegister.setText(_translate("Form", "Register"))
        self.linePassword.setPlaceholderText(_translate("Form", "Password"))
        self.lineUser.setPlaceholderText(_translate("Form", "UserName"))

        # ------------------------------------------------------------------------------------------------------------------



