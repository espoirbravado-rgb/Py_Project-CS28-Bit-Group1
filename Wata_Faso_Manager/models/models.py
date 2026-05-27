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
        Sécurité Interne : Empêche l'enregistrement d'une consommation négative.

        Arguments:
            valeur_index (int): La nouvelle valeur lue sur le compteur.

        Retour:
            bool: True si la mise à jour est valide, False sinon.
        """
        if valeur_index >= self._ancien_index:
            self._nouvel_index = valeur_index
            return True
        return False

    def calculer_consommation(self):
        """Calcule le volume consommé entre les deux index.

        Retour:
            int: Le volume de consommation net.
        """
        return self._nouvel_index - self._ancien_index

    def cloturer_periode_index(self):
        """Applique la bascule automatique des index pour le mois suivant."""
        self._ancien_index = self._nouvel_index

    def calculer_facture(self):
        """Calcule le montant de la facture (méthode générique).

        EXIGENCE POO : Destinée à être surchargée par les classes filles.

        Retour:
            float: 0.0 pour la classe de base.
        """
        return 0.0


class AbonneSocial(Abonne):
    """Classe représentant un abonné soumis au tarif social domestique."""

    def calculer_facture(self):
        """Calcule la facture sociale basée sur le volume et la dette ancienne.

        DEMONSTRATION DU POLYMORPHISME : Surcharge de la méthode parent.
        EXIGENCE BIT (TUPLE) : Extraction des données depuis un tuple de constante.

        Retour:
            float: Le montant total dû en Francs CFA.
        """
        # Création et exploitation d'un tuple immuable pour sécuriser le calcul
        donnees_calcul_social = (self.calculer_consommation(), config.TARIF_SOCIAL)
        
        volume_consomme = donnees_calcul_social[0]
        prix_unitaire = donnees_calcul_social[1]
        
        montant_mois = volume_consomme * prix_unitaire
        return montant_mois + self._solde_impaye


class AbonneCommercial(Abonne):
    """Classe représentant un abonné soumis au tarif commercial."""

    def calculer_facture(self):
        """Calcule la facture commerciale avec taxe fixe de maintenance.

        DEMONSTRATION DU POLYMORPHISME : Surcharge de la méthode parent.
        EXIGENCE BIT (TUPLE) : Utilisation d'un tuple pour regrouper les paramètres.

        Retour:
            float: Le montant total dû en Francs CFA.
        """
        # Regroupement des constantes de facturation dans un tuple structurel
        parametres_facturation = (config.TARIF_COMMERCIAL, config.TAXE_MAINTENANCE)
        
        tarif_unitaire = parametres_facturation[0]
        taxe_fixe = parametres_facturation[1]
        
        volume_consomme = self.calculer_consommation()
        montant_mois = (volume_consomme * tarif_unitaire) + taxe_fixe
        return montant_mois + self._solde_impaye

#  FIN DU CODE DE MODELS.PY VERROUILLÉ
