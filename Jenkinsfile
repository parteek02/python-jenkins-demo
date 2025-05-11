pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    tools {
        python 'Python3'
    }

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv ${VENV_DIR}'
                sh './${VENV_DIR}/bin/pip install --upgrade pip'
                sh './${VENV_DIR}/bin/pip install -r requirements-dev.txt'
            }
        }

        stage('Lint') {
            steps {
                sh './${VENV_DIR}/bin/flake8 app tests'
            }
        }

        stage('Static Analysis') {
            steps {
                sh './${VENV_DIR}/bin/bandit -r app'
            }
        }

        stage('Test') {
            steps {
                sh './${VENV_DIR}/bin/pytest --cov=app --cov-report=xml'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Deploying app...'
                // Simulate deployment
                sh 'echo "Deployment complete."'
            }
        }
    }

    post {
        success {
            mail to: 'parteek.sandhey@opstree.com',
                 subject: "SUCCESS: Jenkins Job ${env.JOB_NAME}",
                 body: "Job ${env.JOB_NAME} succeeded at ${env.BUILD_URL}"
        }

        failure {
            mail to: 'parteek.sandhey@opstree.com',
                 subject: "FAILURE: Jenkins Job ${env.JOB_NAME}",
                 body: "Job ${env.JOB_NAME} failed at ${env.BUILD_URL}"
        }
    }
}

