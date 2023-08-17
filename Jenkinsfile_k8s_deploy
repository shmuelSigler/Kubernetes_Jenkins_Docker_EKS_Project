pipeline {
	agent{
		label 'build-agent'
	}

	stages {
		stage('Build'){
	    	steps{
	       		sh 'docker build -t weather_app .'
	    	}
		}
		stage('Delivery'){
            steps{
                script{
                   withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                   sh 'docker login -u sigler05 -p ${dockerhubpwd}'
					}
					sh '''
					docker tag weather_app sigler05/weather_app:k8s_deployment
                    docker push sigler05/weather_app:k8s_deployment
				   '''
                }
            }
        }
				
		stage('Read_deployment'){
			steps{
				script {
					if (fileExists('deployment.yml')) {
						def file = readFile(file: "deployment.yml") 
      					def deploymentYml = readYaml(text: file)
      					def dockerImageName = deploymentYml.spec.template.spec.containers[0].image
      					env.DOCKER_IMAGE_NAME = dockerImageName
						print env.DOCKER_IMAGE_NAME
					}
				}
				//echo "${env.DOCKER_IMAGE_NAME}"
			}
		}

		stage('Integrate Jenkins with EKS Cluster and Deploy App') {
            steps {
                withAWS(credentials: 'aws-credential', region: 'us-east-1') {
                  script {
                    sh ('aws eks update-kubeconfig --name my-EKS --region us-east-1')
                    sh "kubectl apply -f deployment.yml"
                }
                }
        }
		}	
	}
	
	 post{
			always{
				sh '''
				docker rmi weather_app
					docker rmi sigler05/weather_app:k8s_deployment
					'''
				
				cleanWs()
				dir("${env.WORKSPACE}@tmp") {
					deleteDir()
				}
				dir("${env.WORKSPACE}@script") {
				deleteDir()
				}
				dir("${env.WORKSPACE}@script@tmp") {
				deleteDir()
				}
			}
		}  
	 
}
