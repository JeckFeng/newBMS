"""
*------------------------------------------------*
学生图书查询系统界面
*------------------------------------------------*
"""

from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
import sys


from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QMessageBox, QHBoxLayout, QHeaderView, \
    QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QAction, QAbstractItemView


class StudentMainUi(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.search_layout = QtWidgets.QHBoxLayout()

        self.OpenRuslt = 0
        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecord = 0
        # 每页数据数
        self.pageRecord = 10
        self.initUi()

    # 初始化UI界面
    def initUi(self):

        # 设置窗口标题
        self.setWindowTitle("欢迎使用图书查询")
        # 设置窗口大小
        self.resize(700, 500)

        self.widget2 = QtWidgets.QWidget()
        self.layout = QGridLayout()
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        self.Hlayout3 = QHBoxLayout()
        self.Hlayout = QHBoxLayout()

        # Hlayout1
        # 创建一个文本框部件
        self.line = QtWidgets.QLineEdit()
        self.ButtonSerch = QtWidgets.QPushButton('查询')
        self.combox = QtWidgets.QComboBox()
        self.item = ['ISBN', 'BookName']
        self.combox.addItems(self.item)
        self.Hlayout1.addWidget(self.line)
        self.Hlayout1.addWidget(self.ButtonSerch)
        self.Hlayout1.addWidget(self.combox)

        # Hlayout2初始化
        self.jumpToLabel = QLabel("跳转到第")
        self.pageEdit = QLineEdit()
        self.pageEdit.setFixedWidth(30)
        s = "/" + str(self.totalPage) + "页"
        self.pageLabel = QLabel(s)
        self.jumpToButton = QtWidgets.QPushButton("跳转")
        self.prevButton = QtWidgets.QPushButton("前一页")
        self.prevButton.setFixedWidth(60)
        self.backButton = QtWidgets.QPushButton("后一页")
        self.backButton.setFixedWidth(60)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.jumpToLabel)
        Hlayout.addWidget(self.pageEdit)
        Hlayout.addWidget(self.pageLabel)
        Hlayout.addWidget(self.jumpToButton)
        Hlayout.addWidget(self.prevButton)
        Hlayout.addWidget(self.backButton)
        widget = QtWidgets.QWidget()
        widget.setLayout(Hlayout)

        self.Hlayout3.addWidget(widget)

        # 创建一个按钮组
        self.group_box = QtWidgets.QGroupBox()
        self.group_box_layout = QtWidgets.QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)

        # Table_View
        self.tableView = QtWidgets.QTableView()
        self.tableView.setFixedWidth(500)

        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.queryModel = QSqlQueryModel()
        self.ButtonSerch_clicked()
        self.tableView.setModel(self.queryModel)

        self.queryModel.setHeaderData(0, Qt.Horizontal, "ISBN")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "BookName")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "Author")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "Publisher")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "Date")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "Score")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "Photo")

        # 创建按钮组的按钮

        self.ButtonCreatDb = QtWidgets.QPushButton("打开数据库")
        self.ButtonCreatDb.setFixedHeight(40)
        self.ButtonCreatDb.setFixedWidth(90)

        self.ButtonClose = QtWidgets.QPushButton("退出")
        self.ButtonClose.setFixedHeight(40)
        self.ButtonClose.setFixedWidth(90)

        self.StudentInfo = QtWidgets.QTextEdit(" ")
        self.StudentInfo.setFixedHeight(100)
        self.StudentInfo.setFixedWidth(200)

        # 添加按钮到按钮组中

        self.group_box_layout.addWidget(self.StudentInfo)
        self.group_box_layout.addWidget(self.ButtonCreatDb)

        self.group_box_layout.addWidget(self.ButtonClose)

        self.Hlayout2.addWidget(self.group_box)
        self.Hlayout2.addWidget(self.tableView)

        self.layout.addLayout(self.Hlayout2, 1, 0)
        self.layout.addLayout(self.Hlayout1, 0, 0)
        self.layout.addLayout(self.Hlayout3, 2, 0)
        # self.layout.addWidget(self.StudentInfo,0,0)

        self.widget2.setLayout(self.layout)

        # 发射信号  clicked Or Triggered
        self.ButtonCreatDb.clicked.connect(self.openDb)   # 打开数据库信号
        self.ButtonClose.clicked.connect(self.close)    # 关闭信号
        self.ButtonSerch.clicked.connect(self.ButtonSerch_clicked)  # 查询
        self.backButton.clicked.connect(self.backButtonClicked)
        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.jumpToButton.clicked.connect(self.jumpToButtonClicked)

        self.setCentralWidget(self.widget2)
        self.show()


# -----------------------------------------------槽函数----------------------------------------

    """打开数据库的槽函数"""

    def openDb(self):

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('F:/pycharm项目/图书管理系统NEW/AllDataBase/book.db')

        db.open()

        # 显示数据库

        self.model = QtSql.QSqlTableModel()
        # 将数据库显示在表中
        self.tableView.setModel(self.model)

        self.model.setTable('BookData')  # 设置数据模型的数据表

        self.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)  # 不允许字段更改

        self.totalRecord = self.model.rowCount()
        self.totalPage = int(
            (self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        label = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(label)
        self.model.select()  # 查询所有数据
        # 设置表格头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ISBN')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'BookName')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Author')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'Publisher')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, 'Date')
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, 'Score')
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, 'Photo')
        self.OpenRuslt += 1

        # 显示有多少数据
        self.queryModel = QSqlQueryModel()
        queryCondition = "select * from BookData"
        self.queryModel.setQuery(queryCondition)
        self.totalRecord = self.queryModel.rowCount()
        self.totalPage = int(
            (self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        label = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(label)

    def setButtonStatus(self):
        if(self.currentPage == self.totalPage):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(False)
        if(self.currentPage == 1):
            self.backButton.setEnabled(True)
            self.prevButton.setEnabled(False)
        if(self.currentPage < self.totalPage and self.currentPage > 1):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(True)

    # 得到记录数
    def getTotalRecordCount(self):
        self.queryModel.setQuery("SELECT * FROM BookData")
        self.totalRecord = self.queryModel.rowCount()
        return

    # 得到总页数
    def getPageCount(self):
        self.getTotalRecordCount()
        # 上取整
        self.totalPage = int(
            (self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        print(self.totalPage)
        return

    def on_tableWidget_currentCellChanged(
            self,
            currentRow,
            currentColumn,
            previousRow,
            previousColumn):
        """
        当前单元格改变
        """
        pass

    def recordQuery(self, index):
        """
         查找
        """

        self.queryModel = QSqlQueryModel()
        self.tableView.setModel(self.queryModel)
        conditionChoice = self.combox.currentText()
        if (conditionChoice == "ISBN"):
            conditionChoice = 'ISBN'
        elif (conditionChoice == "BookName"):
            conditionChoice = 'BookName'

        if (self.line.text() == ""):
            queryCondition = "select * from BookData"
            self.queryModel.setQuery(queryCondition)
            self.totalRecord = self.queryModel.rowCount()
            self.totalPage = int(
                (self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)

            queryCondition = (
                "select * from BookData ORDER BY %s  limit %d,%d " %
                (conditionChoice, index, self.pageRecord))
            self.queryModel.setQuery(queryCondition)
            self.setButtonStatus()
            return

        # 得到模糊查询条件
        temp = self.line.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = (
            "SELECT * FROM BookData WHERE %s LIKE '%s' ORDER BY %s " %
            (conditionChoice, s, conditionChoice))
        self.queryModel.setQuery(queryCondition)
        self.totalRecord = self.queryModel.rowCount()

        self.totalPage = int(
            (self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        label = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(label)
        queryCondition = (
            "SELECT * FROM BookData WHERE %s LIKE '%s' ORDER BY %s LIMIT %d,%d " %
            (conditionChoice, s, conditionChoice, index, self.pageRecord))
        self.queryModel.setQuery(queryCondition)
        self.setButtonStatus()
        return

    def ButtonSerch_clicked(self):
        self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        self.getPageCount()
        s = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(s)
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向前翻页
    def prevButtonClicked(self):
        self.currentPage -= 1
        if (self.currentPage <= 1):
            self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向后翻页
    def backButtonClicked(self):
        self.currentPage += 1
        if (self.currentPage >= int(self.totalPage)):
            self.currentPage = int(self.totalPage)
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 点击跳转
    def jumpToButtonClicked(self):
        if (self.pageEdit.text().isdigit()):
            self.currentPage = int(self.pageEdit.text())
            if (self.currentPage > self.totalPage):
                self.currentPage = self.totalPage
            if (self.currentPage <= 1):
                self.currentPage = 1
        else:
            self.currentPage = 1
        index = (self.currentPage - 1) * self.pageRecord
        self.pageEdit.setText(str(self.currentPage))
        self.recordQuery(index)
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = StudentMainUi()

    sys.exit(app.exec_())
