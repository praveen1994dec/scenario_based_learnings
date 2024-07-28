import subprocess

def scale_kubernetes_deployment(deployment_name, namespace, replicas):
    subprocess.run([
        "kubectl", "scale", f"--replicas={replicas}",
        "deployment", deployment_name, 
        f"--namespace={namespace}"
    ])
    print(f"Scaled deployment {deployment_name} to {replicas} replicas")

if __name__ == "__main__":
    scale_kubernetes_deployment("my-microservice", "default", 5)
