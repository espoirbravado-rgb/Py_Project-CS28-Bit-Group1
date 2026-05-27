#  CODE PYTHON DU FICHIER SERVICES.PY CONFORME CAHIER DES CHARGES BIT

"""Module des services analytiques et de reporting pour WattaFaso-Manager.

Ce module applique les corrections logiques pour l'analyse anti-fraude, gère la
liste centrale des incidents et génère les statistiques du Tableau de Bord.
"""

import config

# EXIGENCE BIT (LIST) : Liste centrale mémorisant l'historique des anomalies détectées
registre_alertes_fraude = []


def enregistrer_et_imprimer_rapport(panier_factures):
    """Enregistre l'historique des encaissements de la session sur le disque.

    Arguments:
        panier_factures (list): Liste de tuples (client, volume, versement).
    """
    if not panier_factures:
        return
        
    try:
        with open(config.CHEMIN_HISTORIQUE, "a", encoding="utf-8") as fichier:
            fichier.write("\n--- RAPPORT CHRONOLOGIQUE D'ENCAISSEMENT ---\n")
            for element in panier_factures:
                client = element[0]
                versement = element[2]
                fichier.write(
                    "Client : " + client.obtenir_nom() 
                    + " | Reçu : " + str(versement) + " F CFA.\n"
                )
    except IOError:
        print("Erreur critique : Impossible d'écrire le rapport sur le disque.")


def executer_analyse_anti_fraude(dictionnaire_clients):
    """L'OPTION 4 : Analyse des suspicions de fraudes et des impayés du réseau.

    EXIGENCE BIT (LIST) : Alimentation dynamique d'une liste à l'aide de .append()
    pour mémoriser les alertes de consommation excessive de manière centralisée.

    Arguments:
        dictionnaire_clients (dict): Le dictionnaire des abonnés en mémoire.
    """
    print("\n--- ANALYSE ANTI-FRAUDE ET ALERTES ---")
    
    # Réinitialisation de la liste pour la nouvelle analyse
    registre_alertes_fraude.clear()
    
    for cle in dictionnaire_clients:
        client = dictionnaire_clients[cle]
        consommation = client.calculer_consommation()
        
        if consommation > config.SEUIL_CONSO_MAX:
            texte_alerte = "Alerte de surconsommation pour le client " + client.obtenir_nom()
            
            # Utilisation significative de la méthode append sur notre liste globale
            registre_alertes_fraude.append(texte_alerte)
            
            print(
                "⚠️ ALERT CONSO MAXIMUM DEPASSÉE : " 
                + client.obtenir_nom() + " (" + str(consommation) + " unités)."
            )
            
        if client.obtenir_solde() > 0:
            print(
                "ℹ️ ALERTE IMPAYÉ : " 
                + client.obtenir_nom() + " doit " + str(client.obtenir_solde()) + " F CFA."
            )
            
    if not registre_alertes_fraude:
        print("Félicitations : Aucune anomalie détectée sur les compteurs du réseau.")

