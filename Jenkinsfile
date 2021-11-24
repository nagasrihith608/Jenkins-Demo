pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/aditya-k-7/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Difference.py"
                sh "./Difference.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
