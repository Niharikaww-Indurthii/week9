pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t kubedemoapp:v1 ."
            }
        }

       
stage('Docker Login') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKERHUB_USER',
            passwordVariable: 'DOCKERHUB_TOKEN'
        )]) {
            bat 'echo %DOCKERHUB_TOKEN%| docker login -u "%DOCKERHUB_USER%" --password-stdin'
        }
    }
}


        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker tag kubedemoapp:v1 nihaaaa34/sample:kubeimage1"
                bat "docker push nihaaaa34/sample:kubeimage1"
            }
        }

stage('Deploy to Kubernetes') {
    steps {
        bat 'whoami'
        bat 'where kubectl'
        bat 'kubectl config current-context'
        bat 'kubectl cluster-info'
        bat 'kubectl get nodes'
    }
}

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}