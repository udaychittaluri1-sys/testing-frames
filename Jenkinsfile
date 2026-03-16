pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Containers') {
            steps {
                bat 'docker-compose build'
            }
        }

        stage('Start Services') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --html=reports/report.html'
            }
        }

        stage('Stop Containers') {
            steps {
                bat 'docker-compose down'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html'
        }
    }
}
