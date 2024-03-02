import os
import json
import logging

def setup_logging(log_file='app.log', log_level=logging.INFO):
    logging.basicConfig(filename=log_file, level=log_level)

def load_config(config_file='config.json'):
    if not os.path.exists(config_file):
        logging.error(f"Config file '{config_file}' not found")
        raise FileNotFoundError(f"Config file '{config_file}' not found")
    
    with open(config_file) as f:
        config = json.load(f)
    
    return config

def get_config_value(config, key, default=None):
    value = config.get(key, default)
    if value is None:
        logging.warning(f"No value found for key '{key}' in config. Using default value '{default}'")
    return value

def validate_config(config):
    required_fields = ['base_url', 'dorks_file', 'data_dir', 'headers']
    
    for field in required_fields:
        if field not in config or not config[field]:
            logging.error(f"{field} is missing or empty in the configuration")
            raise ValueError(f"{field} is required in the configuration")

# Set up logging
setup_logging()

# Load configuration from json
config = load_config()

# Get URLs
base_url = get_config_value(config, 'base_url')
dorks_file = get_config_value(config, 'dorks_file')
data_dir = get_config_value(config, 'data_dir')
dorks_file_path = os.path.join(data_dir, dorks_file)

# Get headers
default_headers = {'User-Agent': 'Mozilla/5.0'}
headers = get_config_value(config, 'headers', default=default_headers)

# Get log level
log_level = get_config_value(config, 'log_level', default=logging.INFO)

# Validate config
validate_config(config)
