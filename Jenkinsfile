node {
  stage('SCM') {
	git 'https://github.com/matthew-wottrich-sonarsource/wottrich.git'
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv(https://wott.ngrok.io/) {
      sh "/Users/matthew.wottrich/Documents/sonar-scanner-4.7.0.2747-macosx/bin/sonar-scanner"
    }
  }
}
