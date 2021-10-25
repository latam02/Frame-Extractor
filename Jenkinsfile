pipeline {
  agent any
  stages {
    stage('Unit Test') {
      steps {
        sh 'pip install -r CONVERT_SERVICE/requirements.txt'
        // sh 'ffmpeg'
        // sh 'python -m pytest ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
      }
    }

  }
}