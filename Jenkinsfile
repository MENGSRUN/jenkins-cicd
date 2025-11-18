pipeline {
    agent { 
        node {
            label 'docker-agent-python'
        }
    }

    triggers {
        pollSCM '* * * * *'
    }

    stages {

        stage('Checkout') {
            steps {
                // Checkout latest code
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                cd myapp

                # Remove old venv only
                rm -rf venv

                # Create fresh virtual environment
                python3 -m venv venv

                # Upgrade pip
                venv/bin/pip install --upgrade pip

                # Force uninstall any old Fire package in venv
                venv/bin/pip uninstall -y fire || true

                # Force reinstall dependencies
                venv/bin/pip install --no-cache-dir --upgrade --force-reinstall fire==0.6.0 six termcolor
                '''
            }
        }

        stage('Verify Installation') {
            steps {
                sh '''
                cd myapp
                venv/bin/python3 -m pip show fire
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                cd myapp
                venv/bin/python3 hello.py
                venv/bin/python3 hello.py --name=SRUNNOOBIE
                '''
            }
        }

        stage('Deliver') {
            steps {
                sh '''
                echo "Doing delivery tasks..."
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning old virtual environment only..."
            sh 'rm -rf myapp/venv'
        }
    }
}
