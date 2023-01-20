"""
This script is used to test the initial version of a Gradio demo on a local machine, specifically for NER.
"""

import gradio as gr
from flair.data import Sentence
from flair.models import SequenceTagger

tagger = SequenceTagger.load('/Users/julia/Models/ner_04_results/best-model.pt')

def run_ner(input_text):
    sentence = Sentence(input_text)
    tagger.predict(sentence)
    entities = []
    for entity in sentence.get_spans('ner'):
        entities.append((entity.text, entity.get_label('ner').value, entity.get_label('ner').score))
    return entities

demo = gr.Interface(fn=run_ner, 
                    title='Named Entity Recognition Demo',
                    description='This demo performs **Named Entity Recognition** by tagging user-inputted sentence(s). Give it a try by entering a sentence or using one of the provided examples. Common tags include **geo** (geographical entity), **org** (organization), **per** (person), and **tim** (time). In the box on the right, the results will show the tagged words and their corresponding confidence scores.',
                    article='*This demo is based on a Named Entity Recognition model trained by Curtis Pond and Julia Nickerson as part of their FourthBrain capstone project. For more information, check out their [GitHub repo](https://github.com/nickersonj/glg-capstone).*',
                    inputs=gr.Textbox(label='Input Text', lines=2, placeholder='Type some text here...'), 
                    outputs=gr.Textbox(label='Named Entity Recognition Results', lines=2, placeholder=''),
                    examples=['The indictments were announced Tuesday by the Justice Department in Cairo.', "In 2019, the men's singles winner was Novak Djokovic who defeated Roger Federer in a tournament taking place in the United Kingdom.", 'In a study published by the American Heart Association on January 18, researchers at the Johns Hopkins School of Medicine found that meal timing did not impact weight.'],
                    allow_flagging='never'
)

demo.launch()
