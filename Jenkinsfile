pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\Users\chitt\AppData\Local\Programs\Python\Python311\python.exe" -m pip install --upgrade pip'
                bat '"C:\Users\chitt\AppData\Local\Programs\Python\Python311\python.exe" -m pip install -r requirements.txt'
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
                bat '"C:\Users\chitt\AppData\Local\Programs\Python\Python311\python.exe" -m pytest --html=reports/report.html'
            }
        }

        stage('Stop Services') {
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
