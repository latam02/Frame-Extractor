pipeline {
  agent any
  stages {
    stage('UnitTest') {
      agent {
        docker { 
          image 'crgv/python-c:3.8.12'
          }
      }
      steps {
          // sh 'ffmpeg -version'
          sh 'pip install -r CONVERT_SERVICE/requirements.txt'
          sh 'python -m pytest ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
          sh 'echo new > report.html'
          sh 'ls -la'
      }
      post {
        always {
          archiveArtifacts artifacts: '**/*.html', followSymlinks: false
        }
      }
    }
  }
}


          