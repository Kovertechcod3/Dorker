import os
import shutil
import configparser

CONFIG_FILE = 'deploy.conf'

def load_config():
  config = configparser.ConfigParser()
  config.read(CONFIG_FILE)
  return config['deploy']
  
def deploy_application(deploy_dir):

  if not os.path.exists(deploy_dir):
    os.makedirs(deploy_dir)

  try:
    cfg = load_config()

    copy_list = [f.strip() for f in cfg.get('copy', '').split(',')]
    for f in copy_list:
      shutil.copy(f, deploy_dir)

    source_dir = cfg.get('source_dir')
    if source_dir:
      shutil.copytree(source_dir, os.path.join(deploy_dir, 'source'))

  except OSError as e:
    print("Deployment failed:", e)

def cleanup(deploy_dir):
  shutil.rmtree(deploy_dir, ignore_errors=True)
  
if __name__ == '__main__':

  cfg = load_config()
  deploy_dir = cfg.get('dir', 'deploy')

  deploy_application(deploy_dir)

  # test cleanup
  # cleanup(deploy_dir)
