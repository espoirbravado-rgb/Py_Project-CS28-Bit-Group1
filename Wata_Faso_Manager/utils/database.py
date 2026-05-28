# SECURE AND HARDENED DATABASE.PY PYTHON CODE

"""Data persistence management module for WattaFaso-Manager.

This module handles reading and writing the registry with strict 
column validation to prevent IndexError-type crashes.
"""

import config
import models


def charger_base_de_donnees():
    """Loads the subscriber registry from the text storage file.

    Internal security: Explicitly validates the 6-column structure of each
    line before accessing data, avoiding crashes on corrupted files.

    Returns:
        dict: The dictionary of subscriber objects indexed by their unique code.
    """
    dictionnaire_clients = {}
    
    try:
        with open(config.CHEMIN_STOCK, "r", encoding="utf-8") as fichier:
            for numero_ligne, ligne in enumerate(fichier, 1):
                ligne_nettoyee = ligne.strip()
                if not ligne_nettoyee:
                    continue
                    
                segments = ligne_nettoyee.split(";")
                
                # CRITICAL FIX C: Explicit structure validation
                if len(segments) != 6:
                    print(
                        "Error Line " + str(numero_ligne) 
                        + " : Invalid structure (" + str(len(segments)) 
                        + "/6 columns). Line ignored."
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
                            "Warning Line " + str(numero_ligne) 
                            + " : Unknown subscriber type '" + str(type_client) + "'."
                        )
                        
                except ValueError:
                    print("Error Line " + str(numero_ligne) + " : Corrupted numerical data.")
                    continue
                    
    except FileNotFoundError:
        print("Note: Storage file not found. It will be created automatically.")
        
    return dictionnaire_clients


def sauvegarder_base_de_donnees(dictionnaire_clients):
    """Saves the current state of the dictionary to the storage file.

    Arguments:
        dictionnaire_clients (dict): The dictionary of subscribers in memory.
    """
    try:
        with open(config.CHEMIN_STOCK, "w", encoding="utf-8") as fichier:
            for cle in dictionnaire_clients:
                client = dictionnaire_clients[cle]
                
                if isinstance(client, models.AbonneSocial):
                    etiquette = "SOCIAL"
                elif isinstance(client, models.AbonneCommercial):
                    etiquette = "COMMERCIAL"
                else:
                    continue
                    
                ligne = (
                    etiquette + ";"
                    + client.obtenir_code() + ";"
                    + client.obtenir_nom() + ";"
                    + str(client.obtenir_ancien_index()) + ";"
                    + str(client.obtenir_nouvel_index()) + ";"
                    + str(client.obtenir_solde()) + "\n"
                )
                fichier.write(ligne)
                
    except IOError:
        print("Critical error: Unable to write data to disk.")

#  END OF DATABASE.PY CODE
