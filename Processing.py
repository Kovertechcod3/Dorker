"""
Keyword Search Module

Provides functionality to search and rank keywords in search results using synonyms and stemming.
"""

import argparse
import json
import re
import logging
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import nltk
from scraping import dork_search

# Ensure necessary NLTK data is downloaded
nltk.download('wordnet', quiet=True)

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

def get_synonyms(word):
    """Retrieve a set of synonyms for a given word using WordNet."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    logging.debug(f"Synonyms for '{word}': {synonyms}")
    return synonyms

def search_keywords(results, keyword):
    """Search and rank search results based on the presence of a keyword and its synonyms."""
    keyword = keyword.lower()
    synonyms = get_synonyms(keyword)
    ranked_results = []

    for result in results:
        title = result.get('title', '').lower()
        snippet = result.get('snippet', '').lower()

        stemmed_title = [stemmer.stem(w) for w in title.split()]
        stemmed_snippet = [stemmer.stem(w) for w in snippet.split()]

        if any(s in stemmed_title for s in [keyword] + list(synonyms)) or any(s in stemmed_snippet for s in [keyword] + list(synonyms)):
            count = len(re.findall(keyword, title + snippet))
            ranked_results.append((result, count))
            logging.debug(f"Keyword '{keyword}' found {count} times in result: {result}")

    ranked_results.sort(key=lambda x: x[1], reverse=True)
    return [result for result, count in ranked_results]

def main():
    """Main function to execute the keyword search process."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description="Search for keywords in dork search results.")
    parser.add_argument("keyword", help="Keyword to search")
    args = parser.parse_args()

    keyword = args.keyword
    dork = input("Enter dork query: ")

    try:
        logging.info("Performing dork search")
        results = dork_search(dork)

        logging.info("Searching for keyword and synonyms")
        results = search_keywords(results, keyword)

        logging.info("Search completed. Displaying results:")
        print(json.dumps(results, indent=2))
    except Exception as e:
        logging.error(f"An error occurred during processing: {str(e)}")

if __name__ == '__main__':
    main()
