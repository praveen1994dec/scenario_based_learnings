import subprocess

def deploy_application():
    # Pull latest code
    subprocess.run(["git", "pull", "origin", "main"])
    # Install dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    # Restart the application service
    subprocess.run(["systemctl", "restart", "myapp.service"])
    print("Deployment completed successfully.")

if __name__ == "__main__":
    deploy_application()
