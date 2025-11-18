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

        stage('Cleanup') {
            steps {
                echo "Cleaning workspace..."
                deleteDir()
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp

                # Create virtual environment
                python3 -m venv venv

                # Activate venv
                . venv/bin/activate

                # Install dependencies
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp

                # Activate the virtual environment for TEST stage
                . venv/bin/activate

                python3 hello.py
                python3 hello.py --name=Brad
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}