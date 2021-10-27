pipeline {
  agent any
  environment {
    SONAR_TOKEN=credentials('sonar_token2')
  }
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
          // sh 'python -m pytest -vv --cov=app ./CONVERT_SERVICE/convert_service/convert_app/test/test_ffmpeg_execute.py'
          dir('CONVERT_SERVICE/convert_service') {
          sh 'python -m pytest -r ./convert_app/test/test_ffmpeg_execute.py'
          sh 'python -m pytest --html=../../report.html -s'

        }
      }
      post {
        always {
          archiveArtifacts artifacts: 'report.html', followSymlinks: false
        }
      }
    }
    stage('CodeQuality') {
      steps {
        sh "/var/jenkins_home/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner   -Dsonar.organization=latam02-cv   -Dsonar.projectKey=convert-video   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io"
        }
    }
    stage('QualityGates') {
      steps {
        sh 'echo get the compute results: Failed/Passed for your scanned project'
        }
    } 
  }
}


          