import sys
import os


chemin_dossier_1 = os.path.dirname(os.path.realpath(__file__)) + "/../Piece"


if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)

from Piece import *


class CasePlateau:
    def __init__(self, piece=None):
        self.__piece = piece

    # PROTÉGER LES ATTRIBUTS LIGNES ET COLONNES
    @property
    def piece(self):
        return self.__piece

    @piece.setter
    def piece(self, piece):
        self.__piece = piece

    def est_occupe(self):
        return self.piece != None
