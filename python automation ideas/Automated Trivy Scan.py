import subprocess

def scan_docker_image(image_name):
    result = subprocess.run(["trivy", "image", image_name], capture_output=True, text=True)
    print(result.stdout)

    # Optionally, save scan report to a file
    with open("trivy_scan_report.txt", "w") as file:
        file.write(result.stdout)

if __name__ == "__main__":
    scan_docker_image("123456789012.dkr.ecr.us-west-2.amazonaws.com/microservice-repo:latest")
