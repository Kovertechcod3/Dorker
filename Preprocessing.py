"""
Text Preprocessing Module

Provides functions for cleaning, tokenizing, removing stopwords, and lemmatizing text.
"""

import re
import configparser
import logging
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

# Ensure necessary NLTK data is downloaded
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

def load_stopwords(config_file='config.ini'):
    """Load stopwords from configuration file or use NLTK default stopwords"""
    config = configparser.ConfigParser()
    if not config.read(config_file):
        logging.warning(f"Config file '{config_file}' not found or empty. Using NLTK default stopwords.")
        return set(stopwords.words('english'))

    stopwords_list = config['preprocessing'].get('stopwords', '')
    if stopwords_list:
        return set(stopwords_list.split(','))
    else:
        logging.warning("No stopwords specified in config. Using NLTK default stopwords.")
        return set(stopwords.words('english'))

STOPWORDS = load_stopwords()

def clean(text):
    """Lowercase and remove special characters from text, preserving spaces"""
    text = text.lower()
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def tokenize(text):
    """Tokenize text into words"""
    try:
        words = word_tokenize(text)
        return words
    except Exception as e:
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
    """Preprocess text by cleaning, tokenizing, removing stopwords, and lemmatizing"""
    if not isinstance(text, str):
        raise TypeError('Text input must be a string')

    text = clean(text)
    words = tokenize(text)
    words = remove_stopwords(words)
    lemmas = lemmatize(words)
    return " ".join(lemmas)
