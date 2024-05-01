pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Get the current branch name
                    def currentBranch = env.BRANCH_NAME
                    // Get the branch name from the Jenkinsfile path
                    def jenkinsfileBranch = getCurrentJenkinsfileBranch(env.JOB_NAME)
                    // Compare branch names
                    if (currentBranch == jenkinsfileBranch) {
                        // Checkout code only if branch names match
                        checkout scm
                    } else {
                        error "Jenkinsfile is not in the same branch as the Jenkins pipeline. Jenkinsfile branch: ${jenkinsfileBranch}, Current branch: ${currentBranch}"
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

def getCurrentJenkinsfileBranch(jobName) {
    // Assuming Jenkinsfile path is like 'folder/branch/Jenkinsfile'
    def parts = jobName.split('/')
    return parts.size() > 1 ? parts[-2] : 'master' // Assuming 'master' as default branch if Jenkinsfile is at the root
}
