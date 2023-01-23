# GLG: Automated Text Analysis for Improved Service Demand

By Curtis Pond, Julia Nickerson, and Sam Varghese

### Problem Definition

GLG helps people make smarter decisions by connecting them to experts. Hundreds of requests are submitted daily to GLG via an intake form. GLG wants to help people reach experts faster by:
1. Grouping common topics together
2. Grouping similar client requests together
3. Identifying underlying patterns in the data (NER, time-based patterns)

### :page_with_curl: Data 

#### Two Datasets: NER Corpus & All the News 2.0

|             | NER Corpus                                                                                                | All the News 2.0                                                                                                |
|-------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Description | * 47,959 sentences * Includes each word’s part-of-speech (noun, verb, etc.) and NER (geo, org, per, etc.) | * 27 million news articles published between 2016 and 2020 * Includes date, author, title, and publication name |
| Size        | ~15 MB                                                                                                    | ~9 GB                                                                                                           |
| Labels      | Labeled                                                                                                   | Unlabeled                                                                                                       |
| Task        | Supervised learning (named entity recognition)                                                            | Unsupervised learning (clustering)                                                                              |

### 2. Approach  :boom: 

This project covers four areas of NLP/ML to meet the needs of the business and resourcefulness of GLG’s current data pipelines for efficient data storage and retrieval.

1. Detection of topics and keywords
2. Named Entity Recognition (NER)
3. Grouping similar requests together (unsupervised learning)
4. Temporal direction of the customer request

### 3. Planned Deliverables :dart: 

1. A deployable ML model that performs NER with reasonable accuracy.
2. A clustering mechanism to find patterns from submitted topics or requests.
3. A hierarchical clustering method that can produce a hierarchical dendrogram of topics submitted over a period of time.
4. Some type of lightweight web interface for customers to interact with the model (e.g., Gradio for interface, HuggingFace Spaces for hosting). Example: [NER demo on Hugging Face](https://huggingface.co/spaces/jnick/NER)

### 4. In Progress - What's Next? :wrench: 
1. Work through Model Flow (NER -> Topic Modeling -> Text Classification).
2. Try Transformers to improve NER performance.
3. Further explore unsupervised methods to understand topics (including fine tuning).
4. Complete Gradio web interface for user interaction.

### 5. Resources :clapper: 

1. [EDA](https://github.com/nickersonj/glg-capstone/tree/main/EDA)
2. [Modeling](https://github.com/nickersonj/glg-capstone/tree/main/modeling)
3. [Project Pitch (2022-01-19) slides](https://github.com/nickersonj/glg-capstone/tree/main/Project_Pitch_Slides_2022-01-19.pdf)
