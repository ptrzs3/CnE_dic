# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findpasswd.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fpasswd(object):
    def setupUi(self, fpasswd):
        fpasswd.setObjectName("fpasswd")
        fpasswd.resize(230, 405)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pictures/img/fl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fpasswd.setWindowIcon(icon)
        fpasswd.setStyleSheet("")
        self.label = QtWidgets.QLabel(fpasswd)
        self.label.setGeometry(QtCore.QRect(0, 0, 230, 405))
        self.label.setStyleSheet("image: url(:/pictures/img/resetpswd.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(fpasswd)
        self.comboBox.setGeometry(QtCore.QRect(20, 120, 190, 30))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(fpasswd)
        self.lineEdit.setGeometry(QtCore.QRect(20, 160, 190, 30))
        self.lineEdit.setStyleSheet("background:transparent")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(fpasswd)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 200, 190, 30))
        self.lineEdit_2.setStyleSheet("background:transparent")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(fpasswd)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 240, 190, 30))
        self.lineEdit_3.setStyleSheet("background:transparent")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(fpasswd)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 280, 190, 30))
        self.lineEdit_4.setStyleSheet("background:transparent")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(fpasswd)
        self.label_2.setGeometry(QtCore.QRect(85, 40, 60, 60))
        self.label_2.setStyleSheet("background:transparent;\n"
"image: url(:/pictures/img/fl.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(fpasswd)
        self.pushButton.setGeometry(QtCore.QRect(30, 330, 170, 30))
        self.pushButton.setStyleSheet("boeder-radius:5px;\n"
"background-color: rgb(50, 134, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(fpasswd)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 0, 31, 31))
        self.pushButton_2.setStyleSheet("background:transparent")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pictures/img/关  闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(fpasswd)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 0, 31, 31))
        self.pushButton_3.setStyleSheet("background:transparent")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pictures/img/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(fpasswd)
        self.pushButton_3.clicked.connect(fpasswd.showMinimized)
        self.pushButton_2.clicked.connect(fpasswd.close)
        QtCore.QMetaObject.connectSlotsByName(fpasswd)

    def retranslateUi(self, fpasswd):
        _translate = QtCore.QCoreApplication.translate
        fpasswd.setWindowTitle(_translate("fpasswd", "找回密码"))
        self.comboBox.setPlaceholderText(_translate("fpasswd", "请选择用户"))
        self.lineEdit.setPlaceholderText(_translate("fpasswd", "密保问题"))
        self.lineEdit_2.setPlaceholderText(_translate("fpasswd", "问题答案"))
        self.lineEdit_3.setPlaceholderText(_translate("fpasswd", "新密码"))
        self.lineEdit_4.setPlaceholderText(_translate("fpasswd", "确认密码"))
        self.pushButton.setText(_translate("fpasswd", "修改密码"))
import img_rc