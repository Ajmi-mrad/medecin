from fich_patient import Patient
from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import date, datetime
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def fetch_patient(num_patient):
    conn = sqlite3.connect("dt-base.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()

    sql = "SELECT * FROM patient WHERE num_patient = ?"
    cur.execute(sql, (num_patient,))
    patient = cur.fetchone()

    if patient is not None:
        sql = "SELECT num_maladie FROM maladie_patient WHERE num_patient = ?"
        cur.execute(sql, (num_patient,))
        patient['maladies'] = []
        for dct in cur.fetchall():
            patient['maladies'].append(dct['num_maladie'])

    cur.close()
    conn.close()
    return patient

def fetch_consultation(num_patient):
    conn = sqlite3.connect("dt-base.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()

    sql = "SELECT date_de_consultation FROM consultation WHERE num_patient = ? order by date_de_consultation desc "
    cur.execute(sql, (num_patient,))
    date_de_consultations = cur.fetchall()

    cur.close()
    conn.close()

    return date_de_consultations

def remplir(patient ,date_de_consultations):
    fen.nom.setText(patient['nom'])
    fen.prenom.setText(patient['prenom'])
    fen.adresse.setText(patient['adresse'])
    fen.date.date().toString(patient['date_de_naissance'])
    fen.tel.setText(str(patient['telephone']))
    # print(dir(fen.com))
    fen.coment.setHtml(patient['coment'])
    fen.historique.addItem(date_de_consultations['date_de_consultation'])

def remplir_info(np=-1):
    global num_patient

    num_patient = np

    patient = fetch_patient(num_patient)
    date_de_consultations = fetch_consultation(num_patient)
    remplir(patient ,date_de_consultations)

def fermer():
    fen.hide()

def show():
    global fen 
    fen=uic.loadUi("consultation.ui")
    remplir_info()
    fen.fermer.clicked.connect(fermer)
    fen.show()

fen=None
num_patient = None