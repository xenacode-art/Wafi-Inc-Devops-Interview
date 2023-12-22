# DevOps Assessment Test

**Assignment: Setting up GKE and Deploying an Application**

**Objective:**

Your task is to demonstrate your proficiency in DevOps practices by setting up Google Kubernetes Engine (GKE) and deploying an application using Terraform, GitHub Actions, Argocd,  and Python.

New customers are eligible for $300 in credits from Google Cloud Platform (GCP). You can leverage this credit for the purpose of this assessment.

**Task 1: Infrastructure Provisioning with Terraform**

Write a Terraform script to provision the necessary infrastructure on GKE. This includes creating a GKE cluster that will serve as the deployment environment for the application. Ensure that your script reflects best practices for scalability, reliability, and security.

**Task 2: Dockerizing the Application**

Dockerize the provided application. Create a Docker image that encapsulates the application and its dependencies. Share your Dockerfile and any relevant configuration files used in the process.

**Task 3: Continuous Deployment with GitHub Actions and ArgoCD**

Deploy ArgoCD to manage and automate the continuous delivery of applications on Kubernetes.
Set up a GitHub Actions workflow for the application to be automatically deployed to GKE whenever there are new changes in the repo. Provide documentation on the workflow and configuration files used in both GitHub Actions and ArgoCD.

**Questions for Explanation:**
   - Explain how you would scale the application within the GKE cluster.
   - Outline the measures taken to ensure the reliability of the application on GKE, considering factors like fault tolerance and high availability.
   - Elaborate on the security measures that can be implemented to safeguard the application.
   - Discuss how you would handle migration , secrets and environemnt varaiables.

**Submission Guidelines:**
- Provide a link to the GitHub repository containing your Terraform scripts, Dockerfile, GitHub Actions workflow, and ArgoCD configuration.
- Include documentation that explains the setup, rationale behind design choices, and steps for scaling and securing the application.

This assessment aims to evaluate your ability to implement DevOps practices effectively and make informed decisions in configuring and securing a GKE deployment. Feel free to dazzle with your solutions. Good luck!
