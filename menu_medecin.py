from PyQt5 import QtWidgets, uic,QtPrintSupport, QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
import sys
import subprocess
from datetime import datetime
import sqlite3
import fich_patient as fp
import chercher as ch
import medecin as mc
import editer_maladie as em
import editer_categorie as ec
import supprimer_patient as sp
import supprimer_categorie as sc
import supprimer_maladie as sm
import rendez_vous as rv

def ajouter_patient():
    fp.show()

def modifier_patient():
    ch.show()

def supprimer_patient():
    sp.show()

def show_maladaies_chroniques():
    mc.show()

def editer_categorie():
    ec.show()

def editer_maladie():
    em.show()

def supprimer_categorie():
    sc.show()

def supprimer_maladie():
    sm.show()

def rendez_vous():
    rv.show()

def show():
    global fen 
    fen=uic.loadUi("menu_medecin.ui")
    fen.actionAjouter.triggered.connect(ajouter_patient)
    fen.actionModifier.triggered.connect(modifier_patient)
    fen.actionSupprimer.triggered.connect(supprimer_patient)
    fen.actionAjouter_2.triggered.connect(editer_categorie)
    fen.actionAjouter_3.triggered.connect(editer_maladie)
    fen.actionAffichage.triggered.connect(show_maladaies_chroniques)
    fen.actionSupprimer_2.triggered.connect(supprimer_categorie)
    fen.actionSupprimer_3.triggered.connect(supprimer_maladie)
    fen.actionGestion_rdv.triggered.connect(rendez_vous)
    fen.show()

fen=None
