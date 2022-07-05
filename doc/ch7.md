### 设置用户权限
```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.11.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(211, 139)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(22, 19, 101, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(122, 19, 101, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(22, 49, 101, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(122, 49, 101, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(22, 78, 101, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 106, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.getvalue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getvalue(self):
        oper="" # 记录用户权限
        if self.checkBox.isChecked(): # 判断复选框是否选中
            oper+=self.checkBox.text() # 记录选中的权限
        if self.checkBox_2.isChecked():
            oper +='\n'+ self.checkBox_2.text()
        if self.checkBox_3.isChecked():
            oper+='\n'+ self.checkBox_3.text()
        if self.checkBox_4.isChecked():
            oper+='\n'+ self.checkBox_4.text()
        if self.checkBox_5.isChecked():
            oper+='\n'+ self.checkBox_5.text()
        from  PyQt5.QtWidgets import QMessageBox
        # 使用information()方法弹出信息提示，显示所有选择的权限
        QMessageBox.information(MainWindow, "提示", "您选择的权限如下：\n"+oper, QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设置用户权限"))
        self.checkBox.setText(_translate("MainWindow", "基本信息管理"))
        self.checkBox_2.setText(_translate("MainWindow", "进货管理"))
        self.checkBox_3.setText(_translate("MainWindow", "销售管理"))
        self.checkBox_4.setText(_translate("MainWindow", "库存管理"))
        self.checkBox_5.setText(_translate("MainWindow", "系统管理"))
        self.pushButton.setText(_translate("MainWindow", "设置"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程
```

### 选择列表类控件

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.12.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(244, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 15, 141, 22))
        self.comboBox.setObjectName("comboBox")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(35, 56, 171, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 定义职位列表
        list=["总经理", "副总经理", "人事部经理", "财务部经理", "部门经理", "普通员工" ]
        self.comboBox.addItems(list) # 将职位列表添加到ComboBox下拉列表中
        # 将ComboBox控件的选项更改信号与自定义槽函数关联
        self.comboBox.currentIndexChanged.connect(self.showinfo)

    def showinfo(self):
        self.label_2.setText("您选择的职位是："+self.comboBox.currentText()) # 显示选择的职位


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "职位："))


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程
```

```
 self.comboBox = QtWidgets.QComboBox(self.centralwidget)
 self.comboBox.setGeometry(QtCore.QRect(70, 15, 141, 22))
 self.comboBox.setObjectName("comboBox")
# 定义职位列表
list=["总经理", "副总经理", "人事部经理", "财务部经理", "部门经理", "普通员工" ]
self.comboBox.addItems(list) # 将职位列表添加到ComboBox下拉列表中
# 将ComboBox控件的选项更改信号与自定义槽函数关联
self.comboBox.currentIndexChanged.connect(self.showinfo)
```

### 字体组合框

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.13.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 87)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(30, 15, 213, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(38, 55, 191, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 设置字体组合框中显示所有字体
        self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.AllFonts)
        # 当选择的字体改变时，发射currentIndexChanged信号，调用setfont槽函数
        self.fontComboBox.currentIndexChanged.connect(self.setfont)

    # 自定义槽函数，用来将选择的字体设置为Label标签的字体
    def setfont(self):
        print(self.fontComboBox.currentText()) # 控制台中输出选择的字体
        # 为Label设置字体
        self.label.setFont(QtGui.QFont(self.fontComboBox.currentText()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "每天编程1小时，从菜鸟到大牛"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程
```

```
self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
self.fontComboBox.setGeometry(QtCore.QRect(30, 15, 213, 22))
self.fontComboBox.setObjectName("fontComboBox")
# 设置字体组合框中显示所有字体
self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.AllFonts)
# 当选择的字体改变时，发射currentIndexChanged信号，调用setfont槽函数
self.fontComboBox.currentIndexChanged.connect(self.setfont)
```

### 排行榜

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.14.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 350, 200))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 设置列表中可以多选
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # 设置选中方式为整行选中
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 设置以列表形式显示数据
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setWordWrap(True) # 设置自动换行
        from collections import OrderedDict

        # 定义有序字典，作为List列表的数据源
        dict=OrderedDict({'第1名':'战狼2,2017年上映，票房56.83亿','第2名':'哪吒之魔童降世，2019年上映，票房50.12亿',
                          '第3名':'流浪地球，2019年上映，票房46.86亿','第4名':'复仇者联盟：终局之战，2019年上映，票房42.50亿',
                          '第5名':'红海行动，2018年上映，票房36.51亿','第6名':'唐人街探案2，2018年上映，票房33.98亿',
                          '第7名': '美人鱼，2016年上映，票房33.86亿', '第8名': '我和我的祖国，2019年上映，票房31.71亿',
                          '第9名': '我不是药神，2018年上映，票房31.00亿', '第10名': '中国机长，2019年上映，票房29.13亿'})

        for key,value in dict.items():# 遍历字典，并分别获取到键值
            self.item = QtWidgets.QListWidgetItem(self.listWidget)# 创建列表项
            self.item.setText(key+'：'+value) # 设置项文本
            self.item.setToolTip(value)  # 设置提示文字

        self.listWidget.itemClicked.connect(self.gettext)

    # 自定义槽函数，获取列表选中项的值
    def gettext(self,item):
        if item.isSelected(): # 判断项是否选中
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.information(MainWindow,"提示","您选择的是："+item.text(),QMessageBox.Ok)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程
```

```
self.listWidget = QtWidgets.QListWidget(self.centralwidget)
self.listWidget.setGeometry(QtCore.QRect(0, 0, 350, 200))
self.listWidget.setObjectName("listWidget")

# 设置列表中可以多选
self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
# 设置选中方式为整行选中
self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
# 设置以列表形式显示数据
self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
self.listWidget.setWordWrap(True) # 设置自动换行
from collections import OrderedDict

# 定义有序字典，作为List列表的数据源
dict=OrderedDict({'第1名':'战狼2,2017年上映，票房56.83亿','第2名':'哪吒之魔童降世，2019年上映，票房50.12亿',
                  '第3名':'流浪地球，2019年上映，票房46.86亿','第4名':'复仇者联盟：终局之战，2019年上映，票房42.50亿',
                  '第5名':'红海行动，2018年上映，票房36.51亿','第6名':'唐人街探案2，2018年上映，票房33.98亿',
                  '第7名': '美人鱼，2016年上映，票房33.86亿', '第8名': '我和我的祖国，2019年上映，票房31.71亿',
                  '第9名': '我不是药神，2018年上映，票房31.00亿', '第10名': '中国机长，2019年上映，票房29.13亿'})

for key,value in dict.items():# 遍历字典，并分别获取到键值
    self.item = QtWidgets.QListWidgetItem(self.listWidget)# 创建列表项
    self.item.setText(key+'：'+value) # 设置项文本
    self.item.setToolTip(value)  # 设置提示文字

self.listWidget.itemClicked.connect(self.gettext)
# 自定义槽函数，获取列表选中项的值
    def gettext(self,item):
        if item.isSelected(): # 判断项是否选中
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.information(MainWindow,"提示","您选择的是："+item.text(),QMessageBox.Ok)

```

### 容器控件

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.15.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 187)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 301, 121))
        self.tabWidget.setObjectName("tabWidget")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.addtab) # 为“添加”按钮绑定单击信号
        self.pushButton_2.clicked.connect(self.deltab) # 为“删除”按钮绑定单击信号
        self.tabWidget.currentChanged.connect(self.gettab) # 为选项卡绑定页面切换信号

    # 新增选项卡
    def addtab(self):
        self.atab = QtWidgets.QWidget() # 创建选项卡对象
        name = "tab_"+str(self.tabWidget.count()+1) # 设置选项卡的对象名
        self.atab.setObjectName(name) # 设置选项卡的对象名
        self.tabWidget.addTab(self.atab, name) # 添加选项卡

    # 删除选项卡
    def deltab(self):
        self.tabWidget.removeTab(self.tabWidget.currentIndex()) # 移除当前选项卡

    # 获取选中的选项卡及索引
    def gettab(self,currentIndex):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(MainWindow,"提示","您选择了 "+ self.tabWidget.tabText(currentIndex)+" 选项卡，索引为： "+ str(self.tabWidget.currentIndex()),QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程
```

### 聊天室

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.16.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(142, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建ToolBox工具盒
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 141, 391))
        self.toolBox.setObjectName("toolBox")
        # 我的好友设置
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 141, 287))
        self.page.setObjectName("page")
        self.toolButton = QtWidgets.QToolButton(self.page)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 91, 51))

        ### 熬夜
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("图标/01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(96, 96))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.page)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 49, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("图标/02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.page)
        self.toolButton_3.setGeometry(QtCore.QRect(0, 103, 91, 51))

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("图标/03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolBox.addItem(self.page, "")

        # 同学设置
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 141, 287))
        self.page_2.setObjectName("page_2")
        self.toolButton_4 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_4.setGeometry(QtCore.QRect(0, 0, 91, 51))

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("图标/04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolBox.addItem(self.page_2, "")
        # 同事设置
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.toolButton_5 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_5.setGeometry(QtCore.QRect(0, 1, 91, 51))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("图标/05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_6.setGeometry(QtCore.QRect(0, 50, 91, 51))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("图标/06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolBox.addItem(self.page_3, "")
        # 陌生人设置
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.toolButton_7 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_7.setGeometry(QtCore.QRect(0, 7, 91, 51))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("图标/07.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_7.setAutoRaise(True)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolBox.addItem(self.page_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0) # 默认选择第一个页面，即我的好友
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的QQ"))
        self.toolButton.setText(_translate("MainWindow", "宋江"))
        self.toolButton_2.setText(_translate("MainWindow", "卢俊义"))
        self.toolButton_3.setText(_translate("MainWindow", "吴用"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "我的好友"))
        self.toolButton_4.setText(_translate("MainWindow", "林冲"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "同学"))
        self.toolButton_5.setText(_translate("MainWindow", "鲁智深"))
        self.toolButton_6.setText(_translate("MainWindow", "武松"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "同事"))
        self.toolButton_7.setText(_translate("MainWindow", "方腊"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "陌生人"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程
```

### 日期和时间类控件

```python

```

