"""
*------------------------------------------------*
注册界面
*------------------------------------------------*
"""

import qdarkstyle as qdarkstyle
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5 import  QtWidgets
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

import sys
from Code.Register import Ui_Form2


class DialogUI2(QWidget,Ui_Form2):
    def __init__(self):
        super(DialogUI2, self).__init__()

        self.setupUi(self)

        #self.initUI()
        self.initLineEditRe()
        self.initButtonRe()
        self.show()
    #
    # def initUI(self):
    #         """self.lineUser()  # 账户输入框
    #         self.linePassword()  # 密码输入框
    #         self.ButtonLogin()  # 登录按钮
    #         self.ButtonRegister  # 注册按钮"""

    def initLineEditRe(self):
        self.lineUsername2.textChanged.connect(self.Check_InputRe)
        self.linePassword2.textChanged.connect(self.Check_InputRe)
        self.linePasswordR2.textChanged.connect(self.Check_InputRe)

    def initButtonRe(self):
        self.ButtonSubmit.setEnabled(False)
        self.ButtonSubmit.clicked.connect(self.Check_Register)


    def Check_InputRe(self):
        if self.lineUsername2.text() and self.linePassword2.text() and self.linePasswordR2.text():
            self.ButtonSubmit.setEnabled(True)
        else:
            self.ButtonSubmit.setEnabled(False)

    def Check_Register(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('F:/pycharm项目/图书管理系统NEW/AllDataBase/database1.db')   # 打开成员信息匹配数据库
        if db.open():
            query = QSqlQuery()
        else:
            QMessageBox.information(self, '无法匹配到登录信息')
            return False
        AccountText = self.lineUsername2.text()     # 账号输入
        PassWordText1 = self.linePassword2.text()   # 第一次密码输入
        PassWordText2 = self.linePasswordR2.text()  # 第二次密码输入

        sql="select * from zhucupipei where ID='%s'"% (AccountText)    # 注册匹配表
        sql2 = "select * from denglupipei where ID='%s'"% (AccountText)     # 登录匹配表，是否已经注册
        query.exec_(sql)
        bool1=query.next()      # 布尔值1判断，在注册匹配表中是否存在（是否允许注册）
        
        query.exec_(sql2)
        bool2=query.next()   # 布尔值2判断，在登录匹配表中是否存在（是否已经注册）
        

        if (not bool1):     # 判断布尔值1
            QMessageBox.information(self,"提示","你不能注册")
            self.lineUsername2.clear()
            self.linePassword2.clear()
            self.linePasswordR2.clear()
        elif (bool2):       # 判断布尔值2
            QMessageBox.information(self, "提示", "该账号已注册")
            self.lineUsername2.clear()
            self.linePassword2.clear()
            self.linePasswordR2.clear()
            
        else:
            if PassWordText1 == PassWordText2:
                query.exec("insert into denglupipei values('%s','%s','0')"%(AccountText,PassWordText1))
                QMessageBox.information(self, "提示", "注册成功")
                self.close()
            else:
                QMessageBox.information(self, "提示", "两次密码不一致")
                self.linePassword2.clear()
                self.linePasswordR2.clear()
        db.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DIALOG = DialogUI2()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    sys.exit(app.exec_())