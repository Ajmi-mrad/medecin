from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3

def valider():
    if not valide():
        QMessageBox.information(fen,"Desole","Entrer les changements")
        return

    nv_categorie = fen.nv_categorie.text()

    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="insert into categorie_maladie (categorie) values (?)"
    cur.execute(sql, (nv_categorie,))
    conn.commit()

    cur.close()
    conn.close()
    effacer()
    
def effacer():
    fen.nv_categorie.setText("")

def valide():
    return fen.nv_categorie.text() != "" 

def fermer():
    fen.hide()

def show():
    global fen 
    fen=uic.loadUi("editer_categorie.ui")
    fen.valider.clicked.connect(valider)
    fen.fermer.clicked.connect(fermer)
    # fen.show()
    fen.exec()

fen=None
