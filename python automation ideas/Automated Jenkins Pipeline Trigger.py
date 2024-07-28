import requests

def trigger_jenkins_build(job_name, jenkins_url, jenkins_user, jenkins_token):
    url = f"{jenkins_url}/job/{job_name}/build"
    response = requests.post(url, auth=(jenkins_user, jenkins_token))
    if response.status_code == 201:
        print(f"Successfully triggered Jenkins job: {job_name}")
    else:
        print(f"Failed to trigger Jenkins job: {job_name}, status code: {response.status_code}")

if __name__ == "__main__":
    trigger_jenkins_build("Microservices-Build", "http://jenkins.example.com", "jenkins_user", "jenkins_token")
