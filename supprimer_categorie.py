from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3

# def dict_factory(cursor, row):
    # d = {}
    # for idx, col in enumerate(cursor.description):
        # d[col[0]] = row[idx]
    # return d

def remplir_categorie():
    global categories
    conn = sqlite3.connect("dt-base.db")
    # conn.row_factory = dict_factory
    cur= conn.cursor()

    sql="select * from categorie_maladie order by categorie"
    cur.execute(sql)
    categories = cur.fetchall()

    cur.close()
    conn.close()

    for t in categories : 
        fen.categorie.addItem(t[1])



def supprimer(num_categorie):
    global categories

    num_categorie = categories[fen.categorie.currentIndex()][0]

    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="delete from categorie_maladie where num_categorie = ? "
    cur.execute(sql, (num_categorie ,))

    conn.commit()

    cur.close()
    conn.close()
    

def fermer():
    fen.hide()

def show():
    global fen 
    fen=uic.loadUi("supprimer_categorie.ui")
    fen.supprimer.clicked.connect(supprimer)
    fen.fermer_3.clicked.connect(fermer)
    remplir_categorie()
    fen.show()

fen = None
categories = None