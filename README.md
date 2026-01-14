# Projet_05_AIA02

Développement d'un Système Complet de Recommandation et de Génération d'Images
Machine learning : Développement de modèles

## Structure rapide
- `data/raw` : jeux bruts (reviews, images/texte).
- `data/processed` : données nettoyées/feature engineering.
- `src/reco` : scripts reco (vectorisation, PCA/LDA, kNN, clustering, métriques).
- `src/gan` : scripts GAN (préparation données, modèle, entraînement, évaluation FID/IS).
- `outputs` : résultats (courbes, images générées, prédictions).
- `models` : poids sauvegardés.
- `notebooks` : explorations rapides.
- `config/config.yml` : chemins, seed et hyperparamètres par défaut.

## Démarrage env (suggestion)
```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Objectif
Ce projet vise à concevoir et comparer plusieurs stratégies de recommandation de produits à partir du dataset **Amazon Reviews 2023**, en mobilisant des approches à base de règles, des modèles supervisés et des méthodes non supervisées.

---

## Données utilisées
- Dataset Amazon Reviews 2023 (sous-ensemble multi-catégories)
- `amazon_reviews_cleaned.csv` : données nettoyées au niveau interaction
- `amazon_reviews_model.csv` : données encodées pour les modèles collaboratifs
- `user_behavior_features.csv` : features comportementales agrégées par utilisateur

---

## Nettoyage & préparation
- traitement des valeurs manquantes
- normalisation des notes (`rating_norm`)
- encodage des utilisateurs et produits
- uniformisation des timestamps
- séparation des datasets selon leur usage (EDA, clustering, modèles)

---

## Analyse exploratoire
Analyses univariées et bivariées sur :
- volume et récence des interactions
- distribution des notes
- préférences de catégories
- patterns temporels

Ces analyses mettent en évidence une **forte sparsité** et une distribution très déséquilibrée (long tail).

---

## Feature engineering (comportement utilisateur)
- volume d’interactions et récence
- entropie des catégories
- style de notation et longueur des avis
- patterns temporels (semaine / week-end)

Les features sont regroupées dans `user_behavior_features.csv`.

---

## Stratégies de recommandation

### Baselines
- popularité globale et par catégorie
- produits tendances (pondération temporelle)
- nouveautés bien notées

### Approche non supervisée
- **Clustering utilisateur (KMeans)**
- DBSCAN testé pour comparaison et détection d’outliers  
Recommandation basée sur la popularité intra-cluster.

### Approches supervisées
- **kNN user-based**
- **LSA (SVD)**  
LSA est retenu comme le meilleur modèle supervisé en raison de sa capacité à capturer des préférences latentes.

- **LSA** est la meilleure approche supervisée en théorie.
- **Le clustering utilisateur** est la solution la plus robuste en pratique face au cold-start.
- Une approche hybride serait idéale dans un contexte applicatif réel.


