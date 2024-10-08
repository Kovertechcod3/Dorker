"""
My Application Package

Provides modules for scraping, processing, and deploying data.
"""

__version__ = "1.0.0"

import logging
import os
import json
from logging.handlers import RotatingFileHandler
from .preprocessing import preprocess_dorks
from .search import scrape_google_search
from .processing import perform_keyword_search
from .deployment import deploy_application, cleanup_deployment

__all__ = [
    'preprocess_dorks',
    'scrape_google_search',
    'perform_keyword_search',
    'deploy_application',
    'cleanup_deployment'
]

def setup_logging(log_file='application.log', log_level=logging.INFO):
    """Set up logging with file rotation and console output."""
    logger = logging.getLogger(__name__)
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

def load_config(config_file='config.json'):
    """Load configuration from a JSON file."""
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

def main():
    """Main function to execute the application workflow."""
    # Load configuration
    config = load_config()
    log_file = config.get('log_file', 'application.log')
    log_level = config.get('log_level', logging.INFO)
    setup_logging(log_file=log_file, log_level=log_level)

    try:
        deploy_dir = config.get('deploy_dir', 'website')

        # Execute workflow
        logging.info("Starting preprocessing of dorks")
        dorks = preprocess_dorks()

        logging.info("Starting scraping of search results")
        search_results = scrape_google_search(dorks)

        logging.info("Starting keyword processing")
        keywords = perform_keyword_search(search_results)

        logging.info("Starting deployment")
        deploy_application(deploy_dir)

        logging.info(f"Version {__version__} - Workflow completed successfully")
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
