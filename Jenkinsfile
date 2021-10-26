pipeline {
  agent any
  environment {
    HOST_WORKSPACE = '${WORKSPACE}'
  }
  stages {
    stage('UnitTest') {
      agent {
        docker { 
          image 'crgv/python-c:3.8.12'
          args '-v ${HOST_WORKSPACE}:/tmp/reports --user jenkins'
          }
      }
      steps { 
          sh 'echo ${HOST_WORKSPACE}'
          sh 'pip install -r CONVERT_SERVICE/requirements.txt'
          sh 'ffmpeg -version'
          sh 'python -m pytest ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
          sh 'ls -la /tmp/reports/'
          sh 'sudo touch /tmp/reports/filereport'
      }
    }
  }
}