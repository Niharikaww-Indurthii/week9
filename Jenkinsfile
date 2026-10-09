
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
                bat 'docker login -u nihaaaa34 -p Niharika@30'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                bat "docker tag kubedemoapp:v1 nihaaaa34/sample:kubeimage1"

                bat "docker push nihaaaa34/sample:kubeimage1"
            }
        }

    
stage('Deploy to Kubernetes') {
    steps {
        bat 'kubectl --kubeconfig "C:\\Windows\\System32\\config\\systemprofile\\.kube\\config" config current-context'
        bat 'kubectl --kubeconfig "C:\\Windows\\System32\\config\\systemprofile\\.kube\\config" get nodes'
        bat 'kubectl --kubeconfig "C:\\Windows\\System32\\config\\systemprofile\\.kube\\config" apply -f deployment.yaml'
        bat 'kubectl --kubeconfig "C:\\Windows\\System32\\config\\systemprofile\\.kube\\config" apply -f service.yaml'
        bat 'kubectl --kubeconfig "C:\\Windows\\System32\\config\\systemprofile\\.kube\\config" rollout status deployment/kubedemoapp-deployment'
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
