pipeline {
  agent any
  stages {
      agent {
        docker { 
          image 'crgv/python-c:3.8.12'
          args '--name python-c-ut'
          }
      }
    stage('Unit Test') {
      steps {
        sh 'pip install -r CONVERT_SERVICE/requirements.txt'
        sh 'echo /usr/bin/ffmpeg'
        sh 'python -m pytest ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
      }
    }

  }
}