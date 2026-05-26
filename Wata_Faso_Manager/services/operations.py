#  CODE PYTHON DU FICHIER OPERATIONS.PY SÉCURISÉ ET STABILISÉ

"""Module des opérations de guichet et de terrain pour WattaFaso-Manager.

Ce module gère les procédures d'auto-inscription avec identifiants uniques 
dynamiques et l'enregistrement sécurisé des sessions de relevés d'index.
"""

from datetime import datetime
import models


def inscrire_nouvel_abonne(dictionnaire_clients):
    """Inscrit un nouvel abonné avec un identifiant unique garanti sans doublon.

    Sécurité interne : Détermine l'année actuelle dynamiquement et calcule le 
    numéro séquentiel basé sur le plus grand identifiant existant pour éviter 
    toute collision de clés en cas de suppressions antérieures.

    Arguments:
        dictionnaire_clients (dict): Le registre des abonnés en mémoire vive.
    """
    print("\n--- ATTRIBUTION AUTOMATIQUE D'UN ABONNEMENT ---")
    nom_saisi = input("Entrez le nom complet du nouveau client : ").strip()
    
    if not nom_saisi:
        print("Erreur : Le nom ne peut pas être vide. Annulation.")
        return

    print("Choisissez le profil tarifaire :")
    print("1. Profil Social (Ménages)")
    print("2. Profil Commercial (Boutiques/Ateliers)")
    choix = input("Votre choix (1 ou 2) : ").strip()
    
    if choix == "1":
        prefixe = "SOC"
    elif choix == "2":
        prefixe = "COM"
    else:
        print("Erreur : Choix invalide. Annulation de la procédure.")
        return
        
    # Amélioration D : Extraction dynamique de l'année en cours
    annee_actuelle = str(datetime.now().year)
    
