# Prédiction de la Qualité du Vin Rouge 🍷

## Description
Ce projet de Machine Learning vise à prédire la qualité d’un vin rouge
à partir de ses caractéristiques physicochimiques.
L’objectif est d’automatiser l’évaluation de la qualité du vin,
habituellement réalisée par des experts, en utilisant des techniques
d’apprentissage automatique supervisé.

Le problème est formulé comme une **classification binaire**
(vin de bonne qualité / vin de mauvaise qualité).

---

## Dataset
Le dataset utilisé est **WineQT.csv**.

- Nombre d’observations : 1143
- Nombre de variables : 11 variables physicochimiques
- Variable cible : `quality-bin`
- Variable supprimée : `Id`

Les variables décrivent des propriétés chimiques telles que :
acidité, alcool, sulfates, sucre résiduel, chlorides, etc.

---

## Objectifs du projet
- Comprendre la relation entre les caractéristiques chimiques et la qualité du vin
- Mettre en œuvre plusieurs modèles de classification
- Traiter les valeurs aberrantes (outliers)
- Améliorer les performances via l’ingénierie des variables
- Comparer différentes approches et sélectionner le meilleur modèle

---

## Méthodologie
1. Analyse exploratoire des données (EDA)
2. Analyse de corrélation
3. Détection et traitement des outliers (winsorization)
4. Séparation des données (train / test)
5. Entraînement des modèles
6. Évaluation des performances
7. Comparaison des approches
8. Déploiement du modèle final

---

## Approches utilisées

### Approche Baseline
Prétraitement minimal avec les modèles suivants :
- Régression Logistique
- Random Forest
- Extra Trees
- Gradient Boosting

### Approche Avancée
- Traitement des outliers par winsorization
- Ingénierie des variables (features combinées)
- Sélection des variables pertinentes

---

## Méthodes d’ensemble
Les techniques d’ensemble suivantes ont été appliquées :
- Voting Classifier
- Bagging
- Stacking (modèle final)

Le modèle **Stacking** a donné les meilleurs résultats.

---

## Évaluation
Les modèles ont été évalués à l’aide des métriques suivantes :
- Accuracy
- Precision
- Recall
- F1-score (F1-macro)

Le F1-macro est privilégié en raison du déséquilibre des classes.

### Résultats principaux
| Approche | F1-Macro | Accuracy |
|--------|----------|----------|
| Baseline | 0.70 | 0.67 |
| Prétraitement avancé | 0.75 | 0.72 |
| Voting / Bagging | 0.78 | 0.74 |
| **Stacking (final)** | **0.81** | **0.77** |

---

## Déploiement
Le modèle final (Stacking) a été déployé à l’aide de **Streamlit**.
L’application permet :
- La saisie des caractéristiques physicochimiques d’un vin
- La prédiction instantanée de sa qualité
- L’affichage du résultat (bonne / mauvaise qualité)

---

## Technologies utilisées
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit

---

## Auteurs
- **Hiba El Hamdani**
- **Nawal Ait-Tami**

---

## Encadrement
Projet réalisé sous l’encadrement de :  
**M. Abdelghani Ghazdali**

École Nationale des Sciences Appliquées de Khouribga  
Année universitaire : 2025 – 2026