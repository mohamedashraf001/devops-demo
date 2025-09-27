pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'mohamedashraf001'
        DOCKER_HUB_CREDENTIALS = 'docker-hub-creds'  
        KUBECONFIG = '/home/mohamed/.kube/config'   
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mohamedashraf001/devops-demo.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_HUB_USER/fastapi:latest -f backend/Dockerfile ./backend'
                    sh 'ls -l client/'
                    sh 'docker build -t mohamedashraf001/angular:latest -f ./client/Dockerfile ./client'

                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS, passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push $DOCKER_HUB_USER/fastapi:latest"
                        sh "docker push $DOCKER_HUB_USER/angular:latest"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f infra/k8s/'
                }
            }
        }
    }
}
