pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                script {
                    git branch: 'master',
                        credentialsId: 'git-cred',
                        url: 'https://github.com/Aesha001/Pacific_Project'
                }
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
                    def container = docker.image("ptt-project-img").run("-d -p 8000:8000 --name pacific-container")
                    echo "Container ID: ${container.id}"
                }
            }
        }
    }
}
