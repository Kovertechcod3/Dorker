import os
import shutil
import configparser
import logging

CONFIG_FILE = 'deploy.conf'

def setup_logging():
    logging.basicConfig(filename='deploy.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config['deploy']

def validate_config(config):
    required_fields = ['copy', 'dir']
    for field in required_fields:
        if field not in config or not config[field]:
            logging.error(f"'{field}' is missing or empty in the configuration")
            raise ValueError(f"'{field}' is required in the configuration")

def deploy_application(deploy_dir):
    try:
        if not os.path.exists(deploy_dir):
            os.makedirs(deploy_dir)

        cfg = load_config()

        copy_list = [f.strip() for f in cfg.get('copy', '').split(',')]
        for f in copy_list:
            if os.path.isfile(f):
                shutil.copy(f, deploy_dir)
            else:
                logging.warning(f"File '{f}' not found. Skipping copy.")

        source_dir = cfg.get('source_dir')
        if source_dir:
            if os.path.isdir(source_dir):
                shutil.copytree(source_dir, os.path.join(deploy_dir, 'source'))
            else:
                logging.warning(f"Source directory '{source_dir}' not found. Skipping copy.")

        logging.info("Deployment completed successfully")

    except (OSError, ValueError) as e:
        logging.error(f"Deployment failed: {e}")

def cleanup(deploy_dir):
    try:
        shutil.rmtree(deploy_dir, ignore_errors=True)
        logging.info("Cleanup completed successfully")
    except OSError as e:
        logging.error(f"Cleanup failed: {e}")

if __name__ == '__main__':
    setup_logging()
    config = load_config()
    deploy_dir = config.get('dir', 'deploy')

    validate_config(config)
    deploy_application(deploy_dir)

    # test cleanup
    # cleanup(deploy_dir)
