pipeline {
  agent any
  stages {
    stage('Unit Test') {
      agent {
        docker {
          image 'python:3.8.12'
        }
      }
      steps {
        sh 'ls -la'
        sh 'pip --version'
        sh 'pip install -r requirements.txt'
        sh 'python -m pytest -vv --cov=app .\\CONVERT_SERVICE\\convert_service\\convert_app\\test\\test_ffmpeg_execute.py'
      }
    }

  }
}