import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download the necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()


def preprocess_dorks(dorks):
    preprocessed_dorks = []
    for dork in dorks:
        # Tokenization
        tokens = word_tokenize(dork)

        # Lowercasing
        tokens = [token.lower() for token in tokens]

        # Removal of special characters
        tokens = [re.sub(r'[^a-zA-Z0-9]', '', token) for token in tokens]

        # Stopword removal and lemmatization
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words("english")]

        # Join tokens back into a string
        preprocessed_dork = " ".join(tokens)

        # Append preprocessed dork to the list
        preprocessed_dorks.append(preprocessed_dork)

    return preprocessed_dorks
