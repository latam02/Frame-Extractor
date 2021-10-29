pipeline {
  agent any
  environment {
    SONAR_TOKEN=credentials('sonar_token')
  }
  stages {
    stage('UnitTest') {
      agent {
        docker { 
          image 'crgv/python-c-ffmpeg:3.12.8'
          }
      }
      steps {
          sh 'pip install --upgrade pip'
          sh 'pip install -r CONVERT_SERVICE/requirements.txt --no-cache-dir'
          // sh 'python -m pytest -vv --cov=app ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
          dir('CONVERT_SERVICE/convert_service') {
          sh 'python -m pytest -r ./convert_app/test/test_ffmpeg_execute.py'
          sh 'python -m pytest --html=../../report.html -s'

        }
      }
      post {
        always {
          archiveArtifacts artifacts: 'report.html', followSymlinks: false
        }
      }
    }
    stage('CodeQuality') {
      steps {
        sh "/var/jenkins_home/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner   -Dsonar.organization=ffmpeg   -Dsonar.projectKey=FrameExtractor   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io"
        }
    }
    stage('QualityGates') {
      steps {
        sh 'echo get the compute results: Failed/Passed for your scanned project'
        }
    }
    //     stage('Package'){
    //   steps {
    //     sh 'docker build -t ${IMAGE_NAME}:${TAG_VERSION} .'
    //   }
    // }
    // stage('Publish'){
    //   steps {
    //     sh 'docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}'
    //     sh 'docker tag ${IMAGE_NAME}:${TAG_VERSION} crgv/${IMAGE_NAME}:${TAG_VERSION}'
    //     sh 'docker push crgv/${IMAGE_NAME}:${TAG_VERSION}'
    //   }
    // }
    // stage('Deploy'){
    //   steps {
    //     sh 'echo deploy'
    //   }
    // } 
  }
}


          