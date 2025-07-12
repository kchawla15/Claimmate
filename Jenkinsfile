pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python & Virtualenv') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh './venv/bin/python manage.py test'
            }
        }
        stage('Migrate & Collectstatic') {
            steps {
                sh './venv/bin/python manage.py migrate'
                sh './venv/bin/python manage.py collectstatic --noinput'
            }
        }
        stage('Stop Previous Server') {
            steps {
                sh 'pkill -f "manage.py runserver" || true'
            }
        }
        stage('Run Django Locally') {
            steps {
                sh 'nohup ./venv/bin/python manage.py runserver 0.0.0.0:8000 &'
            }
        }
    }
}
