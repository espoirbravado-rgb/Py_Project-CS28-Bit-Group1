# CODE PYTHON DU FICHIER DATABASE.PY SÉCURISÉ ET BLINDÉ

"""Module de gestion de la persistance des données pour WattaFaso-Manager.

Ce module gère la lecture et l'écriture du registre avec une validation 
stricte du nombre de colonnes pour empêcher les crashs de type IndexError.
"""

import config
import models


def charger_base_de_donnees():
    """Charge le registre des abonnés depuis le fichier de stockage textuel.

    Sécurité interne : Valide explicitement la structure en 6 colonnes de chaque
    ligne avant d'accéder aux données, évitant les crashs sur fichier altéré.

    Retour:
        dict: Le dictionnaire des objets abonnés indexés par leur code unique.
    """
    dictionnaire_clients = {}
    
    try:
        with open(config.CHEMIN_STOCK, "r", encoding="utf-8") as fichier:
            for numero_ligne, ligne in enumerate(fichier, 1):
                ligne_nettoyee = ligne.strip()
                if not ligne_nettoyee:
                    continue
                    
                segments = ligne_nettoyee.split(";")
                
                # CORRECTION CRITIQUE C : Validation explicite de la structure
                if len(segments) != 6:
                    print(
                        "Erreur Ligne " + str(numero_ligne) 
                        + " : Structure invalide (" + str(len(segments)) 
                        + "/6 colonnes). Ligne ignorée."
                    )
                    continue
                    
                try:
                    type_client = segments[0]
                    identifiant = segments[1]
                    nom_client = segments[2]
                    ancien = int(segments[3])
                    nouveau = int(segments[4])
                    solde = float(segments[5])
                    
                    if type_client == "SOCIAL":
                        client_objet = models.AbonneSocial(
                            identifiant, nom_client, ancien, nouveau, solde
                        )
                        dictionnaire_clients[identifiant] = client_objet
                    elif type_client == "COMMERCIAL":
                        client_objet = models.AbonneCommercial(
                            identifiant, nom_client, ancien, nouveau, solde
                        )
                        dictionnaire_clients[identifiant] = client_objet
                    else:
                        print(
                            "Avertissement Ligne " + str(numero_ligne) 
                            + " : Type d'abonné inconnu '" + str(type_client) + "'."
                        )
                        
