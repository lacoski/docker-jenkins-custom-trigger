node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("djangobasic:${env.BUILD_ID}", "./app/")
    }

    stage('Run Test Django') {
        app.inside {
            dir ('app') { 
                sh 'python manage.py test'
            }
        }
    }

    stage('Clear old version') {
        echo "Running source code in a fully containerized environment..."    
        sh '/usr/local/bin/docker-compose down -v'
    }

    stage('Deploy Source Code') {
        echo "Running source code in a fully containerized environment..."    
        sh '/usr/local/bin/docker-compose up -d --build'
    }
}