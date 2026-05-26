# CODE PYTHON CORRIGÉ PEP8 POUR CONFIG.PY

"""Module de configuration globale pour l'application WattaFaso-Manager.

Ce module centralise toutes les constantes logistiques, les tarifs
et les chemins des fichiers de persistance du réseau.
"""

import os

# Création automatique du dossier s'il n'existe pas
DOSSIER_DATA = "données"
if not os.path.exists(DOSSIER_DATA):
    os.makedirs(DOSSIER_DATA)

# Chemins mis à jour vers le sous-dossier
CHEMIN_STOCK = os.path.join(DOSSIER_DATA, "abonnés.txt")
CHEMIN_HISTORIQUE = os.path.join(DOSSIER_DATA, "historique.txt")

TARIF_SOCIAL = 250
TARIF_COMMERCIAL = 450
TAXE_MAINTENANCE = 1000

SEUIL_CONSO_MAX = 500

# Variables d'innovation pour la gestion logistique du carburant
STOCK_CARBURANT_LITRES = 150
SEUIL_CRITIQUE_CARBURANT = 30

# FIN DU CODE DE CONFIG.PY
