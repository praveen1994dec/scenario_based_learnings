import subprocess

def deploy_to_eks(kubeconfig_path, deployment_file):
    # Set the KUBECONFIG environment variable
    subprocess.run(["export", f"KUBECONFIG={kubeconfig_path}"], shell=True)
    
    # Apply the Kubernetes deployment file
    subprocess.run(["kubectl", "apply", "-f", deployment_file])
    print("Deployment applied to EKS.")

if __name__ == "__main__":
    deploy_to_eks("/path/to/kubeconfig", "deployment.yaml")
