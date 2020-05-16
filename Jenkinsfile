node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        echo "Building code in branch ${env.gitlabSourceBranch}"
        sh 'printenv'
        app = docker.build("djangobasic:${env.BUILD_ID}", "./app/")
    }

    stage('Test Code Quality') {
        echo "Testing code quality with flake8"
        app.inside {
            sh 'flake8 --ignore E501 app/'
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

    if (env.gitlabSourceBranch == 'develop') {
        stage('Clear old version') {
            echo "Running source code in a fully containerized environment..."    
            sh '/usr/local/bin/docker-compose down -v'
        }

        stage('Deploy Source Code in Develop Environment') {
            echo "Running source code in a fully containerized environment..."    
            sh '/usr/local/bin/docker-compose up -d --build'
        }
    } 

    if (env.gitlabSourceBranch == 'master') {
        stage('Clear old version') {
            echo "Running source code in a fully containerized environment..."    
            sh '/usr/local/bin/docker-compose down -v'
        }

        stage('Deploy Source Code in Product Environment') {
            echo "Running source code in a fully containerized environment..."    
            sh '/usr/local/bin/docker-compose up -d --build'
        }
    }
    
}