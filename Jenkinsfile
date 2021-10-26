pipeline {
  agent any
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
          sh 'python -m pytest -vv --cov=app ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
          sh 'echo new > report.html'
          sh 'ls -la'
      }
      post {
        always {
          archiveArtifacts artifacts: '**/report.html', followSymlinks: false
        }
      }
    }
  }
}


          