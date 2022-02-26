# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 467)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pictures/img/fl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 471))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 411, 131))
        self.textBrowser.setStyleSheet("background:transparent;background-color: rgb(247,248,250);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 411, 31))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 240, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pictures/img/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 240, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pictures/img/favo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 360, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background:transparent")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 401, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:transparent")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(82, 305, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:transparent")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(110, 240, 80, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 251, 16))
        self.label_5.setStyleSheet("background:transparent;\n"
"color: rgb(138, 138, 138);")
        self.label_5.setObjectName("label_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_6.setGeometry(QtCore.QRect(12, 74, 59, 16))
        self.radioButton_6.setStyleSheet("background:transparent;")
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_6)
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 72, 366, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_8 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_8.setStyleSheet("background:transparent;")
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup.addButton(self.radioButton_8)
        self.horizontalLayout_2.addWidget(self.radioButton_8)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_5.setStyleSheet("background:transparent;")
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup.addButton(self.radioButton_5)
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_10 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_10.setStyleSheet("background:transparent;")
        self.radioButton_10.setObjectName("radioButton_10")
        self.buttonGroup.addButton(self.radioButton_10)
        self.horizontalLayout_2.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_11.setStyleSheet("background:transparent;")
        self.radioButton_11.setObjectName("radioButton_11")
        self.horizontalLayout_2.addWidget(self.radioButton_11)
        self.radioButton_9 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_9.setStyleSheet("background:transparent;")
        self.radioButton_9.setObjectName("radioButton_9")
        self.horizontalLayout_2.addWidget(self.radioButton_9)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(12, 52, 71, 16))
        self.radioButton_2.setStyleSheet("background:transparent;")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 50, 366, 23))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton.setStyleSheet("background:transparent;")
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup.addButton(self.radioButton)
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_4.setStyleSheet("background:transparent;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_7 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_7.setStyleSheet("background:transparent;")
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup.addButton(self.radioButton_7)
        self.horizontalLayout.addWidget(self.radioButton_7)
        self.radioButton_12 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_12.setStyleSheet("background:transparent;")
        self.radioButton_12.setObjectName("radioButton_12")
        self.buttonGroup.addButton(self.radioButton_12)
        self.horizontalLayout.addWidget(self.radioButton_12)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_3.setStyleSheet("background:transparent;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 240, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pictures/img/网站.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(270, 240, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pictures/img/喇叭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 400, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background:transparent;")
        self.pushButton_13.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pictures/img/刷新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setObjectName("pushButton_13")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pictures/img/favo (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 371, 151))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet("background:transparent;\n"
"background-color: rgb(247,248,250);")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 170, 371, 251))
        self.textBrowser_2.setAutoFillBackground(True)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"background-color: rgb(247,248,250);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 130, 51, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border-radius:2px;\n"
"background-color: rgb(242,58,58);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 10, 78, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background:")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/pictures/img/docu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 70, 78, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/pictures/img/grab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 130, 78, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 100, 78, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/pictures/img/人工.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 40, 78, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/pictures/img/图片.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon10)
        self.pushButton_11.setObjectName("pushButton_11")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/pictures/img/trans.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon11, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 371, 411))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 10, 71, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/pictures/img/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon12)
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 40, 71, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/pictures/img/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon13)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_3, icon2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber.setGeometry(QtCore.QRect(130, 60, 261, 51))
        self.lcdNumber.setStyleSheet("background:transparent")
        self.lcdNumber.setDigitCount(9)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 494, 447))
        self.label_11.setStyleSheet("background-image: url(:/pictures/img/bgt6.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setGeometry(QtCore.QRect(30, 150, 137, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.widget1 = QtWidgets.QWidget(self.tab_4)
        self.widget1.setGeometry(QtCore.QRect(170, 150, 111, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_2.setStyleSheet("background:transparent")
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_2.addWidget(self.lcdNumber_2)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_5.setStyleSheet("background:transparent")
        self.lcdNumber_5.setDigitCount(10)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.verticalLayout_2.addWidget(self.lcdNumber_5)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_4.setStyleSheet("background:transparent")
        self.lcdNumber_4.setDigitCount(10)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout_2.addWidget(self.lcdNumber_4)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_3.setStyleSheet("background:transparent")
        self.lcdNumber_3.setDigitCount(10)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_2.addWidget(self.lcdNumber_3)
        self.label_11.raise_()
        self.lcdNumber.raise_()
        self.label_6.raise_()
        self.lcdNumber_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.lcdNumber_3.raise_()
        self.label_10.raise_()
        self.lcdNumber_4.raise_()
        self.lcdNumber_5.raise_()
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/pictures/img/satis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon14, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        self.comboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "外语词汇学习系统"))
        self.pushButton.setText(_translate("Dialog", "查询"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入您要查询的单词"))
        self.pushButton_3.setText(_translate("Dialog", "退出"))
        self.pushButton_2.setText(_translate("Dialog", "收藏"))
        self.label.setText(_translate("Dialog", "eng"))
        self.label_2.setText(_translate("Dialog", "chn"))
        self.label_3.setText(_translate("Dialog", "28"))
        self.label_4.setText(_translate("Dialog", "Dec."))
        self.comboBox.setCurrentText(_translate("Dialog", "切换用户"))
        self.comboBox.setPlaceholderText(_translate("Dialog", "切换用户"))
        self.label_5.setText(_translate("Dialog", "----------------------"))
        self.radioButton_6.setText(_translate("Dialog", "汉译西"))
        self.radioButton_8.setText(_translate("Dialog", "汉译韩"))
        self.radioButton_5.setText(_translate("Dialog", "汉译俄"))
        self.radioButton_10.setText(_translate("Dialog", "简译繁"))
        self.radioButton_11.setText(_translate("Dialog", "汉译古"))
        self.radioButton_9.setText(_translate("Dialog", "汉译粤"))
        self.radioButton_2.setText(_translate("Dialog", "自动检测"))
        self.radioButton.setText(_translate("Dialog", "汉译英"))
        self.radioButton_4.setText(_translate("Dialog", "汉译法"))
        self.radioButton_7.setText(_translate("Dialog", "汉译德"))
        self.radioButton_12.setText(_translate("Dialog", "汉译意"))
        self.radioButton_3.setText(_translate("Dialog", "汉译日"))
        self.pushButton_10.setText(_translate("Dialog", "四六级官网"))
        self.pushButton_12.setText(_translate("Dialog", "朗读"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "查词"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "请输入您要翻译的文字"))
        self.pushButton_8.setText(_translate("Dialog", "翻译"))
        self.pushButton_4.setText(_translate("Dialog", "选择文档"))
        self.pushButton_7.setText(_translate("Dialog", "截图翻译"))
        self.comboBox_2.setCurrentText(_translate("Dialog", "中英互译"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "中英互译"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "中法互译"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "中日互译"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "中俄互译"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "中德互译"))
        self.pushButton_9.setText(_translate("Dialog", "人工翻译"))
        self.pushButton_11.setText(_translate("Dialog", "选择图片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "翻译"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "源语言"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "目标语言"))
        self.pushButton_6.setText(_translate("Dialog", "删除"))
        self.pushButton_5.setText(_translate("Dialog", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "收藏夹"))
        self.label_6.setText(_translate("Dialog", "累计学习时长"))
        self.label_7.setText(_translate("Dialog", "今天学习时长"))
        self.label_8.setText(_translate("Dialog", "本次学习时长"))
        self.label_9.setText(_translate("Dialog", "距离四六级考试还有"))
        self.label_10.setText(_translate("Dialog", "距离考研还有"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "统计"))
import img_rc
