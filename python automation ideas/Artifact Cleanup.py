import requests
import json
from datetime import datetime, timedelta

def clean_old_artifacts(artifactory_url, repo, retention_days, artifactory_user, artifactory_password):
    cutoff_date = datetime.now() - timedelta(days=retention_days)
    response = requests.get(
        f"{artifactory_url}/api/storage/{repo}",
        auth=(artifactory_user, artifactory_password)
    )
    artifacts = response.json()["files"]
    for artifact in artifacts:
        artifact_date = datetime.strptime(artifact["created"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if artifact_date < cutoff_date:
            delete_url = f"{artifactory_url}/{repo}/{artifact['uri']}"
            requests.delete(delete_url, auth=(artifactory_user, artifactory_password))
            print(f"Deleted old artifact: {delete_url}")

if __name__ == "__main__":
    clean_old_artifacts("http://artifactory.example.com/artifactory", "libs-release-local", 30, "artifactory_user", "artifactory_password")
