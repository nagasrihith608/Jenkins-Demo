pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/nagasrihith608/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x build.py"
                sh "./build.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./test.py"
            }
        }
    } 
}
