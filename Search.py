import argparse
import concurrent.futures 
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json

# Dork types for CLI
dork_types = {
  'site': ['site:', 'inurl:', 'intitle:'],
  'file': ['filetype:', 'ext:'],
  'misc': ['intext:', '-intext:', 'allintext:']  
}

def build_dork():

  print("Build your custom Google dork query")
  
  dork = ''
  dork_type = input("Select dork type (site, file, misc): ")

  if dork_type in dork_types:
    terms = dork_types[dork_type]
    term = input(f"Select term ({', '.join(terms)}): ")

    if term in terms:
      value = input(f"Enter value for {term}: ")
      dork = f"{term} {value}"

  if not dork:
    print("Invalid dork query constructed!")
  else:
    print(f"Dork query: {dork}")
  
  return dork

# Selenium driver
driver = webdriver.Chrome()

# Single thread executor
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

# Simplified email regex  
EMAIL_REGEX = r'\w+@\w+\.\w+'

def dork_search(query):

  results = []

  search_url = f'https://www.google.com/search?q={query}'
  driver.get(search_url)

  soup = BeautifulSoup(driver.page_source, 'html.parser')

  for result in soup.select('.g')[:10]:
    data = parse_result(driver, result)
    results.append(data)

  return results

def parse_result(driver, result):

  title = result.select_one('h3').text
  snippet = result.select_one('.VwiC3b').text

  driver.get(result.a['href'])
  content = driver.page_source

  emails = re.findall(EMAIL_REGEX, content)

  data = {
    'title': title,
    'snippet': snippet, 
    'emails': emails
  }

  return data

if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument("-q", "--query", help="Search query")
  args = parser.parse_args()

  if args.query:
    dork = args.query
  else:
    dork = build_dork()

  results = dork_search(dork)

  print(json.dumps(results, indent=2))
