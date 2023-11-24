import os
import shutil


def deploy_application():
    # Create a deployment directory
    deployment_dir = "deployment"
    os.makedirs(deployment_dir, exist_ok=True)

    # Copy necessary files to the deployment directory
    shutil.copy("main_script.py", deployment_dir)
    shutil.copy("preprocessing.py", deployment_dir)
    shutil.copy("search.py", deployment_dir)
    shutil.copy("processing.py", deployment_dir)

    # Any additional files or resources needed can be copied here

    print("Application deployed successfully.")


def cleanup_deployment():
    # Remove the deployment directory
    deployment_dir = "deployment"
    shutil.rmtree(deployment_dir, ignore_errors=True)

    print("Deployment directory cleaned up.")


if __name__ == "__main__":
    deploy_application()
