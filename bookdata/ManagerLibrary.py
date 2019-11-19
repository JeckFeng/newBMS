"""
*------------------------------------------------*
管理员图书管理界面
*------------------------------------------------*
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView, QDataWidgetMapper, QFileDialog
import os
from Code.Library_UI import Ui_MainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import Qt, QItemSelectionModel, QModelIndex, QFile, QIODevice
from PyQt5 import QtSql
from PyQt5.QtGui import QPixmap
from run import ScrapyRun
from multiprocessing import Process, Pool
from scrapy import cmdline


class ManagerMainui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ManagerMainui, self).__init__()
        self.setupUi(self)
        self.opendb()
        self.show()
        self.lianjie()
        self.setCentralWidget(self.splitter)

        self.table_view.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_view.setSelectionMode(
            QAbstractItemView.SingleSelection)  # 一次选择单行还是多行
        self.table_view.setAlternatingRowColors(True)  # 隔行自动改变颜色
        self.table_view.verticalHeader().setDefaultSectionSize(22)
        self.table_view.horizontalHeader().setDefaultSectionSize(60)

        # 为菜单添加动作

        self.filemenu.addAction(self.exit_Act)
        self.Updata_Menu.addAction(self.Updata_Act)

        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecord = 0
        # 每页数据数
        self.pageRecord = 10

    def opendb(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('F:/pycharm项目/图书管理系统NEW/AllDataBase/book.db')
        if db.open():
            self._biaocaozuo()
        else:
            QMessageBox.information(self, 'warning', '无法建立与数据库的连接')
            return False

    def _biaocaozuo(self):
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('BookData')

        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)  # 设置保存策略

        self.table_view.setModel(self.model)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, 'ISBN')
        self.model.setHeaderData(1, Qt.Horizontal, '书名')
        self.model.setHeaderData(2, Qt.Horizontal, '作者')
        self.model.setHeaderData(3, Qt.Horizontal, '出版社')
        self.model.setHeaderData(4, Qt.Horizontal, '出版日期')
        self.model.setHeaderData(5, Qt.Horizontal, '评分')
        self.model.setHeaderData(6, Qt.Horizontal, '照片')
        self.table_view.setColumnHidden(6, True)

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)

        self.mapper.addMapping(self.lineEdit_ISBN, 0)
        self.mapper.addMapping(self.lineEdit_shuming, 1)
        self.mapper.addMapping(self.lineEdit_zuozhe, 2)
        self.mapper.addMapping(self.lineEdit_chubanshe, 3)
        self.mapper.addMapping(self.lineEdit_chubanriqi, 4)
        self.mapper.addMapping(self.lineEdit_pingfen, 5)
        self.mapper.toFirst()

        self.selModel = QItemSelectionModel(self.model)  # 选择模型
        self.table_view.setSelectionModel(self.selModel)
        self.selModel.currentChanged.connect(
            self.do_currentChanged)  # 当前项变化时触发
        self.selModel.currentRowChanged.connect(
            self.do_currentRowChanged)  # 选择行变化时

        # @pyqtSlot()  ##保存修改

    def on_p_baocun_triggered(self):
        result = QMessageBox.question(
            self,
            'warning',
            '你要保存你的修改吗？',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if result == QMessageBox.Yes:
            res = self.model.submitAll()
            if (res == False):
                QMessageBox.information(
                    self, "消息", "数据保存错误,错误信息\n" + self.model.lastError().text())
            else:
                QMessageBox.information(self, "message", "保存成功\n")
                self.p_baocun.setEnabled(False)
                self.p_quxiao.setEnabled(False)
        else:
            QMessageBox.information(self, 'message', 'Thanks')

    # @pyqtSlot()  ##取消修改

    def on_p_quxiao_triggered(self):
        # self.model.revertAll()
        result = QMessageBox.question(
            self,
            'warning',
            '确认取消之前所有的的操作吗？',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if result == QMessageBox.Yes:
            self.model.revertAll()
            self.p_baocun.setEnabled(False)
            self.p_quxiao.setEnabled(False)
        else:
            self.p_baocun.setEnabled(True)
            self.p_quxiao.setEnabled(True)

    # @pyqtSlot()  ##添加记录
    def on_p_zengjia_triggered(self):
        #self.model.insertRows(self.model.rowCount(), 1)
        self.model.insertRow(self.model.rowCount(), QModelIndex())  # 在末尾添加一个记录

        curIndex = self.model.index(
            self.model.rowCount() - 1,
            1)  # 创建最后一行的ModelIndex
        self.selModel.clearSelection()  # 清空选择项
        self.selModel.setCurrentIndex(
            curIndex, QItemSelectionModel.Select)  # 设置刚插入的行为当前选择行

    # 删除记录

    def on_p_sanchu_triggered(self):
        # if self.p_baocun.isEnabled():
        result = QMessageBox.question(
            self,
            'warning',
            '确认删除该记录吗？',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if result == QMessageBox.Yes:
            self.model.removeRow(self.table_view.currentIndex().row())
            self.p_baocun.setEnabled(True)
            self.p_quxiao.setEnabled(True)
        else:
            self.p_baocun.setEnabled(False)
            self.p_quxiao.setEnabled(False)

    # 插入记录

    def on_p_charu_triggered(self):
        curIndex = self.table_view.currentIndex()  # QModelIndex
        self.model.insertRow(curIndex.row(), QModelIndex())
        self.selModel.clearSelection()  # 清除已有选择
        self.selModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)

    # 对当前行设置图片
    def on_p_photo_triggered(self):
        fileName, filt = QFileDialog.getOpenFileName(
            self, "选择图片文件", "", "照片(*.jpg)")
        if (fileName == ''):
            return

        file = QFile(fileName)  # fileName为图片文件名
        file.open(QIODevice.ReadOnly)
        try:
            data = file.readAll()  # QByteArray
        finally:
            file.close()

        curRecNo = self.selModel.currentIndex().row()
        curRec = self.model.record(curRecNo)  # 获取当前记录QSqlRecord
        curRec.setValue("Photo", data)  # 设置字段数据
        self.model.setRecord(curRecNo, curRec)

        pic = QPixmap()
        pic.loadFromData(data)
        W = self.dbLabPhoto.width()
        self.dbLabPhoto.setPixmap(pic.scaledToWidth(W))  # 在界面上显示

    def closeEvent(self, event):
        """
        提示保存
        """
        if self.p_baocun.isEnabled():
            r = QMessageBox.warning(
                self,
                "注意",
                "你还没有保存，现在保存下？",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes)
            if r == QMessageBox.No:
                event.accept()
            else:
                event.ignore()

    def chaxun_ISBN(self):
        text1 = self.lineEdit_chaxun.text()
        self.model.setFilter(("ISBN='%s'" % (text1)))

    def chaxun_zuozhe(self):
        text2 = self.lineEdit_chaxun.text()
        self.model.setFilter(("author='%s'" % (text2)))

    def chaxun_shumin(self):
        text3 = self.lineEdit_chaxun.text()
        self.model.setFilter(("title='%s'" % (text3)))

    def chaxun_(self):
        """
        查找图书
        """
        searchtext = self.lineEdit_chaxun.text()
        if searchtext:
            if self.comboBox_chaxun.currentText() == "ISBN":
                self.chaxun_ISBN()
            elif self.comboBox_chaxun.currentText() == "书名":
                self.chaxun_shumin()
            elif self.comboBox_chaxun.currentText() == "作者":
                self.chaxun_zuozhe()
        else:
            QMessageBox.information(self, "提示", "请输入搜索关键词！")

    def on_p_quxiaoCX_triggered(self):
        self.lineEdit_chaxun.clear()
        self.model.setFilter("")

    def do_currentChanged(self, current, previous):  # 更新actPost和actCancel 的状态
        self.p_baocun.setEnabled(self.model.isDirty())  # 有未保存修改时可用
        self.p_quxiao.setEnabled(self.model.isDirty())

    def do_currentRowChanged(self, current, previous):  # 行切换时的状态控制
        self.mapper.setCurrentIndex(current.row())

        if (current.isValid() == False):
            self.dbLabPhoto.clear()  # 清除图片显示
            return

        self.mapper.setCurrentIndex(current.row())  # 更新数据映射的行号

        curRec = self.model.record(current.row())  # 获取当前记录,QSqlRecord类型
        if (curRec.isNull("Photo")):               # 图片字段内容为空
            self.dbLabPhoto.clear()
        else:
            # data=bytearray(curRec.value("Photo"))   #可以工作
            data = curRec.value("Photo")  # 也可以工作
            pic = QPixmap()
            pic.loadFromData(data)
            W = self.dbLabPhoto.size().width()
            self.dbLabPhoto.setPixmap(pic.scaledToWidth(W))

    def scrapy(self):
        """启动爬虫，在线更新功能"""

        # cmdline.execute(" scrapy ".split())
        self.hide()
        try:
            run=ScrapyRun()
        finally:
            pass


    def lianjie(self):
        self.p_zengjia.clicked.connect(self.on_p_zengjia_triggered)
        self.p_baocun.clicked.connect(self.on_p_baocun_triggered)
        self.p_quxiao.clicked.connect(self.on_p_quxiao_triggered)
        self.p_sanchu.clicked.connect(self.on_p_sanchu_triggered)
        self.p_charu.clicked.connect(self.on_p_charu_triggered)
        self.p_photo.clicked.connect(self.on_p_photo_triggered)
        self.p_chaxun.clicked.connect(self.chaxun_)
        self.p_quxiaoCX.clicked.connect(self.on_p_quxiaoCX_triggered)
        self.p_tuichu.clicked.connect(self.close)

        self.exit_Act.triggered.connect(self.close)
        self.Updata_Act.triggered.connect(self.scrapy)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ManagerMainui()
    sys.exit(app.exec())
