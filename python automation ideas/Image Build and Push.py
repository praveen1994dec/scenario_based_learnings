import subprocess

def build_and_push_docker_image(repository_name, image_tag, aws_account_id, aws_region):
    ecr_url = f"{aws_account_id}.dkr.ecr.{aws_region}.amazonaws.com"
    image_name = f"{ecr_url}/{repository_name}:{image_tag}"
    
    # Build Docker image
    subprocess.run(["docker", "build", "-t", image_name, "."])
    
    # Authenticate Docker to ECR
    login_command = subprocess.run(
        ["aws", "ecr", "get-login-password", "--region", aws_region],
        capture_output=True, text=True
    ).stdout.strip()
    subprocess.run(["docker", "login", "--username", "AWS", "--password", login_command, ecr_url])
    
    # Push Docker image to ECR
    subprocess.run(["docker", "push", image_name])
    print(f"Docker image pushed: {image_name}")

if __name__ == "__main__":
    build_and_push_docker_image("microservice-repo", "latest", "123456789012", "us-west-2")
