# Deployment Tracker API

A small learning project built to practice working with REST APIs, validation, testing, Docker, Terraform and CI.

The application provides a simple API for tracking software deployments, including their environment, version, status, owner and risk level.

## Purpose

This project was created for learning purposes. I used it to practice building a small API step by step and to better understand how different tools work together in a development workflow.

I also used AI assistance during development, mainly for explanations, troubleshooting and generating some initial test cases, while reviewing and testing the code myself.

## Tech Stack

- Python
- FastAPI
- Pydantic
- pytest
- Docker
- Terraform
- GitHub Actions

## Features

- Create deployments
- View all deployments
- View a deployment by ID
- Update deployment status
- Delete deployments
- Validate environment, status and risk level values
- Automated API tests
- Docker containerisation
- Terraform-managed Docker container
- GitHub Actions workflow for automatic testing

## Future Improvements

I plan to add a simple web interface so deployments can be created, viewed and updated through a browser instead of using the API documentation directly.

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Running with Docker

Build the image:

```bash
docker build -t deployment-tracker-api .
```

Run the container:

```bash
docker run -p 8000:8000 deployment-tracker-api
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Using Terraform

Initialise Terraform:

```bash
terraform init
```

Preview the planned changes:

```bash
terraform plan
```

Create the Docker resources:

```bash
terraform apply
```

## Testing

Run tests locally:

```bash
python -m pytest
```

GitHub Actions also runs the test suite automatically on every push and pull request.

## What I Practiced

- REST API development
- Pydantic validation
- CRUD operations
- API testing
- Docker images and containers
- Infrastructure as Code with Terraform
- Git and GitHub workflows
- Basic CI using GitHub Actions