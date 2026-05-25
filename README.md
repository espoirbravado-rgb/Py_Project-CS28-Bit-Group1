# Py_Project-CS28-Bit-Group1
# WattaFaso-Manager (V1.3.5)
## Système de Gestion de Réseau de Distribution d'Eau

---

# 📝 Description du Projet

**WattaFaso-Manager** est une application console développée en Python dans le cadre du module *Programming I with Python* au Burkina Institute of Technology (BIT).

Le projet a été conçu comme une solution de gestion simplifiée pour une organisation de distribution d’eau. Il permet de gérer les abonnés, suivre les consommations, automatiser la facturation, gérer les paiements et produire des analyses simples sur le fonctionnement du réseau.

L’objectif du projet était de développer une application réaliste intégrant les principaux concepts étudiés en Python, notamment :
- la programmation orientée objet,
- la gestion de fichiers,
- les structures de données,
- les fonctions,
- les modules,
- et les bonnes pratiques de développement logiciel.

---

# 🚀 Fonctionnalités Principales

## 📋 Gestion des abonnés
- Ajout de nouveaux abonnés
- Génération automatique de codes uniques
- Affichage du registre des abonnés
- Gestion des abonnés sociaux et commerciaux

## 💧 Gestion des consommations
- Enregistrement des index de consommation
- Calcul automatique des consommations
- Mise à jour des relevés

## 💰 Facturation et Paiements
- Calcul automatique des factures
- Gestion des paiements
- Gestion des impayés
- Calcul de la monnaie rendue

## ⚠️ Analyse et Surveillance
- Détection des consommations anormales
- Système simple d’alerte anti-fraude
- Tableau de bord logistique

## 💾 Persistance des Données
- Sauvegarde des données dans des fichiers texte
- Chargement automatique des abonnés
- Protection contre certaines erreurs de lecture

---

# 🛠️ Technologies Utilisées

- **Langage :** Python 3.x
- **Paradigme :** Programmation Orientée Objet (POO)
- **Stockage :** Fichiers texte (`.txt`)
- **Modules utilisés :**
  - `datetime`
  - `os`
  - gestion des exceptions Python standard

Le projet respecte les conventions de nommage `snake_case` ainsi que les principales recommandations de style PEP 8.

---

# 📂 Structure du Projet

```text
WattaFaso-Manager/
│
├── main.py
├── models.py
├── database.py
├── operations.py
├── services.py
├── config.py
│
└── données/
    ├── abonnés.txt
    └── historique.txt
```

## Description des fichiers

| Fichier | Rôle |
|---|---|
| `main.py` | Point d’entrée principal du programme |
| `models.py` | Définition des classes et logique orientée objet |
| `database.py` | Sauvegarde et chargement des données |
| `operations.py` | Gestion des opérations métiers |
| `services.py` | Services analytiques et tableau de bord |
| `config.py` | Constantes et paramètres du système |

---

# 📐 Architecture Orientée Objet (POO)
