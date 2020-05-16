node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        echo "Building branch ${env}"
        app = docker.build("djangobasic:${env.BUILD_ID}", "./app/")
    }

    stage('Test Code Quality') {
        echo "Testing code quality with flake8"
        app.inside {
            dir ('app') { 
                sh 'flake8 --ignore E501 app/'
            }
        }
    }

    stage('Test Django') {
        echo "Testing source code Django"
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