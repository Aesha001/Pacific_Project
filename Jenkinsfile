pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Get the current branch name
                    def currentBranch = scm.branches[0].name

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
                input(message: 'Please approve this build.', submitter: 'admin','divyesh')
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
