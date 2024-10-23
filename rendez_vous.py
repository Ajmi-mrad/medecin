from fich_patient import Patient
from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidgetItem
import sys
import subprocess
from datetime import date, datetime
import sqlite3

import consultation as c
import ajouter_rdv as ar
import chercher as ch       

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def trouver(ch):
    conn = sqlite3.connect("dt-base.db")
    conn.row_factory = dict_factory
    cur= conn.cursor()
    sql = """SELECT telephone, nom 
FROM patient INNER JOIN rendez_vous ON patient.num_patient = rendez_vous.num_patient
  WHERE rendez_vous.date_rdv like ?  """

    sqll = " select * from rendez_vous "
    ch1 = "%"+ch+"%"
    cur.execute(sql,(ch,))
    rdvs = cur.fetchall()
    print(rdvs)

    cur.execute(sqll)
    infos = cur.fetchall()
    print(infos)
    cur.close()
    conn.close()
    return rdvs

def chercher():
    global rdvs
    ch = fen.date.date().toString("yyyy-MM-dd")
    rdvs = trouver(ch)
    remplir_tab(rdvs)

def remplir_tab(rdvs):
    fen.rdv.setRowCount(len(rdvs))
    lig = 0
    for rdv in rdvs:
        print(rdv)
        add_line(lig, rdv)    
        lig+=1

def add_line(lig, rdv):
    champs = ["nom","telephone","date_rdv"]
    for i in range(len(champs)):
        titem = QTableWidgetItem(str(rdv[champs[i]]))
        titem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        fen.rdv.setItem(lig, i, titem)

def edit(row, col):
    edit_show(rdvs[row]["num_patient"])
  
def consulter():
    row = fen.rdv.currentRow()
    if row == -1 :
        QMessageBox.information(fen , "desolé", "Il faut sélectionner un item !!")
    else:    
        edit_show(rdvs[row]["num_patient"])

def edit_show(num_patient):
    c.show(num_patient)  

def ajouter():
    ar.show()

def sup():
    pass



def show():
    global fen 
    fen=uic.loadUi("rendez_vous.ui")

    fen.rdv.cellDoubleClicked.connect(edit)
    fen.consultation.clicked.connect(consulter)
    fen.ajouter.clicked.connect(ajouter)
    fen.supprimer.clicked.connect(sup)
    fen.chercher.clicked.connect(chercher)
    fen.show()

fen=None
num_patient = None
rdvs = None