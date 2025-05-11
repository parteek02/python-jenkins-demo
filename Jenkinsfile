pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
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

        stage('Security Scan') {
            steps {
                sh './${VENV_DIR}/bin/bandit -r app'
            }
        }

        stage('Test & Coverage') {
            steps {
                sh './${VENV_DIR}/bin/pytest --cov=app --cov-report=xml'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Deploying...'
                sh 'echo "Deployment complete"'
            }
        }
    }

    post {
        success {
            mail to: 'parteeksandhey857@gmail.com',
                 subject: "SUCCESS: ${env.JOB_NAME}",
                 body: "Build succeeded: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'parteeksandhey857@gmail.com',
                 subject: "FAILURE: ${env.JOB_NAME}",
                 body: "Build failed: ${env.BUILD_URL}"
        }
    }
}

