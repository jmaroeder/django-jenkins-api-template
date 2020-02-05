def composeImageName
def imageTag
def targetImageName

pipeline {
    environment {
        COMPOSE_CONTAINER = 'web'
        COMPOSE_DEPLOYABLE_CONTAINER = 'web-deployable'
        COMPOSE_FILE = 'docker-compose.yml:docker-compose.ci.yml'
        COMPOSE_PROJECT_NAME = sh(returnStdout: true, script: 'printf "$BUILD_TAG" | sed -e "s|/|-|g"').trim()
    }

    options {
        ansiColor('xterm')
        skipStagesAfterUnstable()
    }

    stages {
        stage('Build') {
             steps {
                sh 'docker-compose --no-ansi build'
            }
        }
        stage('Static analysis') {
            steps {
                sh 'docker-compose --no-ansi run --no-deps --rm web bin/static_analysis.sh'
            }
            post {
                always {
                    sh 'docker-compose rm --force --stop -v'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose up -d db'
                sh 'docker-compose run --rm wait'
                sh 'docker-compose --no-ansi run --rm web bin/test.sh'
            }
            post {
                always {
                    junit 'test-results/junit.xml'
                    sh 'docker-compose rm --force --stop -v'
                }
            }
        }
        stage('Push') {
            // ...
        }
        stage('Deploy') {
            // ...
        }
    }
}
