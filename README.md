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





**SOLUTION TO QUESTIONS FOR EXPLANATION **

Questions for Explanation:

1. Scaling the Application within GKE:
Utilizing the  GKE's node auto-scaling feature to automatically adjust the number of nodes based on demand.
Implementing horizontal pod auto-scaling (HPA) in Kubernetes to automatically adjust the number of pod replicas based on resource utilization.

2. Measures for Reliability on GKE:
Seting up multiple GKE nodes in different zones for high availability.
Use Kubernetes PodDisruptionBudget to control the disruption caused by voluntary disruptions.
Implement health checks and readiness probes for application pods to ensure they are serving traffic only when ready.

3. Security Measures:
Use GKE Private Clusters to restrict access to the cluster's control plane.
Implement RBAC (Role-Based Access Control) to control access to resources within the cluster.
Enable VPC-native (Alias IP) Clusters for better network security.
Utilize Kubernetes Secrets for sensitive data and avoid storing them in version control.

4. Handling Migration, Secrets, and Environment Variables:
For migration, using Kubernetes Rolling Updates for zero-downtime deployments is the optimal option here.
Storing of sensitive data, such as API keys and database passwords, in Kubernetes Secrets is the best security practice.
Injecting of  environment variables into the application pods using Kubernetes ConfigMaps or Secrets.
Using a tool like Helm to manage and version Kubernetes manifests,in my experience, makes it easier to manage configurations and updates.
