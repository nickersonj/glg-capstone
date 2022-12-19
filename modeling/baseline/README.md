# Establishing A Model Baseline

## Named Entity Recognition (NER) — *Supervised*

| File/Folder | Author | Description |
| --- | --- | --- |
| **ner_01_libraries.ipynb** | Julia | comparing Hugging Face Transformers and Flair libraries to decide which one to use |
| **ner_02_flair_data_prep.ipynb** | Julia | formatting data for input into Flair |
| **ner_03_flair_tiny.ipynb** | Julia | **baseline performance results (0.81 f1-score)** from training a NER model |
| **/ner_03_results** | Julia | folder of training logs |

## Text Classification — *Supervised*

| File/Folder | Author | Description |
| --- | --- | --- |
| **textclass_baseline_dataprep.ipynb** | Curtis | synthesizing the 2.7M article dataset into something usable for purposes of baseline modeling |
| **textclass_baseline_allthenews.ipynb** | Curtis | **baseline performance results (~0.95 f1-score with Logistic Regression)** from training a text classification model based on five news categories: business, healthcare, technology, sports, movies |
| **/data/all-the-news-25k.csv** | Curtis | curated dataset of 25K articles equally distributed across five target news categories |

## Topic Modeling — *Unsupervised*

| File/Folder | Author | Description |
| --- | --- | --- |
| **topicmodel_01_LDA.ipynb** | Julia | **baseline performance results (-1.5 UMass coherence score)** for topic modeling using Latent Dirichlet Allocation (LDA) |

## Clustering — *Unsupervised*

| File/Folder | Author | Description |
| --- | --- | --- |
| **cluster_01_scipy.ipynb** | Julia | **baseline performance** for Ward hierarchical clustering using scipy |

## Temporal Analysis — *Unsupervised*

| File/Folder | Author | Description |
| --- | --- | --- |
|  |  |  |
