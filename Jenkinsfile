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

        stage('Clean Workspace') {
            steps {
                // Clean old workspace to avoid cached packages
                cleanWs()
            }
        }

        stage('Build') {
            steps {
                sh '''
                cd myapp

                # Remove old venv if it exists
                rm -rf venv

                # Create fresh virtual environment
                python3 -m venv venv

                # Upgrade pip
                venv/bin/pip install --upgrade pip

                # Force uninstall any old Fire package in venv (if any)
                venv/bin/pip uninstall -y fire || true

                # Force reinstall dependencies without cache
                venv/bin/pip install --no-cache-dir --upgrade --force-reinstall fire==0.6.0 six termcolor
                '''
            }
        }

        stage('Verify Installation') {
            steps {
                sh '''
                cd myapp

                # Verify Fire version
                venv/bin/python3 -m pip show fire

                # Should output: Version: 0.6.0
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Running Python scripts..."
                sh '''
                cd myapp

                # Run Python scripts using venv interpreter directly
                venv/bin/python3 hello.py
                venv/bin/python3 hello.py --name=SRUNNOOBIE
                '''
            }
        }

        stage('Deliver') {
            steps {
                echo 'Delivering...'
                sh '''
                echo "Doing delivery tasks..."
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace after build..."
            cleanWs()
        }
    }
}
