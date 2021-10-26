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
          sh 'add-apt-repository ppa:jonathonf/ffmpeg-4'
          sh 'apt-get update'
          sh 'apt install ffmpeg'
          sh 'ffmpeg -version'
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


          