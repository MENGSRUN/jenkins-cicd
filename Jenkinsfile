pipeline {
    agent { 
        node {
            label 'docker-agent-python'
        }
    }

    triggers {
        pollSCM '* * * * *'
    }

    environment {
        PYTHON_BIN = "python3.11"  // Use Python 3.11
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

                # Remove old venv if it exists
                rm -rf venv

                # Create fresh virtual environment using Python 3.11
                ${PYTHON_BIN} -m venv venv

                # Upgrade pip in the venv
                venv/bin/pip install --upgrade pip

                # Force reinstall dependencies (Fire 0.6.0 compatible)
                venv/bin/pip install --no-cache-dir --upgrade --force-reinstall fire==0.6.0 six termcolor
                '''
            }
        }

        stage('Verify Installation') {
            steps {
                sh '''
                cd myapp
                echo "Installed packages in venv:"
                venv/bin/pip list
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                cd myapp

                # Run Python scripts using venv interpreter
                venv/bin/python hello.py
                venv/bin/python hello.py --name=SRUNNOOBIE
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
            echo "Cleaning old virtual environment..."
            sh 'rm -rf myapp/venv'
        }
    }
}
