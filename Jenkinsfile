node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def Users/matthew.wottrich/Documents/sonar-scanner-4.7.0.2747-macosx/bin/sonar-scanner = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "Users/matthew.wottrich/Documents/sonar-scanner-4.7.0.2747-macosx/bin/sonar-scanner"
    }
  }
}
