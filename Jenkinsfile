pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Get the current branch name
                    def currentBranch = scm.branches[0].name
                    currentBranch = currentBranch.substring(currentBranch.lastIndexOf('/') + 1)

                    // Check if the Jenkinsfile branch (master) matches the build branch
                    if (currentBranch != 'master') {
                        error "Branch name mismatch! Build branch is '$currentBranch' but Jenkinsfile branch is 'master'."
                        // Stop further execution if branch names don't match
                        return
                    }
                    
                    // Checkout code since branch names match (assuming 'master')
                    git branch: 'master', // Assuming your Jenkinsfile is on 'master' branch
                        credentialsId: 'git-cred',
                        url: 'https://github.com/Aesha001/Pacific_Project'
                }
            }
        }
        // Add your other pipeline stages here (e.g., Get Approval, Build Docker Image)
        stage('Get Approval') {
            steps {
                input(message: 'Please approve this build.', submitter: 'divyesh')
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
