pipeline {
  agent any
  stages {
    stage('UnitTest') {
      agent {
        docker { image 'crgv/python-c:3.8.12' }
      }
      steps { 
          sh 'pip install -r CONVERT_SERVICE/requirements.txt'
          sh 'mkdir -p dir1/reports/html'
          sh 'echo reports > dir1/reports/html/index.html'
          sh 'ls -la ./**' 
      }
      post {
        always {
          archiveArtifacts 'dir1/reports/html'
        }
      }
    }
  }
}