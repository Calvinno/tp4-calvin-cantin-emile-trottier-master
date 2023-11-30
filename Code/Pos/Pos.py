class Pos:
    def __init__(self, ligne_emplacement_ind, colonne=None):
        if isinstance(ligne_emplacement_ind, str):
            self.__ligne = int(ligne_emplacement_ind[1])
            self.__colonne = ord(ligne_emplacement_ind[0]) - 96
        elif isinstance(ligne_emplacement_ind, int) and colonne is not None:
            self.__ligne = ligne_emplacement_ind
            self.__colonne = colonne
        elif isinstance(ligne_emplacement_ind, int):
            self._ligne = (ligne_emplacement_ind - 1) // 8 + 1
            self.__colonne = (ligne_emplacement_ind - 1) % 8 + 1

    @property
    def get_emplacement(self):
        return chr(self.__colonne + 96) + str(self.__ligne)

    # PROTÉGER LES ATTRIBUTS LIGNES ET COLONNES
    @property
    def ligne(self):
        return self.__ligne

    @property
    def colonne(self):
        return self.__colonne

    def __add__(self, addPos):
        resultat_ligne = self.ligne + addPos.ligne
        resultat_colonne = self.colonne + addPos.colonne
        return Pos(resultat_ligne, resultat_colonne)

    def ind(self):
        return int(self.ligne) * 8 + int(self.colonne) + 1

    @staticmethod
    def est_hors_plateau(pos_list):
        liste = []
        for element in [pos_list]:
            liste.append(
                element.ligne not in range(1, 9) or element.colonne not in range(1, 9)
            )
        return liste

    @staticmethod
    def est_dans_liste_pos(pos, listePos):
        return pos in listePos

    def __str__(self):
        return f"Ligne: {self.ligne}, Colonne: {self.colonne}, Emplacement: {self.get_emplacement}"

    def __eq__(self, pos):
        return self.get_emplacement == pos.get_emplacement

    # Fournie
    def __hash__(self):
        return hash((self.ligne, self.colonne))
