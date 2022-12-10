# GLG: Automated Text Analysis for Improved Service Demand

By Curtis Pond, Julia Nickerson, and Sam Varghese

### Problem Definition

GLG helps people make smarter decisions by connecting them to experts. Hundreds of requests are submitted daily to GLG via an intake form. GLG wants to help people reach experts faster by:
1. Grouping common topics together
2. Grouping similar client requests together
3. Identifying underlying patterns in the data (NER, time-based patterns)

### 1. Data

#### Two Datasets: NER Corpus & All the News 2.0

|             | NER Corpus                                                                                                | All the News 2.0                                                                                                |
|-------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Description | * 47,959 sentences * Includes each word’s part-of-speech (noun, verb, etc.) and NER (geo, org, per, etc.) | * 27 million news articles published between 2016 and 2020 * Includes date, author, title, and publication name |
| Size        | ~15 MB                                                                                                    | ~9 GB                                                                                                           |
| Labels      | Labeled                                                                                                   | Unlabeled                                                                                                       |
| Task        | Supervised learning (named entity recognition)                                                            | Unsupervised learning (clustering)                                                                              |

### 2. :boom: Approach 

This project will cover four areas of NLP/ML to meet the needs of the business and resourcefulness of GLG’s current data pipelines for efficient data storage and retrieval.

1. Detection of topics and keywords
2. Named Entity Recognition (NER)
3. Grouping similar requests together (unsupervised learning)
4. Temporal direction of the customer request

### 3. Resources

1. [EDA](https://github.com/nickersonj/glg-capstone/tree/main/EDA)
2. [Modeling](https://github.com/nickersonj/glg-capstone/tree/main/modeling)

