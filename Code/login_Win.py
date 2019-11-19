"""
*------------------------------------------------*
登录界面
运行主窗口
*------------------------------------------------*
"""


import qdarkstyle as qdarkstyle
from PyQt5.QtWidgets import  QMessageBox, QLineEdit,QWidget
from PyQt5 import  QtWidgets
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

import sys


from bookdata.ManagerLibrary import ManagerMainui
from Code.StudentLibrary import StudentMainUi
from Code.Login import Ui_Form
from Code.Register_win import DialogUI2



class DialogUI(QWidget,Ui_Form):
    def __init__(self):
        super(DialogUI, self).__init__()


        self.setupUi(self)
        #self.initUI()

        self.initLineEdit()
        self.initButton()
        self.show()

    #def initUI(self):

        """self.lineUser()  # 账户输入框
        self.linePassword()  # 密码输入框
        self.ButtonLogin()  # 登录按钮
        self.ButtonRegister  # 注册按钮"""

# -----------------------------------------登录界面设计-----------------------------------------
    def initLineEdit(self):
        """初始化输入框"""
        self.linePassword.setEchoMode(QLineEdit.Password)  # 设置密码不可见
        self.linePassword.textChanged.connect(self.Check_Input)  # 发射信号  输入框是否为空
        self.lineUser.textChanged.connect(self.Check_Input)  # 发射信号  输入框是否为空

    def initButton(self):
        """初始化登录和注册按钮为不可选择"""
        self.ButtonLogin.setEnabled(False)
        self.ButtonRegister.setEnabled(True)

        self.ButtonLogin.clicked.connect(self.Check_Login)  # 发射信号 核对密码是否正确
        self.ButtonRegister.clicked.connect(self.show_Register)

    def Check_Input(self, text):
        """检查输入框是否为空，输入框没有字符时，登录按钮不可选择"""
        if self.lineUser.text() and self.linePassword.text():
            self.ButtonLogin.setEnabled(True)
        else:
            self.ButtonLogin.setEnabled(False)

    def Check_Login(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('F:/pycharm项目/图书管理系统NEW/AllDataBase/database1.db')   # 打开成员信息匹配数据库
        if db.open():
            query = QSqlQuery()
        else:
            QMessageBox.information(self, 'error')
            return False
        AccountText = self.lineUser.text()  # 账户信息
        PassWordText = self.linePassword.text()  # 密码信息

        sql = "select * from denglupipei where ID='%s'" % (AccountText)     # 打开登录匹配表
        query.exec_(sql)
        if (not query.next()):
            QMessageBox.information(self, "提示", "该账号不存在")
            self.linePassword.clear()
            self.lineUser.clear()
        else:   # 如果账户存在
            if (PassWordText==query.value(1)):
                if (query.value(2)=='1'):   #权限为0：学生；为1：管理员
                    """ 若权限为1，打开管理员的图书管理系统"""
                    self.close()
                    self.ShowDataBase1=ManagerMainui()
                    self.ShowDataBase1.show()
                else:
                    """ 若权限为0，打开学生的图书查询系统"""
                    self.close()
                    self.ShowDataBase0 = StudentMainUi()
                    self.ShowDataBase0.StudentInfo.setText('用户信息:\n 账号：{0}\n 权限：{1}'.format(AccountText, '学生'))
                    self.ShowDataBase0.show()
                    
            else:   # 若密码出错
                QMessageBox.information(self, "提示", "密码错误！")
                self.linePassword.clear()
                self.lineUser.clear()
        db.close()


        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName('D:/install location/sqlite Expert Pro/Databases/database1.db')
        # if db.open():
        #     query=QSqlQuery()
        # else:
        #     QMessageBox.information(self,'error')
        #     return False
        # text1 = self.lineUser.text()
        # text2 = self.linePassword.text()
        #
        # sql="select * from denglupipei where ID='%s'"%(text1)
        # query.exec_(sql)
        #
        # if (not query.next()):
        #     QMessageBox.information(self,"提示","该账号不存在")
        #     self.linePassword.clear()
        #     self.lineUser.clear()
        # else:
        #     if (text2==query.value(1)):
        #         self.close()
        #         self.Show=Mainui()
        #         self.Show.show()
        #     else:
        #         QMessageBox.information(self, "提示", "密码错误！")
        #         self.linePassword.clear()
        #         #self.lineUser.clear()
        # db.close()

    def show_Register(self):
        self.Show = DialogUI2()
        self.Show.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DIALOG = DialogUI()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    sys.exit(app.exec_())