from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def modifier():
    global informations

    mot_de_passe = fen.mdp.text()
    nv_mot_de_passe = fen.nv_mdp.text()
    r_mot_de_passe = fen.rmdp.text()

    conn = sqlite3.connect("dt-base.db")
    conn.row_factory = dict_factory
    cur= conn.cursor()

    sql="select * from login order by adresse"
    cur.execute(sql)
    informations = cur.fetchall()

    
    cur.close()
    conn.close()

    for info in informations:     
        # print(info['mot_de_passe']) 
        if  mot_de_passe != info['mot_de_passe']  :
            QMessageBox.information(fen , "Erreur" , "Le mot de passe est faut !!!")
            return 
            
    if nv_mot_de_passe != r_mot_de_passe :
        QMessageBox.information(fen,"Erreur" , "L'un de les mots de passe est faut !!")
        return

    if len(nv_mot_de_passe) < 8:
        QMessageBox.information(fen,"Erreur" , "le mot de passe doit composer de 8 charctere au min !!")
        return

    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="update login set mot_de_passe = ? where id_login = ?"
    for info in informations :
        cur.execute(sql, (nv_mot_de_passe, info['id_login']))
        conn.commit()

    cur.close()
    conn.close()

    fen.hide()
    
def effacer():
    fen.nv_mdp.seTtext("")
    fen.mdp.seTtext("")
    fen.rmdp.seTtext("")

# def valide():
#     return fen.adresse.text() != "" 

def show():
    global fen 
    fen=uic.loadUi("modif_mdp.ui")
    fen.modifier.clicked.connect(modifier)
    fen.effacer.clicked.connect(effacer)
    
    fen.show()

fen=None
informations = None