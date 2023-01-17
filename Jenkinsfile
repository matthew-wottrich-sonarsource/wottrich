node {
  stage('SCM') {
	git 'https://github.com/matthew-wottrich-sonarsource/wottrich.git'
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv(https://wott.ngrok.io/) {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
