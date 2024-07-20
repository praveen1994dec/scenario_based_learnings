pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your/repository.git'
            }
        }
        
        stage('Deploy with Rollback') {
            steps {
                sh './deploy.sh --rollback-on-failure'
            }
        }
    }
}
