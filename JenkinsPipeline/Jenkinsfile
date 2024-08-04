pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'kushagraag'
        DOCKER_IMAGE = "${DOCKER_REGISTRY}/todoapp:${BUILD_NUMBER}"
        TRIVY_CACHE_DIR = "${WORKSPACE}/trivy-cache"
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'git-token', url: 'https://github.com/kushagra023/new-todo.git'
            }
        }

        stage('Trivy Scan Filesystem') {
            steps {
                script {
                    sh '''
                    mkdir -p "${TRIVY_CACHE_DIR}"
                    trivy fs --cache-dir "${TRIVY_CACHE_DIR}" --exit-code 1 --severity HIGH,CRITICAL . || true
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            environment {
                scannerHome = tool 'sonarqube'
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh """
                    "${scannerHome}/bin/sonar-scanner" \
                    -Dsonar.projectKey=todoapp \
                    -Dsonar.projectName="todoapp" \
                    -Dsonar.projectVersion=1.0 \
                    -Dsonar.sources=.
                    """
                }
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                script {
                    sh '''
                    dependency-check --project todoapp --format "XML" --out dependency-check-report.xml --scan .
                    '''
                }
            }
            post {
                always {
                    dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Trivy Scan Docker Image') {
            steps {
                script {
                    sh '''
                    mkdir -p "${TRIVY_CACHE_DIR}"
                    trivy image --cache-dir "${TRIVY_CACHE_DIR}" --exit-code 1 --severity HIGH,CRITICAL "${DOCKER_IMAGE}" || true
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-cred') {
                        dockerImage.push('latest')
                        dockerImage.push("${BUILD_NUMBER}")
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    script {
                        sh '''
                        kubectl --kubeconfig="${KUBECONFIG}" apply -f deployment.yaml
                        kubectl --kubeconfig="${KUBECONFIG}" apply -f service.yaml
                        '''
                    }
                }
            }
        }

    }

    post {
        always {
            cleanWs()
        }
    }
}
