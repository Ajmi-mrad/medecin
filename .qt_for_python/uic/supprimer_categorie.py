# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\jdid\nv-medecin\supprimer_categorie.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 181)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 20))
        self.label.setObjectName("label")
        self.categorie = QtWidgets.QComboBox(self.centralwidget)
        self.categorie.setGeometry(QtCore.QRect(100, 20, 291, 20))
        self.categorie.setObjectName("categorie")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 100, 296, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.supprimer = QtWidgets.QPushButton(self.layoutWidget)
        self.supprimer.setObjectName("supprimer")
        self.horizontalLayout_3.addWidget(self.supprimer)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.fermer_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.fermer_3.setObjectName("fermer_3")
        self.horizontalLayout_3.addWidget(self.fermer_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Supprimer categorie"))
        self.label.setText(_translate("MainWindow", "Categorie"))
        self.supprimer.setText(_translate("MainWindow", "Supprimer"))
        self.fermer_3.setText(_translate("MainWindow", "Fermer"))
