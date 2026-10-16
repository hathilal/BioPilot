# Kaggle first run: FLIP2 Alpha-amylase

This is the first reproducible BioPilot exercise. It downloads the official FLIP2 Alpha-amylase `one-to-many` CSV split and audits the file before fitting any model. Do not upload the dataset to this repository; `data/` is git-ignored.

## Why this dataset?

The official FLIP2 page describes Alpha-amylase as 3,706 variants, including 488 single mutants, with measured stain-removal activity. In the `one-to-many` split, training is on single-mutant variants and evaluation is on variants with more mutations. This tests generalization to more mutations, rather than a random split.

Source: https://flip.protein.properties/  
Dataset URL: https://flip.protein.properties/assets/splits/amylase/one_to_many.csv.gz

The dataset page reports an MIT license for Alpha-amylase. Preserve the source attribution and check the dataset README/citation guidance before redistributing data or derived artifacts.

## Kaggle notebook — Cell 1: download and inspect

Enable internet in the Kaggle notebook settings if the download is blocked.

```python
from pathlib import Path
import pandas as pd
from urllib.request import urlretrieve

DATA_DIR = Path("/kaggle/working/biopilot_data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

url = "https://flip.protein.properties/assets/splits/amylase/one_to_many.csv.gz"
csv_path = DATA_DIR / "amylase_one_to_many.csv.gz"

if not csv_path.exists():
    urlretrieve(url, csv_path)

df = pd.read_csv(csv_path)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
display(df.head())
```

The first download can take a short time; later runs reuse the saved file.

## Kaggle notebook — Cell 2: audit labels and official split

```python
required = {"sequence", "target", "set"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Unexpected dataset schema; missing columns: {missing}")

print("Rows per set:")
print(df["set"].value_counts(dropna=False))
if "validation" in df.columns:
    print("\nSet by validation flag:")
    print(pd.crosstab(df["set"], df["validation"], dropna=False))

print("\nMissing values:")
print(df[["sequence", "target", "set"]].isna().sum())
print("\nDuplicate sequences:", df["sequence"].duplicated().sum())
print("\nDuplicate sequence-target rows:", df.duplicated(["sequence", "target"]).sum())
print("\nSequence length summary:")
print(df["sequence"].astype(str).str.len().describe())
print("\nTarget summary by set:")
print(df.groupby("set", dropna=False)["target"].agg(["count", "mean", "std", "min", "median", "max"]))
print("\nExample sequence alphabet:", sorted(set("".join(df["sequence"].astype(str)))))
```

## Stop here and inspect the output

Before training, confirm the actual `set`/ `validation` convention, target distribution, sequence lengths, missing values, and duplicates. Do not randomly repartition this benchmark or use test labels for model selection. Share the output so the training code uses the correct official train, validation, and test rows.

## Training plan after the audit

1. Fit a small ridge-regression baseline using fixed-position amino-acid encoding, if sequence lengths and alphabet support it.
2. Tune hyperparameters only against validation data.
3. Evaluate the selected model once on the held-out test split, reporting Spearman correlation and a complementary error metric.
4. Save the model, preprocessing configuration, random seed, package versions, and metrics.
5. Only after the baseline is understood, compare pretrained protein-language-model embeddings or fine-tuning. A more complex model is not assumed to be better.

A retrospective active-learning simulation can compare acquisition strategies using the already-labelled pool, but it does not establish real wet-lab cost savings.
