from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3
import fich_patient as fp
import chercher as ch
import medecin as mc


def inscription():
    fp.show()

def chercher():
    ch.show()

def parametre():
    mc.show()


# app=QtWidgets.QApplication([])
# fen=uic.loadUi("menu.ui")
# fen.inscription.clicked.connect(inscription)
# fen.chercher.clicked.connect(chercher)
# fen.parametre.clicked.connect(parametre)


# fen.show()
# app.exec()

def show():
    global fen 
    fen=uic.loadUi("menu.ui")
    fen.inscription.clicked.connect(inscription)
    fen.chercher.clicked.connect(chercher)
    fen.parametre.clicked.connect(parametre)
    fen.show()

fen=None
