pipeline {
    agent any

    environment {
        DOCKER_USER = "yourdockerhub"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/YOUR_USERNAME/three-tier-devops-project.git'
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker build -t $DOCKER_USER/frontend:latest ./frontend'
                sh 'docker build -t $DOCKER_USER/backend:latest ./backend'
            }
        }

        stage('Push Images') {
            steps {
                sh 'docker push $DOCKER_USER/frontend:latest'
                sh 'docker push $DOCKER_USER/backend:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
