"""
Text preprocessing module
"""

import re
import configparser
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import logging

config = configparser.ConfigParser()
config.read('config.ini')

STOPWORDS = set(config['preprocessing'].get('stopwords', '').split(','))

def clean(text):
    """Lowercase and remove special chars from text"""
    text = text.lower()
    return re.sub(r'[^a-zA-Z0-9]', '', text)

def tokenize(text):
    """Tokenize text into words"""
    try:
        words = word_tokenize(text)
        return words
    except ValueError as e:
        logging.error(f"Tokenization error: {e}")
        return []

def remove_stopwords(words):
    """Remove stopwords from list of word tokens"""
    return [w for w in words if w not in STOPWORDS]

def lemmatize(words):
    """Lemmatize a list of word tokens"""
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(w) for w in words]
    return lemmas

def preprocess(text):
    """Preprocess text by cleaning, normalizing and formatting"""
    if not isinstance(text, str):
        raise TypeError('Text input must be a string')

    text = clean(text)
    words = tokenize(text)
    words = remove_stopwords(words)
    lemmas = lemmatize(words)
    return " ".join(lemmas)
