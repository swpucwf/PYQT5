# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 490, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")



        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showMessage(self):
        from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类

        # 使用information()方法弹出信息提示框

        QMessageBox.information(MainWindow, "提示框","欢迎进入PyQt5编程世界" ,QMessageBox.Yes |  QMessageBox.No,defaultButton= QMessageBox.Yes)
    def retranslateUi(self, MainWindow):
        '''
        主题框
        :param MainWindow:
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("design")
        # 改变窗口大小
        # MainWindow.resize(200,200)
        MainWindow.setWindowTitle(_translate("MainWindow", "标题栏目"))
        self.pushButton.setText(_translate("MainWindow", "点一下"))
        # 信号与槽
        self.pushButton.clicked.connect(self.showMessage)

        # 设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)


import sys
# 程序入口，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    # from PyQt5.QtWidgets import QDesktopWidget
    # screen = QDesktopWidget().screenGeometry()
    # width = screen.width()
    # height = screen.height()
    # print(width,height)

    ui = Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    # 设置背景图片
    MainWindow.setObjectName("MainWindow")


    # from PyQt5.QtCore import Qt
    # palette = QtGui.QPalette()
    # palette.setColor(QtGui.QPalette.Background, Qt.red)
    # MainWindow.setPalette(palette)

    # 使用QPalette设置窗口背景图片

    # from PyQt5.QtGui import QBrush, QPixmap
    # MainWindow.resize(252, 100)
    # palette = QtGui.QPalette()
    # palette.setBrush(QtGui.QPalette.Background, QBrush(QPixmap("img.png")))
    # MainWindow.setPalette(palette)

    # 使用QPalette设置窗口背景图片(自动适应窗口大小)

    # MainWindow.resize(252, 100)
    #
    # palette = QtGui.QPalette()
    #
    # palette.setBrush(MainWindow.backgroundRole(), QBrush(
    #     QPixmap("img.png").scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio,
    #                                        QtCore.Qt.SmoothTransformation)))
    #
    # MainWindow.setPalette(palette)

    # MainWindow.setWindowOpacity(0.5)
    MainWindow.setWindowFlags(QtCore.Qt.Dialog)  # 显示一个有问号（？）和关闭按钮的对话框
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮

    # 设置背景
    # MainWindow.setStyleSheet("#MainWindow{background-color:red}")
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程