pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Extract') {
            steps {
                sh 'python3 extract.py'
            }
        }

        stage('Transform') {
            steps {
                sh 'python3 transform.py'
            }
        }

        stage('Load') {
            steps {
                sh 'python3 load.py'
            }
        }
    }

    post {
        success {
            echo 'ETL pipeline executed successfully.'
        }
        failure {
            echo 'ETL pipeline failed.'
        }
    }
}

