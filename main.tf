# Configure terraform and set the Docker provider
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

# Connect terraform to the local Docker
provider "docker" {}

# Reference the Docker image that was built locally
resource "docker_image" "deployment_tracker" {
  name = "deployment-tracker-api:latest"
}

# Create and manage a container from the Docker image
resource "docker_container" "deployment_tracker" {
  name  = "deployment-tracker-api-container"
  image = docker_image.deployment_tracker.image_id

# Map port 8000 inside the container to port 8000 on the host machine
  ports {
    internal = 8000
    external = 8000
  }
}