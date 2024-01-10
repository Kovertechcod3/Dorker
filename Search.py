import concurrent.futures
import re
import json
import redis
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import docker

# Multithreading executor
executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)  

# Redis cache
redis_cache = redis.Redis(host='localhost', port=6379, db=0)

# Regex for data extraction
EMAIL_REGEX = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
SSN_REGEX = r'\d{3}-?\d{2}-?\d{4}'

# Selenium browser docker container
chrome_container = docker.from_env().containers.run("selenium/standalone-chrome", detach=True)

def dork_search(query):

  # Check cache    
  if redis_cache.exists(query):
    return json.loads(redis_cache.get(query))
  
  results = []  

  # Headless Chrome options
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--no-sandbox")

  # Initialize Chrome browser
  driver = webdriver.Remote(command_executor=chrome_container.id, options=chrome_options)

  # Perform search
  search_url = f'https://www.google.com/search?q={query}'
  driver.get(search_url)  

  # Parse results
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  for result in soup.select('.g'):
      
    # Extract info from each page
    data = parse_result(driver, result)
    results.append(data)

  # Cache for 12 hours
  serialized_results = json.dumps(results)
  redis_cache.set(query, serialized_results, ex=43200)

  return results

def parse_result(driver, result):

  # Get title, link, snippet
  title = result.select_one('h3').text
  link = result.select_one('a')['href']
  snippet = result.select_one('.VwiC3b').text

  # Retrieve page content  
  driver.get(link)
  content = driver.page_source

  # Extract email, SSN  
  emails = re.findall(EMAIL_REGEX, content)
  ssns = re.findall(SSN_REGEX, content)

  data = {
    'title': title,
    'link': link, 
    'snippet': snippet,
    'emails': emails,
    'ssns': ssns
  }

  return data
  
# Sample usage  
future = executor.submit(dork_search, 'intext:"admin" inurl:"php"')
results = future.result()

print(json.dumps(results, indent=2))
