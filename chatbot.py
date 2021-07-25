import random
import json
import pickle
import re
from absl.logging import ERROR
from google.protobuf import message
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from numpy.lib.npyio import load
from tensorflow.keras.models import load_model
from tensorflow.python.keras import models
import arabic_reshaper
from bidi.algorithm import get_display

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json', encoding="utf8").read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.model')

def clean_up_sentence(sentence):
    sentence_words = nltk.tokenize.wordpunct_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

reshaped_print = arabic_reshaper.reshape(("ابدأ بالكلام"))
bidi_print = get_display(reshaped_print)
print(bidi_print)

while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)

    reshaped_res = arabic_reshaper.reshape(res)
    bidi_res = get_display(reshaped_res)
    print(bidi_res)
