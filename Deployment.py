"""
Deployment Module

Handles the deployment of application files and directories based on configuration settings.
"""

import os
import shutil
import configparser
import logging
from logging.handlers import RotatingFileHandler

CONFIG_FILE = os.getenv('DEPLOY_CONFIG_FILE', 'deploy.conf')

def setup_logging(log_file='deploy.log', log_level=logging.INFO):
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

def load_config(config_file=CONFIG_FILE):
    """Load deployment configuration from a file."""
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        logging.error(f"Config file '{config_file}' not found")
        raise FileNotFoundError(f"Config file '{config_file}' not found")

    config.read(config_file)
    
    if 'deploy' not in config:
        logging.error("Missing 'deploy' section in configuration")
        raise ValueError("Configuration must contain a 'deploy' section")
    
    return config['deploy']

def validate_config(config):
    """Validate the deployment configuration for required fields."""
    required_fields = ['copy', 'deploy_dir']
    for field in required_fields:
        if field not in config or not config[field]:
            logging.error(f"'{field}' is missing or empty in the configuration")
            raise ValueError(f"'{field}' is required in the configuration")

def deploy_application(deploy_dir):
    """Deploy application files and directories to the specified directory."""
    try:
        if not os.path.exists(deploy_dir):
            os.makedirs(deploy_dir)

        cfg = load_config()

        copy_list = [f.strip() for f in cfg.get('copy', '').split(',') if f.strip()]
        for f in copy_list:
            if os.path.isfile(f):
                shutil.copy(f, deploy_dir)
                logging.info(f"Copied '{f}' to '{deploy_dir}'")
            else:
                logging.warning(f"File '{f}' not found. Skipping copy.")

        source_dir = cfg.get('source_dir')
        if source_dir:
            if os.path.isdir(source_dir):
                shutil.copytree(source_dir, os.path.join(deploy_dir, 'source'))
                logging.info(f"Copied directory '{source_dir}' to '{os.path.join(deploy_dir, 'source')}'")
            else:
                logging.warning(f"Source directory '{source_dir}' not found. Skipping copy.")

        logging.info("Deployment completed successfully")

    except (OSError, ValueError) as e:
        logging.error(f"Deployment failed: {e}")

def cleanup(deploy_dir):
    """Clean up the deployment directory."""
    try:
        shutil.rmtree(deploy_dir, ignore_errors=True)
        logging.info("Cleanup completed successfully")
    except OSError as e:
        logging.error(f"Cleanup failed: {e}")

def main():
    """Main function to set up logging, load, and validate configuration, and deploy application."""
    setup_logging()
    try:
        config = load_config()
        deploy_dir = config.get('deploy_dir', 'deploy')

        validate_config(config)
        deploy_application(deploy_dir)

        # Uncomment the following line to test cleanup
        # cleanup(deploy_dir)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
