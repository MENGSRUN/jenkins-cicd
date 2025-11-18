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

                # remove old venv only
                if [ -d "venv" ]; then
                    rm -rf venv
                fi

                # create fresh venv
                python3 -m venv venv

                # activate venv
                . venv/bin/activate

                # upgrade pip
                pip install --upgrade pip

                # install dependencies
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp

                # run without activate
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