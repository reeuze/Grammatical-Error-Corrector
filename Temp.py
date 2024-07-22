import re
import nltk
import spacy
from nltk.tokenize import word_tokenize
from num2words import num2words
from textblob import TextBlob


## Pre-processing sentence
def function_normalize(sentence):
    tokens = word_tokenize(sentence)
    normalized_tokens = []
    for token in tokens:
        token = token.lower()
        token = re.sub(r'\W+', '', token)  # Remove non-alphanumeric characters
        if token.isdigit():
            token = num2words(token)
        if token:
            normalized_tokens.append(token)
    return normalized_tokens

nlp = spacy.load("en_core_web_sm")

def function_recognize_entities(sentence):
    doc = nlp(sentence)
    entities = [(ent.sentence, ent.label_) for ent in doc.ents]
    return entities

def function_replace_entities(sentence, entities):
    for entity, label in entities:
        if label in ["PERSON", "GPE", "ORG", "DATE"]:
            placeholder = f'[{label}]'
            sentence = sentence.replace(entity.lower(), placeholder)
    return sentence

sentence = "John Doe goes in New York on July 5th, 2021."

normalize = function_normalize(sentence)
entities = function_recognize_entities(normalize)
sentence_with_placeholder = function_replace_entities(sentence, entities)

print (f" Sentence with placeholder = {sentence_with_placeholder}")
# Excpected output = "[PERSON] doe goes in [GPE] on [DATE]"

## Correction Grammatical Error Algorithm
def rule_based_correction(text):
    text_blob = TextBlob(text)
    corrected_text = str(text_blob.correct())
    return corrected_text

def model_based_correction(dataset):
    print('a') # Unfinished

correction = rule_based_correction(sentence_with_placeholder)
print (f"Correction based on rule : {correction}")
correction = model_based_correction(correction)
print (f"Correction based on machine learning model : {correction}")

## Finishing
def replace_placeholders(sentence, entities):
    for entity, label in entities:
        placeholder = f'[{label}]'
        sentence = sentence.replace(placeholder, entity, 1)
    return sentence

def format_sentence(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    formatted_sentences = [sentence.capitalize() for sentence in sentences]
    formatted_text = ' '.join(formatted_sentences)
    return formatted_text

corrected_sentence = replace_placeholders(correction)
corrected_sentence = format_sentence(corrected_sentence)

print (f"corrected sentence : {corrected_sentence}")