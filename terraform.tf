provider "google" {
  credentials = file("<path-to-the-service-account-key>")
  project     = "<the-gcp-project>"
  region      = "us-central1"
}

resource "google_container_cluster" "my_cluster" {
  name     = "my-gke-cluster"
  location = "us-central1"

  node_pool {
    name       = "default-pool"
    node_count = 1
    machine_type = "e2-medium"

    preemptible  = false
    autoscaling {
      min_node_count = 1
      max_node_count = 5
    }
  }
}

output "kubeconfig" {
  value = google_container_cluster.my_cluster.kubeconfig[0].raw_config
}
