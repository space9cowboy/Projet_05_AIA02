from datasets import load_dataset
import pandas as pd
from pathlib import Path

# Dossier de sortie CSV
output_dir = Path("/Users/tsantaloic/Desktop/Projet_05_AIA02/data/raw")
output_dir.mkdir(exist_ok=True)

CATEGORIES = [
    "Automotive",
    "Books",
    "CDs_and_Vinyl",
    "Cell_Phones_and_Accessories",
    "Clothing_Shoes_and_Jewelry",
    "Digital_Music",
    "Electronics",
]

# Nombre de reviews à récupérer par catégorie
MAX_REVIEWS_PER_CATEGORY = 3000

for category in CATEGORIES:
    config_name = f"raw_review_{category}"
    print(f"\nCatégorie : {category} ({config_name})")

    # 1) Chargement en mode STREAMING -> ne télécharge pas tout le fichier
    stream = load_dataset(
        "McAuley-Lab/Amazon-Reviews-2023",
        name=config_name,
        streaming=True,
    )["full"]

    # 2) On récupère seulement les 100 premières lignes
    rows = []
    for i, row in enumerate(stream):
        if i >= MAX_REVIEWS_PER_CATEGORY:
            break
        rows.append(row)

    print(f"{len(rows)} reviews récupérées")

    # 3) Conversion en DataFrame pandas
    df = pd.DataFrame(rows)

    # 4) Sauvegarde dans un CSV
    csv_path = output_dir / f"{category}.csv"
    df.to_csv(csv_path, index=False)

    print(f"CSV créé : {csv_path}")
