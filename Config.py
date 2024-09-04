import os
import json
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='app.log', log_level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def load_config(config_file=None):
    if config_file is None:
        config_file = os.getenv('CONFIG_FILE', 'config.json')

    if not os.path.exists(config_file):
        logging.error(f"Config file '{config_file}' not found")
        raise FileNotFoundError(f"Config file '{config_file}' not found")
    
    try:
        with open(config_file) as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from config file '{config_file}': {e}")
        raise
    
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
    
    # Additional validation
    if not config['base_url'].startswith('http'):
        logging.error("Invalid base_url in configuration")
        raise ValueError("base_url must be a valid URL")
    
    if not os.path.isdir(config['data_dir']):
        logging.error("Invalid data_dir in configuration")
        raise ValueError("data_dir must be a valid directory path")

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
