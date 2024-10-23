from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidgetItem
import sys
import subprocess
from datetime import datetime
import sqlite3
import fich_patient as fp

def verif_date(date):
    formats = ["%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y"]
    for format in formats:
        try:
            date = datetime.strptime(date, format)
            # print(date)
            return date.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return date
        


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def trouver(ch):
    conn = sqlite3.connect("dt-base.db")
    conn.row_factory = dict_factory
    cur= conn.cursor()
    sql = "select * from patient where date_de_naissance like ? or nom like ? or prenom like ? or CNAM like ? "
    ch1 = "%"+ch+"%"
    cur.execute(sql,(verif_date(ch), ch1 , ch1 , ch1 ))
    pats = cur.fetchall()
    cur.close()
    conn.close()
    return pats

def chercher():
    global pats
    ch = fen.chercher.text()
    pats = trouver(ch)
    remplir_tab(pats)

def remplir_tab(pats):
    fen.patient.setRowCount(len(pats))
    lig = 0
    for pat in pats:
        add_line(lig, pat)    
        lig+=1

def add_line(lig, pat):
    champs = ["nom","prenom","date_de_naissance","telephone","adresse","poid","haut","CNAM"]
    for i in range(len(champs)):
        titem = QTableWidgetItem(str(pat[champs[i]]))
        titem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        fen.patient.setItem(lig, i, titem)
    
        

def sup(num_patient):
    global pats
    
    num_patient = pats[fen.patient.currentRow()]['num_patient']
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="delete from patient where num_patient = ? "
    cur.execute(sql, (num_patient,))

    conn.commit()

    cur.close()
    conn.close()

def fermer():
    fen.hide()

def show():
    global fen 
    fen=uic.loadUi("supprimer_patient.ui")
    fen.supprimer.clicked.connect(sup)
    fen.fermer.clicked.connect(fermer)
    fen.prouver.clicked.connect(chercher)
    fen.chercher.returnPressed.connect(chercher)
    fen.show()

fen=None
pats = None