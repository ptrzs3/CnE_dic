# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeuser.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cguser(object):
    def setupUi(self, cguser):
        cguser.setObjectName("cguser")
        cguser.resize(285, 172)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pictures/img/fl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cguser.setWindowIcon(icon)
        cguser.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(cguser)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(cguser)
        self.lineEdit.setGeometry(QtCore.QRect(60, 90, 161, 20))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(cguser)
        self.pushButton_2.setGeometry(QtCore.QRect(253, 0, 31, 31))
        self.pushButton_2.setStyleSheet("background:transparent")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pictures/img/关  闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(cguser)
        self.pushButton_3.setGeometry(QtCore.QRect(223, 0, 31, 31))
        self.pushButton_3.setStyleSheet("background:transparent")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pictures/img/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(cguser)
        self.label.setGeometry(QtCore.QRect(110, 20, 51, 51))
        self.label.setStyleSheet("background:transparent;image: url(:/pictures/img/fl.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(cguser)
        self.pushButton_2.clicked.connect(cguser.close)
        self.pushButton_3.clicked.connect(cguser.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(cguser)

    def retranslateUi(self, cguser):
        _translate = QtCore.QCoreApplication.translate
        cguser.setWindowTitle(_translate("cguser", "切换用户"))
        self.pushButton.setText(_translate("cguser", "切换用户"))
        self.lineEdit.setPlaceholderText(_translate("cguser", "输入密码"))
import img_rc
