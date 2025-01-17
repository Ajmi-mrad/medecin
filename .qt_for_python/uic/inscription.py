# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\jdid\nv-medecin\inscription.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 70, 521, 511))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.inscription = QtWidgets.QPushButton(self.frame)
        self.inscription.setGeometry(QtCore.QRect(20, 400, 471, 51))
        self.inscription.setStyleSheet("QPushButton{\n"
"color:white;\n"
"border-radius:15px;\n"
"font-family:century gothiw ;\n"
"font-size:24px;}\n"
"\n"
"QPushButton:hover{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:red;\n"
"}")
        self.inscription.setObjectName("inscription")
        self.adresse = QtWidgets.QLineEdit(self.frame)
        self.adresse.setGeometry(QtCore.QRect(20, 180, 431, 41))
        self.adresse.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"\n"
"color:#717072;\n"
"\n"
"font-family:century gothiw ;\n"
"font-size:24px;\n"
"\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.adresse.setText("")
        self.adresse.setObjectName("adresse")
        self.mdp = QtWidgets.QLineEdit(self.frame)
        self.mdp.setGeometry(QtCore.QRect(20, 290, 431, 31))
        self.mdp.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"\n"
"font-family:century gothiw ;\n"
"font-size:24px;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.mdp.setText("")
        self.mdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mdp.setObjectName("mdp")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 70, 121, 71))
        self.label.setStyleSheet("*{\n"
"font-family:century gothiw ;\n"
"font-size:24px;\n"
"}\n"
"\n"
"QLabel {\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 141, 41))
        self.label_2.setStyleSheet("*{\n"
"font-family:century gothiw ;\n"
"font-size:24px;\n"
"}\n"
"\n"
"QLabel {\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 161, 51))
        self.label_3.setStyleSheet("*{\n"
"font-family:century gothiw ;\n"
"font-size:24px;\n"
"}\n"
"\n"
"QLabel {\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.effacer = QtWidgets.QPushButton(self.frame)
        self.effacer.setGeometry(QtCore.QRect(20, 460, 111, 31))
        self.effacer.setStyleSheet("QPushButton{\n"
"color:white;\n"
"border-radius:15px;\n"
"font-family:century gothiw ;\n"
"font-size:12px;}\n"
"\n"
"QPushButton:hover{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:red;\n"
"}")
        self.effacer.setObjectName("effacer")
        self.rmdp = QtWidgets.QLineEdit(self.frame)
        self.rmdp.setGeometry(QtCore.QRect(20, 360, 431, 31))
        self.rmdp.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"\n"
"font-family:century gothiw ;\n"
"font-size:24px;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.rmdp.setText("")
        self.rmdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rmdp.setObjectName("rmdp")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(180, 250, 321, 21))
        self.label_4.setStyleSheet("*{\n"
"font-family:century gothiw ;\n"
"font-size:12px;\n"
"}\n"
"\n"
"QLabel {\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(210, 10, 141, 121))
        self.toolButton.setStyleSheet("#toolButton\n"
"\n"
"{\n"
"background:red;\n"
"border-radius:60px;\n"
"}")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/HP/Pictures/Camera Roll/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 60))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inscription"))
        self.inscription.setText(_translate("MainWindow", "Inscri"))
        self.adresse.setPlaceholderText(_translate("MainWindow", "xyz...@gmail.com"))
        self.mdp.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.label.setText(_translate("MainWindow", "Inscription"))
        self.label_2.setText(_translate("MainWindow", "Adresse :"))
        self.label_3.setText(_translate("MainWindow", "Mot de passe :"))
        self.effacer.setText(_translate("MainWindow", "Tout Effacer"))
        self.rmdp.setPlaceholderText(_translate("MainWindow", "Retapez le mot de passe"))
        self.label_4.setText(_translate("MainWindow", "Le mot de passe doit composer de 8 charcteres minimum "))
