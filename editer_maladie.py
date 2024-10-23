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
    
def valider():
    global categories
    if not valide():
        QMessageBox.information(fen, "Desole", "Entrer les informations")
        return


    num_categorie = categories[fen.categorie.currentIndex()][0]
    nv_maladie = fen.nv_maladie.text()

    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="insert into maladies_chroniques (maladie , num_categorie) values (?,?)"
    cur.execute(sql, (nv_maladie,num_categorie))
    conn.commit()

    cur.close()
    conn.close()
    effacer()


def effacer():
    fen.nv_maladie.setText("")

def valide():
    return fen.nv_maladie.text() != "" 

def fermer():
    fen.hide()
def show():
    global fen 
    fen=uic.loadUi("editer_maladie.ui")
    fen.valider.clicked.connect(valider)
    fen.fermer.clicked.connect(fermer)
    remplir_categorie()
    fen.categorie.activated.connect(categorie)
    fen.show()

fen = None
categories = None
maladie = []