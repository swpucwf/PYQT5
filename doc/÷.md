### 常用PyQt5窗口常用的一些属性及说明。

![image-20220630232654767](C:%5CUsers%5CCWF%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220630232654767.png)

### 1 基本属性设置

窗口包含一些基本的组成要素，包括对象名称、图标、标题、位置和背景等，这些要素可以通过窗口中的“属性编辑器”窗口进行设置，也可以通过代码来实现。下面详细介绍窗口的常见属性设置。

（1）设置窗口的对象名称

窗口的对象名称，相当于窗口的标识，是唯一的，在编写代码时，对窗口的任何设置和使用都是通过该名称进行操作的。在Qt Designer设计器中，窗口的对象名称是通过“属性编辑器”中的objectName属性进行设置的，默认名称为MainWindow，如图1所示，用户可以根据实际情况进行更改，但要保证在当前窗口中是唯一的。

除了可以在Qt Designer设计器的“属性编辑器”中对其进行修改之外，还可以通过Python代码进行设置，设置时需要使用setObjectName()函数，使用方法如下：

```python
MainWindow.setObjectName("MainWindow")
```

### **2 设置窗口的标题栏名称**

在窗口的属性中，通过windowTitle属性设置窗口的标题栏名称，标题栏名称就是显示在窗口标题上的文本，windowTitle属性设置及窗口标题栏的预览效果分别如图2和图3所示。

![img](images/%C3%B7/3a3cb957f4744d48b34a905e33a455cd.png)

在Python中使用setWindowTitle()函数也可以设置窗口标题栏，代码如下：

```python
MainWindow.setWindowTitle(_translate("MainWindow", "标题栏"))
```

### 3.修改窗口的大小

在窗口的属性中，通过展开geometry属性，可以设置窗口的大小。修改窗口的大小，只需更改宽度和高度的值即可，如图4所示。

![img](images/%C3%B7/26b609efb16248e8bf72d79d29ae6747.png)

```python
MainWindow.resize(252, 100)
```

### 4.获取屏幕大小

```python
from PyQt5.QtWidgets import QDesktopWidget         # 导入屏幕类

screen=QDesktopWidget().screenGeometry()         # 获取屏幕大小

width=screen.width()                     # 获取屏幕的宽

height=screen.height()                     # 获取屏幕的高
```

### 5 更换窗口图标

添加一个新的窗口后，窗口的图标是系统默认的QT图标。如果想更换窗口的图标，可以在“属性编辑器”中设置窗口的windowIcon属性，窗口的系统默认图标和更换后的新图标如图5所示。

![img](images/%C3%B7/5742e8fc47684b48ae965ff4661344a4.png)

```python
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("K:/F盘/例图/图标/32×32(像素）/ICO/图标 (7).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
MainWindow.setWindowIcon(icon)
```

### 6.**设置窗口的背景**

使用setStyleSheet()函数设置窗口背景

在使用setStyleSheet()函数设置窗口背景时，需要以background-color或者border-image的方式来进行设置，其中background-color可以设置窗口的背景颜色；而border-image可以设置窗口的背景图片。

使用setStyleSheet()函数设置窗口背景颜色的代码如下：

使用了，但是失效：

```python
MainWindow.setStyleSheet("#MainWindow{background-color:red}")
```

```python
# 设置背景图片
MainWindow.setStyleSheet("#MainWindow{background-image:url(image/back.jpg)}")
```

### 使用QPalette设置窗口背景

1. **使用****QPalette****设置窗口背景**

```python
    from PyQt5.QtCore import Qt
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Background, Qt.red)
    MainWindow.setPalette(palette)
```

2. 设置背景图片

```python
   # 使用QPalette设置窗口背景图片

    from PyQt5.QtGui import QBrush, QPixmap
    MainWindow.resize(252, 100)
    palette = QtGui.QPalette()
    palette.setBrush(QtGui.QPalette.Background, QBrush(QPixmap("img.png")))
    MainWindow.setPalette(palette)
```

3.自适应背景图片大小

```python
MainWindow.resize(252, 100)

    palette = QtGui.QPalette()

    palette.setBrush(MainWindow.backgroundRole(), QBrush(
        QPixmap("img.png").scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio,
                                           QtCore.Qt.SmoothTransformation)))

    MainWindow.setPalette(palette)
```

### 4.背景透明度

```python
    MainWindow.setWindowOpacity(0.5)
```

### 5.添加问号

```python
   MainWindow.setWindowFlags(QtCore.Qt.Dialog)  # 显示一个有问号（？）和关闭按钮的对话框
```

![image-20220701005222766](images/%C3%B7/image-20220701005222766.png)

![image-20220701005235928](images/%C3%B7/image-20220701005235928.png)

MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint) # 只显示关闭按钮

```python
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
```

