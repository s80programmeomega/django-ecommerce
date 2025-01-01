pipeline {
    agent any
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 5, unit: 'SECONDS')
    }
    stages {
        stage('build') {
            steps {
                echo 'Building the application ...'
            }
        }
        stage('test') {
            steps {
                echo 'Testing the applcation ...'
            }
        }
        stage('deploy') {
            steps {
                echo 'Deploying the application ...'
            }
        }
    }
}