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

        stage('Build') {
            steps {
                sh '''
                cd myapp

                # Remove old venv if any
                rm -rf venv

                # Create fresh venv
                python3 -m venv venv

                # Upgrade pip
                venv/bin/pip install --upgrade pip

                # Force reinstall dependencies to ensure correct versions
                venv/bin/pip install --upgrade --force-reinstall fire==0.6.0 six termcolor
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Running Python scripts..."
                sh '''
                cd myapp

                # Run scripts using venv interpreter directly (no activate needed)
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
