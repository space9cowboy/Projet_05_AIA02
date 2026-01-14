# Comparaison des stratégies de recommandation

## 1. Stratégies analysées

Deux approches ont été mises en œuvre :

- **Approche supervisée** :  
  Un modèle de **régression logistique** prédit la probabilité qu’un utilisateur aime un produit (`like = rating ≥ 4`), à partir de ses caractéristiques comportementales (activité, diversité, sentiment, etc.).  
  Le modèle est évalué avec **ROC AUC, matrice de confusion, courbes ROC et PR, calibration**.

- **Approche non supervisée** :  
  Un **clustering KMeans** segmente les utilisateurs selon leur comportement.  
  La recommandation repose sur les **Top-N produits** les plus populaires et les mieux notés à l’intérieur de chaque cluster.  
  Le choix du nombre de clusters est validé avec **Silhouette** et **Elbow**.

---

## 8. Comparaison des deux stratégies

| Critère | Modèle supervisé (Logistic Regression) | Clustering (KMeans + Top-N) |
|--------|---------------------------------------|-----------------------------|
| **Précision** | Élevée. Le modèle prédit directement la probabilité qu’un utilisateur aime un produit (ROC AUC, F1). | Moyenne. Les recommandations sont basées sur la popularité moyenne du cluster. |
| **Robustesse** | Sensible au bruit dans les notes et aux classes déséquilibrées. | Très robuste : les moyennes de cluster lissent les comportements atypiques. |
| **Interprétabilité** | Bonne : coefficients, importance des variables, SHAP et permutation importance. | Excellente : chaque cluster correspond à un profil utilisateur clair. |
| **Facilité de déploiement** | Plus complexe : nécessite un pipeline (scaling, modèle, features). | Très simple : assignation au cluster + table Top-N. |
| **Cold start** | Faible : nécessite de l’historique et des labels. | Meilleur : un utilisateur peut être affecté à un cluster avec peu d’interactions. |

---

## 9. Meilleure stratégie de recommandation

### Approche hybride : Clustering + Scoring supervisé

1. **Segmentation**  
   L’utilisateur est assigné à un **cluster** via KMeans.

2. **Sélection de candidats**  
   On récupère les **Top-N produits** les plus populaires et les mieux notés dans ce cluster.

3. **Classement supervisé**  
   Le modèle supervisé calcule pour chaque produit la **probabilité que l’utilisateur l’aime**.

4. **Recommandation finale**  
   On recommande les produits ayant la probabilité la plus élevée.

---

### Justification

Cette stratégie hybride permet de :
- tirer parti de la **robustesse et de l’explicabilité** du clustering,
- bénéficier de la **précision et de la personnalisation** du modèle supervisé.

Elle limite les recommandations hors contexte tout en offrant un classement personnalisé.

---

