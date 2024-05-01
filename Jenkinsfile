pipeline {
    agent any
    stages {
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
                        // Alternatively, you can return here to stop further execution:
                        // return
                    }
                    
                    // Checkout code since branch names match (assuming 'master')
                    git branch: currentBranch, 
                        credentialsId: 'git-cred',
                        url: 'https://github.com/Aesha001/Pacific_Project'
                }
            }
        }
        // Add your other pipeline stages here (e.g., Get Approval, Build Docker Image)
    }
}

        stage('Get Approval') {
            steps {
                input('Please approve this.....')
            }
        }
        stage('Build Docker Image') {pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Get the current branch name
                    def currentBranch = 'master'
                    // Get the branch name from the Jenkinsfile path
                     def pipelineBranch = scm.branchSpecifier.toString()

                    // Compare branch names
                    if (currentBranch == pipelineBranch) {
                        // Checkout code only if branch names match
                        git branch: currentBranch, 
                            credentialsId: 'git-cred',
                            url: 'https://github.com/Aesha001/Pacific_Project'
                    } else {
                        error "Jenkinsfile is not in the same branch as the Jenkins pipeline."
                    }
                }
            }
        }
        stage('Get Approval') {
            steps {
                input(message: 'Please approve this build.', submitter: 'admin')
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
