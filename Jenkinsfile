pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build test image') {
            steps {
                sh 'docker build -t aqa-ui-tests:${BUILD_NUMBER} .'
            }
        }

        stage('Run UI tests') {
            steps {
                script {
                    // returnStatus не останавливает pipeline при падении теста.
                    // Отчёт Allure всё равно будет опубликован в блоке post.
                    int exitCode = sh(
                        script: '''
                            mkdir -p Action_Press/allure-results
                            docker run --rm \
                              --ipc=host \
                              -v "$WORKSPACE/Action_Press/allure-results:/app/Action_Press/allure-results" \
                              aqa-ui-tests:${BUILD_NUMBER}
                        ''',
                        returnStatus: true
                    )

                    if (exitCode != 0) {
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
    }

    post {
        always {
            // Путь указан относительно корня Jenkins workspace.
            // Плагин публикует отчёт и ведёт историю билдов этого job.
            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'Action_Press/allure-results']]
            )

            // Сохраняем исходные результаты как artifact на случай отладки.
            archiveArtifacts(
                artifacts: 'Action_Press/allure-results/**',
                allowEmptyArchive: true
            )
        }
    }
}