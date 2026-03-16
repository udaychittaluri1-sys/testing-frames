pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/udaychittaluri1-sys/testing-frames.git'
            }
        }

        stage('Build Docker Containers') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Start Services') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose exec -T test pytest --html=reports/report.html'
            }
        }

        stage('Stop Containers') {
            steps {
                sh 'docker-compose down'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
        }
    }
}
