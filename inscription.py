from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3


def inscription():
    adresse = fen.adresse.text()
    mot_de_passe = fen.mdp.text()
    r_mot_de_passe = fen.rmdp.text()

    if "@gmail.com" not in adresse :
        QMessageBox.information(fen,"Erreur" , "L'adresse doit sous la forme de xyz...@gmail.com")

    if mot_de_passe != r_mot_de_passe :
        QMessageBox.information(fen,"Erreur" , "L'un de les mots de passe est faut !!")
    
    if len(mot_de_passe) < 8:
        QMessageBox.information(fen,"Erreur" , "le mot de passe doit composer de 8 charctere au min !!")
    
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="insert into login (adresse , mot_de_passe) values (? , ?)"
    cur.execute(sql, (adresse , mot_de_passe))
    conn.commit()

    cur.close()
    conn.close()

    fen.hide()
    
def effacer():
    fen.adresse.seTtext("")
    fen.mdp.seTtext("")
    fen.rmdp.seTtext("")

# def valide():
#     return fen.adresse.text() != "" 

def show():
    global fen 
    fen=uic.loadUi("inscription.ui")
    fen.inscription.clicked.connect(inscription)
    fen.effacer.clicked.connect(effacer)
    
    fen.show()

fen=None
