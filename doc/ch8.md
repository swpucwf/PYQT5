### 进度条类控件
```python

# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '6.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 259)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(50, 180, 201, 31))
        self.progressBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar_2.setProperty("value", -1)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(20, 10, 31, 201))
        self.progressBar_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_3.setProperty("value", -1)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar_3.setTextVisible(True)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_3.setObjectName("progressBar_3")
        
        self.progressBar_1 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_1.setGeometry(QtCore.QRect(250, 10, 31, 201))
        self.progressBar_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_1.setProperty("value", -1)
        self.progressBar_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar_1.setTextVisible(True)
        self.progressBar_1.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_1.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_1.setObjectName("progressBar_1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 220, 101, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QBasicTimer() # 创建定时器对象
        # 为按钮绑定单击信号
        self.pushButton.clicked.connect(self.running)
    # 控制进度条的滚动效果
    def running(self):
        if self.timer.isActive(): # 判断计时器是否开启
            self.timer.stop() # 停止计时器
            self.pushButton.setText('开始')# 设置按钮的文本
            # 设置4个进度条的最大值为100
            self.progressBar.setMaximum(100)
            self.progressBar_1.setMaximum(100)
            self.progressBar_2.setMaximum(100)
            self.progressBar_3.setMaximum(100)
        else:
            self.timer.start(100,MainWindow) # 启动计时器
            self.pushButton.setText('停止') # 设置按钮的文本
            # 将4个进度条的最大值和最小值都设置为0，以便显示循环滚动的效果
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(0)
            
            self.progressBar_1.setInvertedAppearance(True) # 设置进度反方向显示
            self.progressBar_1.setMinimum(0)
            self.progressBar_1.setMaximum(0)
            self.progressBar_2.setMinimum(0)
            self.progressBar_2.setMaximum(0)
            self.progressBar_3.setMinimum(0)
            self.progressBar_3.setMaximum(0)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "跑马灯效果"))
        self.pushButton.setText(_translate("MainWindow", "开始"))

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
![image-20220707124852198](images/ch8/image-20220707124852198.png)

### 自定义提示框,设置自定义提示框

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(150, 20, 100, 100))
        self.loading.setStyleSheet("")
        self.loading.setText("")
        self.loading.setObjectName("loading")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 140, 100, 50))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(250, 140, 100, 50))
        self.pushButton_stop.setObjectName("pushButton_stop")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_start.clicked.connect(self.start_loading)  # 启动加载提示框
        self.pushButton_stop.clicked.connect(self.stop_loading)  # 停止加载提示框

    def start_loading(self):
        self.gif = QtGui.QMovie('loading.gif')  # 加载gif图片
        self.loading.setMovie(self.gif)  # 设置gif图片
        self.gif.start()  # 启动图片，实现等待gif图片的显示

    def stop_loading(self):
        self.gif.stop()
        self.loading.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "启动等待提示"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止等待提示"))


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

### 使用滑块改变刻度值以及标签中字体大小

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建横向滑块
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 10, 231, 22))
        self.horizontalSlider.setMinimum(8) # 设置最小值为8
        self.horizontalSlider.setMaximum(72) # 设置最大值为72
        self.horizontalSlider.setSingleStep(1) # 设置通过鼠标拖动时的步长值
        self.horizontalSlider.setPageStep(1) # 设置通过鼠标点击时的步长值
        self.horizontalSlider.setProperty("value", 8) # 设置默认值为8
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal) # 设置滑块为横向滑块
        # 设置在滑块上方显示刻度
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(3) # 设置刻度的间隔
        self.horizontalSlider.setObjectName("horizontalSlider")
        # 创建垂直滑块
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(270, 20, 22, 171))
        self.verticalSlider.setMinimum(8) # 设置最小值为8
        self.verticalSlider.setMaximum(72) # 设置最大值为72
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical) # 设置滑块为垂直滑块
        self.verticalSlider.setInvertedAppearance(True) # 设置刻度反方向显示
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksRight) # 设置在滑块右侧显示刻度
        self.verticalSlider.setTickInterval(3) # 设置刻度的间隔
        self.verticalSlider.setObjectName("verticalSlider")
        # 创建一个水平布局管理器，主要用来放置显示文字的Label
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 251, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 创建Label控件，用来显示文字
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter) # 设置文字居中对齐
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label) # 将Label添加到水平布局管理器中
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为横向滑块绑定valueChanged信号，在值发生更改是发射
        self.horizontalSlider.valueChanged.connect(self.setfontsize)
    # 定义槽函数，根据横向滑块的值改变垂直滑块的值和Label控件的字体大小
    def setfontsize(self):
        value = self.horizontalSlider.value()
        self.verticalSlider.setValue(value)
        self.label.setFont(QtGui.QFont("楷体", value))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "敢想敢为，注重细节"))

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

