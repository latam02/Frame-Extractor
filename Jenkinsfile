pipeline {
  agent any
  stages {
    stage('Unit Test') {
      agent {
        docker { 
          image 'crgv/python-c:3.8.12'
          args '--name python-c-ut'
          }
      }
      steps {
        sh 'pip install -r CONVERT_SERVICE/requirements.txt'
        sh '$PATH:/usr/bin/ffmpeg'
        // sh 'python -m pytest ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
      }
    }

  }
}