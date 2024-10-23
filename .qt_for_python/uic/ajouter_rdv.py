# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\dernier version md\ajouter_rdv.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 47, 13))
        self.label_3.setObjectName("label_3")
        self.nom = QtWidgets.QLineEdit(self.centralwidget)
        self.nom.setGeometry(QtCore.QRect(100, 20, 171, 20))
        self.nom.setReadOnly(False)
        self.nom.setObjectName("nom")
        self.telephone = QtWidgets.QLineEdit(self.centralwidget)
        self.telephone.setGeometry(QtCore.QRect(100, 70, 171, 20))
        self.telephone.setObjectName("telephone")
        self.date = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(103, 120, 171, 22))
        self.date.setObjectName("date")
        self.ajouter = QtWidgets.QPushButton(self.centralwidget)
        self.ajouter.setGeometry(QtCore.QRect(40, 180, 75, 23))
        self.ajouter.setObjectName("ajouter")
        self.fermer = QtWidgets.QPushButton(self.centralwidget)
        self.fermer.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.fermer.setObjectName("fermer")
        self.chercher = QtWidgets.QPushButton(self.centralwidget)
        self.chercher.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.chercher.setObjectName("chercher")
        self.disponibilite = QtWidgets.QPushButton(self.centralwidget)
        self.disponibilite.setGeometry(QtCore.QRect(290, 120, 75, 23))
        self.disponibilite.setObjectName("disponibilite")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nom patient :"))
        self.label_2.setText(_translate("MainWindow", "Telepohne :"))
        self.label_3.setText(_translate("MainWindow", "L\'Heur :"))
        self.ajouter.setText(_translate("MainWindow", "Ajouter"))
        self.fermer.setText(_translate("MainWindow", "Fermer"))
        self.chercher.setText(_translate("MainWindow", "Chercher..."))
        self.disponibilite.setText(_translate("MainWindow", "chercher..."))

