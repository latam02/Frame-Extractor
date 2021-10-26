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
          sh 'pip install -r CONVERT_SERVICE/requeriments.txt'
          sh 'ls -la /tmp/reports/'
          sh 'touch /tmp/reports/filereport'
      }
      //post {
        //always {
          //archiveArtifacts 'requirements.txt'
        //}
      //}
    }
  }
}