from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtCore import QDateTime,Qt,QDate,QTime

import sys
import subprocess
from datetime import datetime
import sqlite3
import chercher as ch
import rendez_vous as rdv

def valider():

    nom = fen.nom.text()
    telephone = fen.telephone.text()
    heur = fen.date.date().toString(Qt.ISODate)

    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="insert into patient (nom , telephone , prenom , adresse , haut , poid , CNAM , date_de_naissance,coment) values (? ,? ,? ,? ,? ,? ,? ,? ,?)"
    cur.execute(sql, (nom,telephone,'','','','','','2000-01-01',''))
    num_patient = cur.lastrowid

    sqll = "insert into rendez_vous (date_rdv, num_patient) values(? ,?)"
    cur.execute(sqll, (heur,num_patient))
    conn.commit()

    cur.close()
    conn.close()

    effacer()
    
def effacer():
    fen.nom.setText("")
    fen.telephone.setText("")

# def valide():
#     return fen.nv_categorie.text() != "" 

# def disponible():
#     global dates
#     date = fen.date.date().toString("yyyy-MM-dd")
#     conn = sqlite3.connect("dt-base.db")
#     cur= conn.cursor()

#     sql="select * from rendez_vous where date like ?"
#     cur.execute(sql, (date,))
#     dates = cur.fetchall()

#     cur.close()
#     conn.close()


#     return dates
    
# def disponibilite ():
#     rvd.show()
#     global dates
#     date = chercher_categorie()

#     fen.categori.clear()
#     for t in categorie : 
#         fen.categori.addItem(t[1])
def chercher():
    ch.show()


def fermer():
    fen.hide()

def show():
    global fen 
    fen=uic.loadUi("ajouter_rdv.ui")
    fen.ajouter.clicked.connect(valider)
    fen.fermer.clicked.connect(fermer)
    fen.chercher.clicked.connect(chercher)
    # fen.disponibilite.clicked.connect(disponibilite)
    fen.show()

fen=None
dates = None