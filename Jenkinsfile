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

                # remove old venv
                rm -rf venv

                # create new venv
                python3 -m venv venv

                # force upgrade pip
                venv/bin/pip install --upgrade pip

                # force reinstall all dependencies
                venv/bin/pip install --upgrade --force-reinstall -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                cd myapp

                # run python scripts using venv interpreter
                venv/bin/python3 hello.py
                venv/bin/python3 hello.py --name=Brad
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