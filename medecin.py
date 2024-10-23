from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3
import editer_maladie as em
import editer_categorie as ec

def chercher_categorie():
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="select * from categorie_maladie order by categorie"
    cur.execute(sql)
    categorie = cur.fetchall()

    cur.close()
    conn.close()
    return categorie

def chercher_maladie(num_categorie):
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="select * from maladies_chroniques where num_categorie = ? order by maladie"
    cur.execute(sql,(num_categorie,))
    maladie = cur.fetchall()

    cur.close()
    conn.close()
    return maladie

def remplir_categorie():
    global categorie
    categorie = chercher_categorie()

    fen.categori.clear()
    for t in categorie : 
        fen.categori.addItem(t[1])
    if len(categorie) > 0 :
        remplir_maladie(categorie[0][0])

def remplir_maladie(nmr_categorie):
    global maladie
    maladie = chercher_maladie(nmr_categorie)

    fen.maladie.clear()
    for t in maladie : 
        fen.maladie.addItem(t[2])

def ajouter_maladie():
    em.show()

def ajouter_categorie():
    ec.show()

def fermer():
    fen.hide()

def categorie_changed():
    global categorie
    nmr_categorie = categorie[fen.categori.currentRow()][0]
    remplir_maladie(nmr_categorie)

def init():
    remplir_categorie()

def show():
    global fen 
    fen=uic.loadUi("maladie_chronique.ui")
    fen.ajouter_categorie.clicked.connect(ajouter_categorie)
    fen.ajouter_maladie.clicked.connect(ajouter_maladie)
    fen.fermer.clicked.connect(fermer)
    fen.categori.itemSelectionChanged.connect(categorie_changed)
    init()
    fen.show()
    
categorie = []
maladie = []
fen = None