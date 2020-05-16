node {
    def app

    stage('Clone repository') {
        updateGitlabCommitStatus(name: 'Start Clone repository', state: 'running')
        checkout scm
        updateGitlabCommitStatus(name: 'Start Clone repository', state: 'success')
    }

    stage('Build image') {
        updateGitlabCommitStatus(name: 'Build image', state: 'running')
        echo "Building code in branch ${env.gitlabSourceBranch}"
        sh 'printenv'
        app = docker.build("djangobasic:${env.BUILD_ID}", "./app/")
        updateGitlabCommitStatus(name: 'Build image', state: 'success')
    }

    stage('Test Code Quality') {
        updateGitlabCommitStatus(name: 'Test Code Quality', state: 'running')
        echo "Testing code quality with flake8"
        app.inside {
            sh 'flake8 --ignore E501 app/'
        }
        updateGitlabCommitStatus(name: 'Test Code Quality', state: 'success')
    }

    stage('Test Django') {
        updateGitlabCommitStatus(name: 'Test Django', state: 'running')
        echo "Testing source code Django"
        app.inside {
            dir ('app') { 
                sh 'python manage.py test'
            }
        }
        updateGitlabCommitStatus(name: 'Test Django', state: 'success')
    }

    if (env.gitlabActionType == 'PUSH'){
        // stage('Clear all container') {
        //     sh '/usr/bin/docker container stop $(docker container ls -aq)'
        //     sh '/usr/bin/docker container rm $(docker container ls -aq)'
        // }
        if (env.gitlabSourceBranch == 'develop') {
            stage('Clear old version') {
                updateGitlabCommitStatus(name: 'Deploy Django Development', state: 'running')
                echo "Running source code in a fully containerized environment..."    
                sh '/usr/local/bin/docker-compose down -v'
            }

            stage('Deploy Source Code in Develop Environment') {
                echo "Running source code in a fully containerized environment..."    
                sh '/usr/local/bin/docker-compose up -d --build'
                updateGitlabCommitStatus(name: 'Deploy Django Development', state: 'success')
            }
        }

        if (env.gitlabSourceBranch == 'master') {
            stage('Clear old version') {
                updateGitlabCommitStatus(name: 'Deploy Django Production', state: 'running')
                echo "Running source code in a fully containerized environment..."    
                sh '/usr/local/bin/docker-compose -f docker-compose.prod.yml down -v'
            }

            stage('Deploy Source Code in Product Environment') {
                echo "Running source code in a fully containerized environment..."    
                sh '/usr/local/bin/docker-compose -f docker-compose.prod.yml up -d --build'
                updateGitlabCommitStatus(name: 'Deploy Django Production', state: 'success')
            }
        }
    }
}