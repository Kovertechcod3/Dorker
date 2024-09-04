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
    """Load stopwords from configuration file or use NLTK default stopwords."""
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
    """Lowercase and remove special characters from text, preserving spaces."""
    if not isinstance(text, str):
        logging.error("Input text must be a string.")
        raise TypeError("Input text must be a string.")
    
    text = text.lower()
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    logging.debug(f"Cleaned text: {cleaned_text}")
    return cleaned_text

def tokenize(text):
    """Tokenize text into words."""
    try:
        words = word_tokenize(text)
        logging.debug(f"Tokenized words: {words}")
        return words
    except Exception as e:
        logging.error(f"Tokenization error: {e}")
        return []

def remove_stopwords(words):
    """Remove stopwords from list of word tokens."""
    filtered_words = [w for w in words if w not in STOPWORDS]
    logging.debug(f"Words after stopword removal: {filtered_words}")
    return filtered_words

def lemmatize(words):
    """Lemmatize a list of word tokens."""
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(w) for w in words]
    logging.debug(f"Lemmatized words: {lemmas}")
    return lemmas

def preprocess(text):
    """Preprocess text by cleaning, tokenizing, removing stopwords, and lemmatizing."""
    logging.info("Starting text preprocessing.")
    text = clean(text)
    words = tokenize(text)
    words = remove_stopwords(words)
    lemmas = lemmatize(words)
    processed_text = " ".join(lemmas)
    logging.info("Text preprocessing completed.")
    return processed_text
