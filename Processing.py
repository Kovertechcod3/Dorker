import re
from nltk.stem import PorterStemmer 
from nltk.corpus import wordnet 

stemmer = PorterStemmer()

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.add(l.name())
    return synonyms

def perform_keyword_search(results, keyword):
    keyword = keyword.lower()
    synonyms = get_synonyms(keyword) 
    ranked_results = []
    
    for result in results:
        title = result['title'].lower()
        snippet = result['snippet'].lower()
        
        stemmed_title = [stemmer.stem(word) for word in title.split()]
        stemmed_snippet = [stemmer.stem(word) for word in snippet.split()]
        
        # Stemming and synonyms
        if any(stem in stemmed_title for stem in [keyword] + list(synonyms)) or any(stem in stemmed_snippet for stem in [keyword] + list(synonyms)):
            count = len(re.findall(keyword, title + snippet))
            ranked_results.append((result, count))

    ranked_results.sort(key=lambda x: x[1], reverse=True)   
    return [result for result, count in ranked_results]
