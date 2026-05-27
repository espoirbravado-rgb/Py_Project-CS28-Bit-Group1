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
    
    # Amélioration C : Algorithme de recherche du numéro maximum pour éviter les doublons
    max_numero = 0
    for cle in dictionnaire_clients:
        # Un code valide ressemble à "SOC-2026-003"
        segments = cle.split("-")
        if len(segments) == 3 and segments[0] == prefixe and segments[1] == annee_actuelle:
            try:
                numero_extrait = int(segments[2])
                if numero_extrait > max_numero:
                    max_numero = numero_extrait
            except ValueError:
                continue
                
    numero_sequentiel = max_numero + 1
    code_unique = prefixe + "-" + annee_actuelle + "-" + str(numero_sequentiel).zfill(3)
    
    # Création de l'objet avec des index et un solde initialisés à zéro
    if prefixe == "SOC":
        nouveau_client = models.AbonneSocial(code_unique, nom_saisi, 0, 0, 0)
    else:
        nouveau_client = models.AbonneCommercial(code_unique, nom_saisi, 0, 0, 0)
        
    dictionnaire_clients[code_unique] = nouveau_client
    print("Succès : Enregistrement effectué par le système.")
    print("Code unique généré par la machine : " + code_unique)


def executer_session_releve_et_caisse(dictionnaire_clients, fonction_saisie_securisee):
    """Gère la saisie des index de consommation et l'encaissement financier.

    Arguments:
        dictionnaire_clients (dict): Le dictionnaire des abonnés du réseau.
        fonction_saisie_securisee (function): La fonction de validation numérique.

    Retour:
        list: Une liste de tuples contenant les transactions validées de la session.
    """
    panier_factures = []
    continuer_saisie = "OUI"
    
    while continuer_saisie == "OUI":
        print("\n--- MISE À ZONE ET ENCAISSEMENT ---")
        code_saisi = input("Entrez le code unique de l'abonné : ").strip()
        
        if code_saisi not in dictionnaire_clients:
            print("Erreur : Ce code n'existe pas dans le réseau.")
            continue
            
        client_actif = dictionnaire_clients[code_saisi]
        print("Client trouvé : " + client_actif.obtenir_nom())
        print("Dette antérieure : " + str(client_actif.obtenir_solde()) + " F CFA.")
        
        nouveau_releve = fonction_saisie_securisee("Entrez la valeur du nouvel index lu : ")
        
        # Utilisation stricte du setter pour l'encapsulation
        if not client_actif.modifier_nouvel_index(nouveau_releve):
            print("Erreur : L'index saisi est inférieur à l'ancien index.")
            continue
            
        volume = client_actif.calculer_consommation()
        montant_total_du = client_actif.calculer_facture()
        
        print("Montant total à payer (incluant les impayés) : " + str(montant_total_du) + " F CFA.")
        montant_verse = fonction_saisie_securisee("Entrez le montant versé au guichet : ")
        
        # Gestion sécurisée du recouvrement et du report de dette
        reste_a_payer = montant_total_du - montant_verse
        if reste_a_payer < 0:
            print("Le système rend la monnaie : " + str(abs(reste_a_payer)) + " Francs CFA.")
            client_actif.modifier_solde(0)
        else:
            client_actif.modifier_solde(reste_a_payer)
            if reste_a_payer > 0:
                print("Note : Un solde impayé de " + str(reste_a_payer) + " F sera reporté.")
                
        # Bascule automatique du cycle de l'index
        client_actif.cloturer_periode_index()
        
        # Mémorisation de la transaction pour le rapport de caisse
        ligne_facture = (client_actif, volume, montant_verse)
        panier_factures.append(ligne_facture)
        
        reponse = input("Voulez-vous traiter un autre abonné ? (OUI/NON) : ").strip()
        continuer_saisie = reponse.upper()
        
    return panier_factures

#  FIN DU CODE DE OPERATIONS.PY
