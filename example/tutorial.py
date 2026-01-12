#!/usr/bin/env python
# coding: utf-8

# # TP : Analyse de la transpiration des plantes
# Ce notebook analyse les données de pesée pour extraire la transpiration nette des plantes.

# # 1. Importation des librairies nécessaires



# Importation des librairies, on leur donne des aliases pour faciliter leur utilisation, pas obligatoire
import pandas as pd
import matplotlib.pyplot as plt


# # 2. Chargement des données


# Lecture des données (on utilise sep="\t" car ton texte semble tabulé)
df = pd.read_csv("data_tutorial.csv", sep=",", decimal=",") # Modifier si nécessaire sur base du format réel du fichier
# sep = ","  # Exemple de modification si le fichier utilise des virgules comme séparateurs
# sep = ";"  # Exemple de modification si le fichier utilise des points-virgules comme séparateurs
# sep = "\t"  # Exemple de modification si le fichier utilise des tabulations comme séparateurs
# decimal = ","  # Exemple de modification si le fichier utilise des virgules comme séparateurs décimaux
# decimal = "."  # Exemple de modification si le fichier utilise des points comme séparateurs décimaux

# Affichage des premières lignes pour vérification
print("Aperçu des données chargées :")
df.head()


# On peut lire n'importe quel type de fichier, certains demandent l'importation d'un package spécifique

import openpyxl
df = pd.read_excel("data_tutorial.xlsx", decimal=",")
df.head()


# Nettoyage de la date (on retire " UTC" pour faciliter la conversion)
df["Date_Heure"] = df["Date_Heure"].str.replace(" UTC", "") # Retirer " UTC" si présent
df["Date_Heure"] = pd.to_datetime(df["Date_Heure"]) # Convertir en datetime, un format standard pour les dates
# Faire uniquement si nécessaire en fonction du format réel des dates dans le fichier


# # 3. Calcul de nouvelle variable

# On peut maintenant calculer une nouvelle variable, par exemple la somme des balances (que ça soit utile ou non) :
df["Sum_all"] = df[["Bal1", "Bal2", "Bal3", "Bal4", "Bal5", "Bal6"]].sum(axis=1)
# On peut décider de n'avoir que les heures minutes si les jours ne sont pas nécessaires: 
df['hm'] = pd.to_datetime(df['Date_Heure'], format="%H:%M")
df.head()


# # 4. Réaliser un graphe



plt.figure() 
plt.plot(df["hm"], df["Bal1"], label="Balance 1")
plt.title("Exemple de graphe : Balance 1 au cours du temps") # Ajout du titre du graphe
plt.xlabel("Temps") # Ajout de l'étiquette de l'axe x
plt.ylabel("Poids perdu (g)") # Ajout de l'étiquette de l'axe y
plt.legend() # Ajout de la légende pour identifier les courbes
plt.xticks(rotation=45) # Rotation des labels de l'axe x pour meilleure lisibilité
plt.grid(True, alpha=0.3) # Ajout d'une grille pour faciliter la lecture des valeurs
plt.tight_layout() # Ajustement de la mise en page pour éviter le chevauchement
plt.show()


# L'axe des X n'a pas un affichage très propre, On peut forcer cela, ici, on va décider d'afficher uniquement les heures et minutes.


import matplotlib.dates as mdates
ax = plt.gca() 
# On ne garde que l'heure et les minutes
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M')) # Formatage des dates sur l'axe x
plt.plot(df["hm"], df["Bal1"], label="Balance 1")
plt.title("Exemple de graphe : Balance 1 au cours du temps") # Ajout du titre du graphe
plt.xlabel("Temps") # Ajout de l'étiquette de l'axe x
plt.ylabel("Poids perdu (g)") # Ajout de l'étiquette de l'axe y
plt.legend() # Ajout de la légende pour identifier les courbes
plt.xticks(rotation=45) # Rotation des labels de l'axe x pour meilleure lisibilité
plt.grid(True, alpha=0.3) # Ajout d'une grille pour faciliter la lecture des valeurs
plt.tight_layout() # Ajustement de la mise en page pour éviter le chevauchement
plt.show()


plt.figure()
ax = plt.gca() 
# On ne garde que l'heure et les minutes
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M')) # Formatage des dates sur l'axe x
plt.plot(df["hm"], df["Bal1"], label="Balance 1")
plt.plot(df["hm"], df["Bal2"], label="Balance 2")
plt.plot(df["hm"], df["Bal3"], label="Balance 3")
plt.plot(df["hm"], df["Sum_all"], label="Somme des balances", linewidth=3, color='black', linestyle='--')
plt.title("Exemple de graphe : Somme des balances au cours du temps") # Ajout du titre du graphe
plt.xlabel("Temps")
plt.ylabel("Poids perdu (g)")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# On peut tout simplement afficher les mesures par groupes aussi, que cela ait du sens ou non


# Sélection des colonnes de balances (Bal1 à Bal6)
cols_balances = ["Bal1", "Bal2", "Bal3", "Bal4", "Bal5", "Bal6"]

plt.figure(figsize=(10, 6), dpi=150)
df[cols_balances].boxplot()

plt.title("Distribution des mesures par Balance (Boxplot)", fontsize=14)
plt.ylabel("Poids / Delta (g)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

