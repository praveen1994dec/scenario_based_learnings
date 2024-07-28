import subprocess

def run_sonarqube_analysis(project_key, project_name, project_version, sonar_host, sonar_login):
    subprocess.run([
        "sonar-scanner",
        f"-Dsonar.projectKey={project_key}",
        f"-Dsonar.projectName={project_name}",
        f"-Dsonar.projectVersion={project_version}",
        f"-Dsonar.host.url={sonar_host}",
        f"-Dsonar.login={sonar_login}"
    ])
    print("SonarQube analysis completed.")

if __name__ == "__main__":
    run_sonarqube_analysis("my-project-key", "My Project", "1.0", "http://sonarqube.example.com", "sonar_token")
