import os
import json
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Load configuration from json
config_file = 'config.json'
with open(config_file) as f:
  CONFIG = json.load(f)

# URLs
BASE_URL = CONFIG.get('base_url')  
if not BASE_URL:
  logging.error("Base URL not specified in config")
  raise Exception("Base URL is required")

# Paths
DORKS_FILE = CONFIG.get('dorks_file')
if not DORKS_FILE:
  logging.error("Dorks file path not specified")
  raise Exception("Dorks file path is required")

DORKS_FILE = os.path.join(CONFIG.get('data_dir'), DORKS_FILE)

# Headers
HEADERS = CONFIG.get('headers')
if not HEADERS:
  logging.error("Headers not specified")
  HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Logging level  
LOG_LEVEL = CONFIG.get('log_level', logging.INFO)
logging.basicConfig(level=LOG_LEVEL)

# Validate config  
validate_config(CONFIG)
