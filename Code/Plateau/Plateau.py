import sys
import os

chemin_dossier_1 = os.path.dirname(os.path.realpath(__file__)) + "/../Pos"
chemin_dossier_2 = os.path.dirname(os.path.realpath(__file__)) + "/../CasePlateau"


if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)
if chemin_dossier_2 not in sys.path:
    sys.path.append(chemin_dossier_2)

from Pos import *
from CasePlateau import *


class Plateau:
    NLIGNES = 8
    NCOLONNES = 8

    def __init__(self):
        mat = [[] for i in range(self.NLIGNES)]
        for row in range(self.NLIGNES):
            for col in range(self.NCOLONNES):
                mat[row].append(CasePlateau())
        self.__matCases = mat

    @property
    def matCases(self):
        return self.__matCases

    def ajoute_piece(self, piece, pos):
        self.matCases[pos.ligne - 1][pos.colonne - 1].piece = piece

    def bouge_piece(self, pos_depart, pos_fin):
        piece = self.matCases[pos_depart.ligne - 1][pos_depart.colonne - 1].piece
        if piece != None:
            self.matCases[pos_depart.ligne - 1][pos_depart.colonne - 1].piece = None
            self.matCases[pos_fin.ligne - 1][pos_fin.colonne - 1].piece = piece

    def est_case_occupe(self, pos):
        return self.matCases[pos.ligne - 1][pos.colonne - 1].est_occupe()

    def init_partie(self):
        for row in range(self.NLIGNES):
            for col in range(self.NCOLONNES):
                if row == 0 or row == 7:
                    if col == 0 or col == 7:
                        self.matCases[row][col].piece = Piece(
                            TypePiece(3), Couleur(0 if row == 0 else 1)
                        )
                    elif col == 1 or col == 6:
                        self.matCases[row][col].piece = Piece(
                            TypePiece(5), Couleur(0 if row == 0 else 1)
                        )
                    elif col == 2 or col == 5:
                        self.matCases[row][col].piece = Piece(
                            TypePiece(4), Couleur(0 if row == 0 else 1)
                        )
                    elif col == 3:
                        self.matCases[row][col].piece = Piece(
                            TypePiece(2),
                            Couleur(0 if row == 0 else 1),
                        )
                    elif col == 4:
                        self.matCases[row][col].piece = Piece(
                            TypePiece(1),
                            Couleur(0 if row == 0 else 1),
                        )

                elif row == 1 or row == 6:
                    self.matCases[row][col].piece = Piece(
                        TypePiece(6), Couleur(0 if row == 6 else 1)
                    )

    def liste_piece(self):
        piecesSurPableau = []
        for row in range(self.NLIGNES):
            for col in range(self.NCOLONNES):
                if self.matCases[row][col].est_occupe():
                    piecesSurPableau.append(
                        {
                            "type": self.matCases[row][col].piece.type,
                            "couleur": self.matCases[row][col].piece.couleur,
                            "emplacement": Pos(row + 1, col + 1).get_emplacement(),
                        }
                    )
        return piecesSurPableau

    def piece_a_position(self, pos):
        return self.matCases[pos.ligne - 1][pos.colonne - 1].piece
