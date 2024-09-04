import os
import json
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='app.log', log_level=logging.INFO):
    """Set up logging with file rotation and console output."""
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
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
    """Load configuration from a JSON file."""
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
    """Retrieve a configuration value with a default fallback."""
    value = config.get(key, default)
    if value is None:
        logging.warning(f"No value found for key '{key}' in config. Using default value '{default}'")
    return value

def validate_config(config):
    """Validate the configuration for required fields and correct formats."""
    required_fields = ['search_url', 'dorks_file', 'deploy_dir', 'headers']
    
    for field in required_fields:
        if field not in config or not config[field]:
            logging.error(f"{field} is missing or empty in the configuration")
            raise ValueError(f"{field} is required in the configuration")
    
    # Additional validation
    if not config['search_url'].startswith('http'):
        logging.error("Invalid search_url in configuration")
        raise ValueError("search_url must be a valid URL")
    
    if not os.path.isdir(config['deploy_dir']):
        logging.error("Invalid deploy_dir in configuration")
        raise ValueError("deploy_dir must be a valid directory path")

def main():
    """Main function to set up logging, load, and validate configuration."""
    # Set up logging
    config = load_config()
    log_file = get_config_value(config, 'log_file', 'app.log')
    log_level = get_config_value(config, 'log_level', logging.INFO)
    setup_logging(log_file=log_file, log_level=log_level)

    # Validate config
    validate_config(config)

    # Get configuration values
    search_url = get_config_value(config, 'search_url')
    dorks_file = get_config_value(config, 'dorks_file')
    deploy_dir = get_config_value(config, 'deploy_dir')
    headers = get_config_value(config, 'headers', default={'User-Agent': 'Mozilla/5.0'})
    
    # Example usage of configuration values
    dorks_file_path = os.path.join(deploy_dir, dorks_file)
    logging.info(f"Using search URL: {search_url}")
    logging.info(f"Dorks file path: {dorks_file_path}")

if __name__ == '__main__':
    main()
