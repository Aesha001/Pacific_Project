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
    }
}
