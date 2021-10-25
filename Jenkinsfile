pipeline {
  agent {
      docker { image 'python:3.8-slim' }
  }
  stages {
    stage('Unit Test') {
      steps {
        sh 'python -m pytest -vv --cov=app .\CONVERT_SERVICE\convert_service\convert_app\test\test_ffmpeg_execute.py'
      }
    }
    // post {
    //   always {
    //     archiveArtifacts 'dir1/reports/html'
    //   }
    // }

  }
}