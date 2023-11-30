from enum import Enum


class TypePiece(Enum):
    ROI = 1
    DAME = 2
    TOUR = 3
    FOU = 4
    CAVALIER = 5
    PION = 6

    def vers_chaine(self):
        match self.name:
            case "ROI":
                return "Roi"
            case "DAME":
                return "Dame"
            case "TOUR":
                return "Tour"
            case "FOU":
                return "Fou"
            case "CAVALIER":
                return "Cavalier"
            case "PION":
                return "Pion"
