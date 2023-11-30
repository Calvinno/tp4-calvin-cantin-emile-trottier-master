from enum import Enum


class Couleur(Enum):
    BLANC = 0
    NOIR = 1

    def __invert__(self):
        if self.name == "BLANC":
            return Couleur.NOIR
        else:
            return Couleur.BLANC

    @classmethod
    def vers_chaine(cls, couleur):
        if couleur.name == "BLANC":
            return "Blanc"
        else:
            return "Noir"
