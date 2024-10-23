from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3


import menu_medecin
import inscription 
import modif_mdp



# from cle import cnx 

# def connextion_base():
# from mysql.connector import (connection)

# cnx = connection.MySQLConnection(user='scott', password='password',
#                                  host='127.0.0.1',
#                                  database='employees')
# cnx.close()
# return cnx 
# %s = ?

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def login():
    global informations
    username = fen.adresse.text()
    password = fen.mot_de_passe.text()

    
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
        if  username == info['adresse']  and  password == info['mot_de_passe'] :
            menu_medecin.show()
            fen.hide()
        else :
            QMessageBox.information(fen , "Erreur" , "Input the correct Information Please !!!")

def compter_table():
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()
    
    sql="select count (*) from login"
    cur.execute(sql)
    nbr=cur.fetchone()

    cur.close()
    conn.close()

    return nbr


def creer_nv_compte():
    nbr_compte = compter_table
    if nbr_compte == 0 :
        inscription.show()
        fen.hide()
    else :
        QMessageBox.information(fen , "Desole" , "Desole pour la protection il faut existe un seul compte ☺")

def modifier_compte():
    nbr_compte = compter_table
    if nbr_compte == 0 :
        QMessageBox.information(fen , "Erreur" , "Il n'y a pas de compte pour modifier")
    
    else :
        fen.hide()
        modif_mdp.show()
        

app=QtWidgets.QApplication([])
fen=uic.loadUi("cle.ui")

fen.login.clicked.connect(login)
fen.nv_compte.clicked.connect(creer_nv_compte)
fen.modifier.clicked.connect(modifier_compte)

informations = None

fen.show()
app.exec()