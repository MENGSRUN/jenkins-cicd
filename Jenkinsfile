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
                echo "Building.."
                sh '''
                cd myapp

                # Remove old virtual environment (only venv folder)
                rm -rf venv

                # Create fresh venv
                python3 -m venv venv

                # Activate venv and install
                . venv/bin/activate
                
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