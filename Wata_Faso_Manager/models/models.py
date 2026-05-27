# CODE PYTHON DU FICHIER MODELS.PY CONFORME CAHIER DES CHARGES BIT

"""Module de modélisation des profils d'abonnés du réseau WattaFaso-Manager.

Ce module contient la classe de base Abonne ainsi que les classes enfants
AbonneSocial et AbonneCommercial appliquant l'encapsulation et le polymorphisme.
"""

import config


class Abonne:
    """Classe abstraite/générique représentant un abonné du réseau."""

    def __init__(self, code, nom, index_precedent, index_actuel, solde_initial=0):
        """Initialise un nouvel abonné avec ses index et son solde d'impayés.

        Arguments:
            code (str): Le code unique d'identification.
            nom (str): Le nom complet du client.
            index_precedent (int): L'index de consommation du mois passé.
            index_actuel (int): Le nouvel index relevé sur le compteur.
            solde_initial (float): La dette initiale du client (0 par défaut).
        """
        self._code = code
        self._nom = nom
        self._ancien_index = index_precedent
        self._nouvel_index = index_actuel
        self._solde_impaye = solde_initial

    def obtenir_code(self):
        """Retourne le code unique de l'abonné.

        Retour:
            str: Le code d'identification.
        """
        return self._code

    def obtenir_nom(self):
        """Retourne le nom complet de l'abonné.

        Retour:
            str: Le nom du client.
        """
        return self._nom

    def obtenir_ancien_index(self):
        """Retourne l'ancien index de consommation.

        Retour:
            int: L'index précédent.
        """
        return self._ancien_index

    def obtenir_nouvel_index(self):
        """Retourne le nouvel index de consommation.

        Retour:
            int: L'index actuel.
        """
        return self._nouvel_index

    def obtenir_solde(self):
        """Retourne le solde des impayés du client.

        Retour:
            float: Le montant de la dette restante.
        """
        return self._solde_impaye

    def modifier_solde(self, montant):
        """Met à jour le solde des impayés avec un nouveau montant.

        Arguments:
            montant (float): Le nouveau reste à payer.
        """
        self._solde_impaye = montant

    def modifier_nouvel_index(self, valeur_index):
        """Met à jour le nouvel index après vérification de cohérence
