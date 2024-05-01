pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master',
                   credentialsId: 'git-cred',
                   url: 'https://github.com/Aesha001/Pacific_Project'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("ptt-project-img")
                }
            }
        }
  stage('Deploy Container') {
            steps {
                script {
                    // Run the Docker container from the built image
                    def container = docker.run("-d -p 8000:8000 --name pacific-container ptt-project-img")

                    // Output container ID for reference
                    echo "Container ID: ${container.id}"
                }
            }
        }
    }
}
