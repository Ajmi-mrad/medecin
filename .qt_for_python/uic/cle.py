# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\jdid\nv-medecin\cle.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 610)
        MainWindow.setStyleSheet("#pushButton\n"
"{\n"
"background:red;\n"
"border-radius:60px\n"
"}\n"
"# QWidget{\n"
"# background-image:url(:/newPrefix/bg.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 521, 511))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login = QtWidgets.QPushButton(self.frame)
        self.login.setGeometry(QtCore.QRect(20, 400, 471, 51))
        self.login.setStyleSheet("QPushButton{\n"
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
        self.login.setObjectName("login")
        self.adresse = QtWidgets.QLineEdit(self.frame)
        self.adresse.setGeometry(QtCore.QRect(30, 210, 431, 41))
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
        self.adresse.setObjectName("adresse")
        self.mot_de_passe = QtWidgets.QLineEdit(self.frame)
        self.mot_de_passe.setGeometry(QtCore.QRect(30, 330, 431, 31))
        self.mot_de_passe.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"\n"
"font-family:century gothiw ;\n"
"font-size:24px;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.mot_de_passe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mot_de_passe.setObjectName("mot_de_passe")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 70, 171, 71))
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
        self.label_2.setGeometry(QtCore.QRect(30, 150, 161, 51))
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
        self.label_3.setGeometry(QtCore.QRect(30, 260, 161, 51))
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
        self.nv_compte = QtWidgets.QPushButton(self.frame)
        self.nv_compte.setGeometry(QtCore.QRect(20, 460, 131, 31))
        self.nv_compte.setStyleSheet("QPushButton{\n"
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
        self.nv_compte.setObjectName("nv_compte")
        self.modifier = QtWidgets.QPushButton(self.frame)
        self.modifier.setGeometry(QtCore.QRect(330, 460, 171, 31))
        self.modifier.setStyleSheet("QPushButton{\n"
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
        self.modifier.setObjectName("modifier")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(200, 20, 141, 121))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Connexion"))
        self.login.setText(_translate("MainWindow", "Connexion"))
        self.adresse.setText(_translate("MainWindow", "ajmimrad@gmail.com"))
        self.adresse.setPlaceholderText(_translate("MainWindow", "Adresse"))
        self.mot_de_passe.setText(_translate("MainWindow", "ajmimrad0"))
        self.mot_de_passe.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.label.setText(_translate("MainWindow", "Connexion ICI"))
        self.label_2.setText(_translate("MainWindow", "Adresse :"))
        self.label_3.setText(_translate("MainWindow", "Mot de passe :"))
        self.nv_compte.setText(_translate("MainWindow", "Créer un compte"))
        self.modifier.setText(_translate("MainWindow", "Modifier le mot de passe"))
import user_rc