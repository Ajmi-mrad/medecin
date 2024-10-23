from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3

def remplir_categorie():
    global categories
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="select * from categorie_maladie order by categorie"
    cur.execute(sql)
    categories = cur.fetchall()

    cur.close()
    conn.close()

    for t in categories : 
        fen.categorie.addItem(t[1])


def chercher_maladie(num_categorie):
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="select * from maladies_chroniques where num_categorie = ? order by maladie"
    cur.execute(sql,(num_categorie,))
    maladie = cur.fetchall()

    cur.close()
    conn.close()
    return maladie

def remplir_maladie(nmr_categorie):
    global maladie
    maladie = chercher_maladie(nmr_categorie)

    fen.maladie.clear()
    for t in maladie : 
        fen.maladie.addItem(t[2])

def categorie(index):
    remplir_maladie(categories[index][0])
    
def supprimer(num_maladie):
    global maladie

    num_maladie = maladie[fen.maladie.currentIndex()][0]

    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="delete from maladies_chroniques where num_maladie = ? "
    cur.execute(sql, (num_maladie,))
    conn.commit()

    QMessageBox.information(fen , "Supprition " , "C'est bon la maladie est supprimer")

    cur.close()
    conn.close()
    
def fermer():
    fen.hide()

def show():
    global fen 
    fen=uic.loadUi("supprimer_maladie.ui")
    fen.supprimer.clicked.connect(supprimer)
    fen.fermer_3.clicked.connect(fermer)
    remplir_categorie()
    fen.categorie.activated.connect(categorie)
    fen.show()

fen = None
categories = None
maladie = []
