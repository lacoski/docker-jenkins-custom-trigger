node {
    def app

    stage('Clone repository') {
        updateGitlabCommitStatus(name: 'Start Clone repository', state: 'running')
        checkout scm
        updateGitlabCommitStatus(name: 'Start Clone repository', state: 'success')
    }

    stage('Build image') {
        try {
            updateGitlabCommitStatus(name: 'Build image', state: 'running')
            echo "Building code in branch ${env.gitlabSourceBranch}"
            sh 'printenv'
            app = docker.build("djangobasic:${env.BUILD_ID}", "./app/")
            updateGitlabCommitStatus(name: 'Build image', state: 'success')
        } catch (ex) {
            updateGitlabCommitStatus(name: 'Build image', state: 'failed')
            error ex
        }
    }

    stage('Test Code Quality') {
        try {
            updateGitlabCommitStatus(name: 'Test Code Quality', state: 'running')
            echo "Testing code quality with flake8"
            app.inside {
                sh 'flake8 --ignore E501 app/'
            }
            updateGitlabCommitStatus(name: 'Test Code Quality', state: 'success')
        } catch (ex) {
            updateGitlabCommitStatus(name: 'Test Code Quality', state: 'failed')
            error ex
        }
    }

    stage('Test Django') {
        try {
            updateGitlabCommitStatus(name: 'Test Django', state: 'running')
            echo "Testing source code Django"
            app.inside {
                dir ('app') { 
                    sh 'python manage.py test'
                }
            }
            updateGitlabCommitStatus(name: 'Test Django', state: 'success')
        } catch (ex) {
            updateGitlabCommitStatus(name: 'Test Django', state: 'failed')
            error ex
        }
    }

    if (env.gitlabActionType == 'PUSH'){
        if (env.gitlabSourceBranch == 'develop') {
            try {
                stage('Clear old version') {
                    updateGitlabCommitStatus(name: 'Deploy Django Development', state: 'running')
                    echo "Running source code in a fully containerized environment..."    
                    sh '/usr/local/bin/docker-compose down -v --remove-orphans'
                }

                stage('Deploy Source Code in Develop Environment') {
                    echo "Running source code in a fully containerized environment..."    
                    sh '/usr/local/bin/docker-compose up -d --build'
                    updateGitlabCommitStatus(name: 'Deploy Django Development', state: 'success')
                }
            } catch (ex) {
                updateGitlabCommitStatus(name: 'Deploy Django Development', state: 'failed')
                error ex
            }
        }

        if (env.gitlabSourceBranch == 'master') {
            try {
                stage('Clear old version') {
                    updateGitlabCommitStatus(name: 'Deploy Django Production', state: 'running')
                    echo "Running source code in a fully containerized environment..."    
                    sh '/usr/local/bin/docker-compose -f docker-compose.prod.yml down -v --remove-orphans'
                }

                stage('Deploy Source Code in Product Environment') {
                    echo "Running source code in a fully containerized environment..."    
                    sh '/usr/local/bin/docker-compose -f docker-compose.prod.yml up -d --build'
                    updateGitlabCommitStatus(name: 'Deploy Django Production', state: 'success')
                }
            } catch (ex) {
                updateGitlabCommitStatus(name: 'Deploy Django Production', state: 'failed')
                error ex
            }
        }
    }
}
