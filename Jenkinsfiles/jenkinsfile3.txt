pipeline {
    agent any
    
    stages {
        stage('Database Migrations') {
            steps {
                sh './migrate-db.sh'
            }
        }
    }
}
