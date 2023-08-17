
# Integrate Jenkins with EKS Cluster and Deploy App with DevOps Pipeline


## Overview
This repository contains an extended version of the [Weather App DevOps project](https://github.com/shmuelSigler/Jenkins_Docker_Slack), showcasing additional features and enhancements. The project demonstrates my skills in Python development, Dockerization, Kubernetes deployment, Jenkins integration, and dynamic application configuration.

The project demonstrates the implementation of a Jenkins pipeline for building, deploying, and managing a Dockerized application on an EKS cluster. The application is made accessible externally using NGINX Ingress Controller.

![jenkins+k8s](https://raw.githubusercontent.com/shmuelSigler/Kubernetes_Jenkins_Docker_EKS_Project/main/kubernetes-jenkins.png)

![jenkins+k8s](https://raw.githubusercontent.com/shmuelSigler/Kubernetes_Jenkins_Docker_EKS_Project/e8272d1767426caaf87b59bf5bcdee0d52e5d0ae/eks.svg)

## Key Features
- **Automated Docker image build and push to Docker Hub.**
- **Deployment of the Docker image to an EKS cluster.**
- **Application access through Kubernetes Ingress.**
- **Jenkins pipeline integration.**

## Accomplishments
1. **Flask Web Application**: Developed a Flask-based web application that allows users to interact with the Weather App, enter search queries, and view weather forecasts and historical data.
2. **History Feature Implementation**: Designed and integrated a history feature that records user search queries and stores them in a JSON file. This allows users to review their past queries and weather data.
3. **Dynamic Background Color**: Demonstrated my understanding of dynamic app configuration by enabling users to configure the app's background color using the BG_COLOR environment variable during Docker image build.
4. **EKS Cluster Setup**: Successfully set up an Amazon EKS cluster to create a managed Kubernetes environment. This involved configuring and provisioning the necessary compute resources and networking components..
5. **Kubernetes Manifests**: Created a Kubernetes deployment manifest (deployment.yaml) that defines the desired state of your Weather App application. This manifest specified the number of replicas, container specifications, and other deployment-related settings.
6. **Integration with Jenkins**: In Jenkins pipeline, i integrated the deployment of my Weather App to the EKS cluster.

For detailed steps and code, refer to the [Jenkinsfile](https://github.com/shmuelSigler/Kubernetes_Jenkins_Docker_EKS_Project/blob/main/Jenkinsfile)
 in this repository.

## Project Architecture and Components

![Architecture](https://raw.githubusercontent.com/shmuelSigler/Kubernetes_Jenkins_Docker_EKS_Project/main/architecture.png)

- Executed a comprehensive project involving GitLab and Jenkins servers, showcasing my expertise in streamlining development workflows. 
- Developed and implemented a Jenkins pipeline for the Weather app, effectively integrating remote GitLab repositories. 
- Demonstrated proficiency in automating the build process by creating Docker images. 
- Successfully deployed the tested images to Docker Hub, emphasizing my ability to ensure reliable software delivery. 
- Successfully set up an Amazon EKS cluster to create a managed Kubernetes environment. This involved configuring and provisioning the necessary compute resources and networking components.



#### Contact
For any inquiries or questions, please reach out to yakovsig@gmail.com.

