import argparse
import json
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import re
import logging
import search

stemmer = PorterStemmer()

def get_synonyms(word):
    synonyms = set()
  
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.add(l.name())
  
    return synonyms

def search_keywords(results, keyword):
    keyword = keyword.lower()
    synonyms = get_synonyms(keyword)
  
    ranked_results = []

    for result in results:
        title = result['title'].lower()
        snippet = result['snippet'].lower()

        stemmed_title = [stemmer.stem(w) for w in title.split()]
        stemmed_snippet = [stemmer.stem(w) for w in snippet.split()]

        if any(s in stemmed_title for s in [keyword] + list(synonyms)) or any(s in stemmed_snippet for s in [keyword] + list(synonyms)):
            count = len(re.findall(keyword, title + snippet))
            ranked_results.append((result, count))

    ranked_results.sort(key=lambda x: x[1], reverse=True)
  
    return [result for result, count in ranked_results]

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="Keyword to search")
    args = parser.parse_args()

    keyword = args.keyword
    dork = input("Enter dork query: ")

    try:
        results = search.dork_search(dork)  # Assuming dork_search() is defined in search.py
        results = search_keywords(results, keyword)
        print(json.dumps(results, indent=2))
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
