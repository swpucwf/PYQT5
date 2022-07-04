### 文本类控件

### 标签控件,label设置

```python
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 19:03
# @Author  : 陈伟峰
# @Site    : 
# @File    : 5-1.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 231)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 314, 81))
        self.label.setText("用户名：")

        # 设置文本对齐方式
        # self.label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        # 设置图片
        # from PyQt5.QtGui import QPixmap # 导入QPixmap类
        # self.label.setPixmap(QPixmap('test.png')) # 为label设置图片

        # # 设置超链接
        # self.label.setText("<a href='https://www.mingrisoft.com'>明日学院</a>")
        # self.label.setOpenExternalLinks(True) # 设置允许访问超链接
        #
        # # 设置长文本，并换行显示
        # self.label.setText("每天编程1小时，从菜鸟到大牛")
        # self.label.setWordWrap(True)

        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print(self.label.text()) # 获取Label的文本

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

### 设置文本对齐方式

```python
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 19:03
# @Author  : 陈伟峰
# @Site    : 
# @File    : 5-1.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 231)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 314, 81))
        self.label.setText("用户名：")

        # 设置文本对齐方式
        self.label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)


        # 设置图片
        # from PyQt5.QtGui import QPixmap # 导入QPixmap类
        # self.label.setPixmap(QPixmap('test.png')) # 为label设置图片

        # # 设置超链接
        # self.label.setText("<a href='https://www.mingrisoft.com'>明日学院</a>")
        # self.label.setOpenExternalLinks(True) # 设置允许访问超链接
        #
        # # 设置长文本，并换行显示
        # self.label.setText("每天编程1小时，从菜鸟到大牛")
        # self.label.setWordWrap(True)

        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print(self.label.text()) # 获取Label的文本

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

### 文本设置超链接

```python
 self.label.setText("<a href='https://www.baidu.com'>百度</a>")
 self.label.setOpenExternalLinks(True) # 设置允许访问超链接
```

```python
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 19:03
# @Author  : 陈伟峰
# @Site    : 
# @File    : 5-1.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 231)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 314, 81))
        self.label.setText("用户名：")

        # 设置文本对齐方式
        self.label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)


        # 设置图片
        # from PyQt5.QtGui import QPixmap # 导入QPixmap类
        # self.label.setPixmap(QPixmap('test.png')) # 为label设置图片

        # # 设置超链接
        self.label.setText("<a href='https://www.baidu.com'>百度</a>")
        self.label.setOpenExternalLinks(True) # 设置允许访问超链接
        #
        # # 设置长文本，并换行显示
        # self.label.setText("每天编程1小时，从菜鸟到大牛")
        # self.label.setWordWrap(True)

        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print(self.label.text()) # 获取Label的文本

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

### 为标签设置图片

```python
from PyQt5.QtGui import QPixmap # 导入QPixmap类
self.label.setPixmap(QPixmap('test.png')) # 为label设置图片

```

```python
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 19:03
# @Author  : 陈伟峰
# @Site    : 
# @File    : 5-1.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 231)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 314, 81))
        self.label.setText("用户名：")

        # 设置文本对齐方式
        self.label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)


        # 设置图片
        from PyQt5.QtGui import QPixmap # 导入QPixmap类
        self.label.setPixmap(QPixmap('test.png')) # 为label设置图片

        # # 设置超链接
        # self.label.setText("<a href='https://www.baidu.com'>百度</a>")
        # self.label.setOpenExternalLinks(True) # 设置允许访问超链接
        #
        # # 设置长文本，并换行显示
        # self.label.setText("每天编程1小时，从菜鸟到大牛")
        # self.label.setWordWrap(True)

        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print(self.label.text()) # 获取Label的文本

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



### 密码文本框写法

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 118)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 22, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 52, 54, 12))
        self.label_2.setObjectName("label_2")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 18, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) # 设置文本框为密码
        # 设置输入int 类型，范围
        self.lineEdit_2.setValidator(QtGui.QIntValidator(10000000,99999999)) # 设置只能输入8位数字

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 271, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "系统登录"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密  码："))


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':

   # 常规流程
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程
```

### 多行文本框TextEdit

```python
# 设置纯文本显示
self.textEdit.setPlainText('与失败比起来，我对乏味和平庸的恐惧要严重的多。'
                           '对我而言，很好的事要比糟糕的事好，而糟糕的事要比平庸的是好，因为糟糕的事至少给生活增加了滋味。')
# 设置HTML文本显示
self.textEdit_2.setHtml("与失败比起来，我对乏味和平庸的恐惧要严重的多。"
                        "对我而言，<font color='red' size=12>很好的事要比糟糕的事好，而糟糕的事要比平庸的是好，</font>因为糟糕的事至少给生活增加了滋味。")

```

### SpinBox

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(284, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(20, 10, 101, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(0) # 设置最小值
        self.spinBox.setMaximum(100) # 设置最大值
        self.spinBox.setSingleStep(2) # 设置步长值

        # # 通过setRange()方法设置最小值、最大值,等同于setMinimum和setMaximum
        self.spinBox.setRange(0,100)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 54, 12))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 284, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        # 将valueChanged信号与自定义槽函数相关联
        self.spinBox.valueChanged.connect(self.getvalue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 获取SpinBox的当前值，并显示在Label中
    def getvalue(self):
        self.label_2.setText(str(self.spinBox.value()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "当前控件中显示的数值："))

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

### DoubleSpinBox：小数数字选择控件

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(234, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 54, 12))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(20, 10, 101, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(0)  # 设置最小值
        self.doubleSpinBox.setMaximum(99.999)  # 设置最大值
        self.doubleSpinBox.setSingleStep(0.001)  # 设置步长值
        self.doubleSpinBox.setDecimals(3) # 设置保留3位小数

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 234, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        # 将valueChanged信号与自定义槽函数相关联
        self.doubleSpinBox.valueChanged.connect(self.getvalue)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # 获取SpinBox的当前值，并显示在Label中
    def getvalue(self):
        self.label_2.setText(str(self.doubleSpinBox.value()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "当前控件中显示的数值："))


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

### 液晶显示数字控件

```python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '5.5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(234, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 54, 12))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(20, 10, 101, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(0)  # 设置最小值
        self.doubleSpinBox.setMaximum(99.999)  # 设置最大值
        self.doubleSpinBox.setSingleStep(0.001)  # 设置步长值
        self.doubleSpinBox.setDecimals(3) # 设置保留3位小数

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 234, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        # 将valueChanged信号与自定义槽函数相关联
        self.doubleSpinBox.valueChanged.connect(self.getvalue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # 获取SpinBox的当前值，并显示在Label中
    def getvalue(self):
        self.label_2.setText(str(self.doubleSpinBox.value()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "当前控件中显示的数值："))


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

### 按钮控件

```python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '5.9.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(289, 84)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 20, 241, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.commandLinkButton.setText(_translate("MainWindow", "https://www.mingrisoft.com"))

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

### 命令链接按钮

```python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '5.9.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(289, 84)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 20, 241, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.commandLinkButton.setText(_translate("MainWindow", "https://www.mingrisoft.com"))

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

