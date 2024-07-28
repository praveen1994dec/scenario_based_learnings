import requests
from pathlib import Path

def upload_to_artifactory(artifact_path, artifactory_url, repo, artifactory_user, artifactory_password):
    file_path = Path(artifact_path)
    if file_path.is_file():
        with open(file_path, 'rb') as file:
            url = f"{artifactory_url}/{repo}/{file_path.name}"
            response = requests.put(url, data=file, auth=(artifactory_user, artifactory_password))
            if response.status_code == 201:
                print(f"Artifact uploaded: {url}")
            else:
                print(f"Failed to upload artifact: {url}, status code: {response.status_code}")
    else:
        print(f"File not found: {artifact_path}")

if __name__ == "__main__":
    upload_to_artifactory("target/my-app.jar", "http://artifactory.example.com/artifactory", "libs-release-local", "artifactory_user", "artifactory_password")
