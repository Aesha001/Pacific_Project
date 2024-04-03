pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', // Update with your branch name
                   credentialsId: 'JK-Cred', // Replace with your credential ID
                   url: 'https://github.com/Aesha001/Pacific_Project' // Replace with your repository URL
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ptt-project-img ./' // Replace with your image name
            }
        }
        stage('Run Tests (Optional)') {
            steps {
                // Add commands to run your Django tests here inside the container
                // Example: docker run your-django-app-image python manage.py test
            }
        }
    }
}

