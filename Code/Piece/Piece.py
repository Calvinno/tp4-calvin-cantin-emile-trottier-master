import sys
import os

chemin_dossier_1 = os.path.dirname(os.path.realpath(__file__)) + "/../Couleur"
chemin_dossier_2 = os.path.dirname(os.path.realpath(__file__)) + "/../TypePiece"

if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)
if chemin_dossier_2 not in sys.path:
    sys.path.append(chemin_dossier_2)

from Couleur import *
from TypePiece import *


class Piece:
    def __init__(self, type_piece, couleur):
        self.__type_piece = type_piece
        self.__couleur = couleur

    # PROTÉGER LES ATTRIBUTS LIGNES ET COLONNES
    @property
    def type(self):
        return self.__type_piece

    @property
    def couleur(self):
        return self.__couleur
