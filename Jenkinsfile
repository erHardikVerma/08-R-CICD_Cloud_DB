pipeline {
    agent any

    stages {
        // Stage 1: Pull the latest code from GitHub
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/erHardikVerma/08-R-CICD_Cloud_DB.git'
            }
        }

        // Stage 2: Build the Docker container (the shipping box)
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ebg-backend .'
            }
        }

        // Stage 3: Smoke test - turn on the box and check if it's alive
        stage('Test Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name ebg-test ebg-backend'
                bat 'ping -n 6 127.0.0.1 > nul'
                bat 'docker logs ebg-test'
                bat 'docker stop ebg-test'
                bat 'docker rm ebg-test'
            }
        }
    }

    // Cleanup if anything fails mid-pipeline
    post {
        failure {
            bat 'docker stop ebg-test || exit 0'
            bat 'docker rm ebg-test || exit 0'
        }
        success {
            echo '✅ Pipeline completed successfully! Docker image ebg-backend is ready.'
        }
    }
}
