from PyQt5 import QtWidgets, uic, QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox, QCheckBox, QGroupBox, QGridLayout, QVBoxLayout
import sys
import subprocess
from datetime import datetime
import sqlite3
# import medecin as mc


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Patient:
    def __init__(self,nom, date_de_naissance, adresse, prenom, telephone, commentaire, poid, hauteur, CNAM, mal_chek):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.adresse = adresse
        self.telephone = telephone
        self.poid = poid
        self.hauteur = hauteur
        self.commentaire = commentaire
        self.mal_chek = mal_chek
        self.CNAM = CNAM


def numerique(ch):
    for i in range (len(ch)):
        if not ('1' <= ch[i] <= '9' or ch[i] == ' '):
            return False
    return True

def alphabetique(ch):
    for i in range (len(ch)):
        if ch[i].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ,' ']:
            return False
    return True

def enregistrer():
    global num_patient
    if not valide():
        QMessageBox.information(fen, "desole", "Entrer les informations")
        return

    while True:
        nom = fen.nom.text()
        if alphabetique(nom) == True:
            break
        else:
            QMessageBox.information(fen, "Erreur!!", "Le nom doit composer de l'alphabet")
            return

    while True:
        prenom = fen.prenom.text()
        if alphabetique(prenom) == True :
            break
        else:
            QMessageBox.information(fen, "Erreur!!", "Le prenom doit composer de l'alphabet")
            return
    # conn = sqlite3.connect("dt-base.db")
    # cur= conn.cursor()
    # sql = "select count(*) from  patient where nom = ? "
    # cur.execute(sql,(nom,))
    # nb_repetition = cur.fetchone()
    # if nb_repetition[0] > 1 :
    #     msg=f'Ce nom {nom} est deja exsist donner le nom de ton pere  '
    #     QMessageBox.information(fen ,"Inscription" , msg)
    #     return

    # cur.close()
    # conn.close()

    adresse = fen.adresse.text()
    while True:
        telephone = fen.tel.text()
        if numerique(telephone) == True:
            break
        else:
            QMessageBox.information(fen, "Erreur !!", "le numéro de telephone doit composer de numero ")
            return

    date_de_naissance = fen.date.date().toString("yyyy-MM-dd")
    poid = fen.poid.text()
    hauteur = fen.haut.text()
    while True:
        CNAM = fen.cnam.text()
        if len(CNAM) == 10 and CNAM.isdigit():
            break
        else:
            QMessageBox.information(fen, "Erreur !!", "le CNAM doit composer de dix numero ")
            return

    commentaire = fen.commentaire.toPlainText()
    mal_chek = maladies_checked()

    pat = Patient(nom, date_de_naissance, adresse, prenom, telephone, commentaire, poid, hauteur, CNAM, mal_chek)

    if mode == 'Insertion':
        num_patient = insert_patient(pat.nom, pat.date_de_naissance, pat.adresse,
         pat.prenom, pat.telephone, pat.commentaire, pat.poid, pat.hauteur, pat.CNAM, pat.mal_chek)
    else:
        update_patient(num_patient, pat.nom, pat.date_de_naissance, pat.adresse,
         pat.prenom, pat.telephone, pat.commentaire, pat.poid, pat.hauteur, pat.CNAM, pat.mal_chek)
    effacer()


def effacer():
    fen.nom.setText("")
    fen.prenom.setText("")
    fen.adresse.setText("")
    fen.date.date().toString("yyyy-MM-dd")
    fen.tel.setText("")
    # print(dir(fen.com))
    fen.commentaire.setPlainText("")
    fen.poid.setText("")
    fen.haut.setText("")
    fen.cnam.setText("")


def valide():
    return fen.nom.text() != "" and fen.prenom.text() != ""


# def suivant():
#     mc.show()


def fermer():
    fen.hide()


def show(np=-1):
    global fen, layout, mode, num_patient

    num_patient = np

    fen = uic.loadUi("fich_patient.ui")
    fen.enregistrer.clicked.connect(enregistrer)
    fen.fermer.clicked.connect(fermer)
    # fen.suivant.clicked.connect(suivant)
    fen.show()

    if num_patient == -1:
        mode = "Insertion"
    else:
        mode  = "Edition"

    patient = fetch_patient(num_patient)
    if patient is None:
        patient = {
            'nom': '',
            'date_de_naissance': '2000-01-01', 
            'adresse': '', 
            'prenom': '', 
            'telephone': '', 
            'num_patient': '', 
            'coment': "", 
            'poid': '', 
            'haut': '', 
            'CNAM': '', 
            'maladies': []
        }

    # layout = QGridLayout()
    layout = fen.mal_chron.layout()
    remplir_form_maladies()

    remplir(patient)

def remplir_form_maladies():
    global tchk
    maladies = fetch_maladies_chroniques()

    mal_dict = {}
    for maladie in maladies:
        if maladie['categorie'] not in mal_dict:
            mal_dict[maladie['categorie']] = []
        mal_dict[maladie['categorie']].append(maladie)

    l, c = 0, 0
    tchk = []
    for key in mal_dict.keys():
        ajout_group_box(l, c, key, mal_dict[key])
        c += 1
        if c >= 3:
            l, c = l+1, 0

def ajout_group_box(row, col, categorie, maladies):
    global layout, tgrp, tchk

    grp = QGroupBox(categorie, fen.mal_chron)
    grp.setCheckable(True)
    tgrp.append((maladies[0]['num_categorie'], grp))

    layout.addWidget(grp, row, col)

    vbox = QVBoxLayout()
    grp.setLayout(vbox)

    for maladie in maladies:
        chk = QCheckBox(maladie['maladie'])
        tchk.append((maladie["num_maladie"], chk))
        vbox.addWidget(chk)


def maladies_checked():
    mal_chek = []
    for num_maladie, chk in tchk:
        if chk.isChecked():
            mal_chek.append(num_maladie)
    return mal_chek


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

def fetch_maladies_chroniques():
    conn = sqlite3.connect("dt-base.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()

    sql = """SELECT * 
FROM categorie_maladie AS cm 
  INNER JOIN maladies_chroniques AS mc ON cm.num_categorie = mc.num_categorie
ORDER BY categorie, maladie"""
    cur.execute(sql)
    maladies = cur.fetchall()
    cur.close()
    conn.close()
    return maladies


def insert_patient(nom, date_de_naissance, adresse, prenom, telephone, commentaire, poid, hauteur, CNAM, mal_chek):
    conn = sqlite3.connect("dt-base.db")
    cur = conn.cursor()

    sql = "insert into patient(nom,date_de_naissance,adresse,prenom,telephone,coment,poid,haut,CNAM) values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(sql, (nom, date_de_naissance, adresse, prenom,
                telephone, commentaire, poid, hauteur, CNAM))
    num_patient = cur.lastrowid

    for num_maladie in mal_chek:
        sql = 'insert into maladie_patient (num_patient , num_maladie)values(?,?)'
        cur.execute(sql, (num_patient, num_maladie))
    conn.commit()

    cur.close()
    conn.close()

    return num_patient

def update_patient(num_patient, nom, date_de_naissance, adresse, prenom, telephone, commentaire, poid, hauteur, CNAM, mal_chek):
    conn = sqlite3.connect("dt-base.db")
    cur= conn.cursor()

    sql="update patient set nom = ?, date_de_naissance = ?, adresse = ?, prenom = ?, telephone = ?, coment = ?, poid = ?, haut = ?, CNAM = ? where num_patient = ? "
    cur.execute(sql, (nom, date_de_naissance, adresse, prenom, telephone, commentaire, poid, hauteur, CNAM, num_patient))

    sql = "delete from maladie_patient where num_patient = ? "
    cur.execute(sql,(num_patient,))
    for num_maladie in mal_chek:
        sql = 'insert into maladie_patient (num_patient , num_maladie)values(?,?)'
        cur.execute(sql, (num_patient, num_maladie))
    conn.commit()

    cur.close()
    conn.close()

def remplir(patient):
    fen.nom.setText(patient['nom'])
    fen.prenom.setText(patient['prenom'])
    fen.adresse.setText(patient['adresse'])
    fen.date.date().toString(patient['date_de_naissance'])
    fen.tel.setText(str(patient['telephone']))
    # print(dir(fen.com))
    fen.commentaire.setPlainText(patient['coment'])
    fen.poid.setText(str(patient['poid']))
    fen.haut.setText(str(patient['haut']))
    fen.cnam.setText(str(patient['CNAM']))
    # print(patient['maladies'])

    for num_maladie , chk in  tchk:
        chk.setChecked(num_maladie in patient["maladies"])


fen = None
layout = None
mode = 'Insertion'
tgrp, tchk = [], []
num_patient = -1
