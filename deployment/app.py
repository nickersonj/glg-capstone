# Imports
import gradio as gr
from sklearn.linear_model import LogisticRegression
import pickle5 as pickle
import re
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from flair.data import Sentence
from flair.models import SequenceTagger

# Load pickled model and vectorizer
model = 'lr_021823.pkl'
model_loaded = pickle.load(open(model, 'rb'))
vectorizer = 'vectorizer_021823.pkl'
vectorizer_loaded = pickle.load(open(vectorizer, 'rb'))

# Process input text, including removing stopwords, converting to lowercase, and removing punctuation
stop = stopwords.words('english')
def process_text(text):
    text = [word for word in text.split() if word not in stop]
    text = str(text).lower()
    text = re.sub(
        f"[{re.escape(string.punctuation)}]", " ", text
    )
    text = " ".join(text.split())
    return text

# Vectorize text
def vectorize_text(text):
    text = process_text(text)
    text = vectorizer_loaded.transform([text])
    return text

# Valid input for the model so number of features match
def class_predict(text):
    text = process_text(text)
    vec = vectorizer_loaded.transform([text])
    prediction = model_loaded.predict(vec)
    return prediction


# Specify NER model
tagger = SequenceTagger.load('best-model.pt') # SequenceTagger.load('best-model.pt')

# Runs NER on input text
def run_ner(input_text):
    sentence = Sentence(input_text)
    tagger.predict(sentence)
    output = []
    for entity in sentence.get_spans('ner'):
        output.append({'entity': entity.get_label('ner').value, 'word': entity.text, 'start': entity.start_position, 'end': entity.end_position})
    return {"text": input_text, "entities": output}

# Run both models, and return a tuple of their results
def run_models(input_text):
    prediction = class_predict(input_text)
    entities = run_ner(input_text)
    return prediction, entities

# Define interface
demo = gr.Interface(fn=run_models,
                    title="Text Classification & Named Entity Recognition Demo",
                    description="This is a demo of a text classification model using logistic regression as well as a named entity recognition model. Enter in some text or use one of the provided examples. Note that common named entity recognition tags include **geo** (geographical entity), **org** (organization), **per** (person), and **tim** (time).",
                    article='*This demo is based on Logistic Regression and Named Entity Recognition models trained by Curtis Pond and Julia Nickerson as part of their FourthBrain capstone project. For more information, check out their [GitHub repo](https://github.com/nickersonj/glg-capstone).*',
                    inputs=gr.Textbox(lines=10, placeholder='Input text here...', label="Input Text"),
                    outputs=[gr.Textbox(label="Predicted Classification Label: Healthcare: 0, Other: 1, Technology: 2", lines=2, placeholder='Predicted label will appear here...'), 
                             gr.HighlightedText(label='Named Entity Recognition Results')],
                    # These examples are just placeholders; once the LR model is working, we can use longer example text such as paragraphs
                    examples=['Next to toys and books, there are medications and care charts for baby Elin Anderson who burst onto the scene early.\n "She was only 13.1 ounces, 10 inches long. You could hold her in your hand," said Jill Anderson. "She\'s had 12 surgeries, thousands of blood draws, blood transfusions. She was on a breathing tube for many months before she got this trach. She\'s just been through so much, but she\'s come so far." But the journey to get Elin home took 411 days -- initially because she needed NICU care, but eventually because Jill and Kyle couldn\'t find a home healthcare nurse.', 
                              'Despite Meta, the company formerly known as Facebook, losing billions of dollars on its metaverse efforts, the idea of spending time in virtual online worlds is increasingly becoming part of the public consciousness, and the buzz is set to grow in 2023, according to Khanna. “Retail and entertainment companies will launch increasing pilots on how to build customer engagement and loyalty in the various metaverses, especially game platforms like Roblox,” she says. “Metaverse natives who have grown up gaming and socializing in alternate digital realities will drive companies to host concerts, fashion weeks, customer journeys and edutainment activities in 2023.”', 
                              'With the 2022 NFL regular season now concluded, the playoff picture is set. The Chiefs clinched the 1-seed in the AFC with their win over the Raiders on Saturday, while the Philadelphia Eagles clinched the 1-seed in the NFC on Sunday with a win over the New York Giants. The Miami Dolphins clinched the last AFC postseason spot with a win and a New England Patriots loss.'],
                    allow_flagging='never'
)

demo.launch()

