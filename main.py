from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum #for validation

app = FastAPI()

# Validation classes, will use them in models
class Environment(str, Enum):
    development = "development"
    staging = "staging"
    production = "production"


class DeploymentStatus(str, Enum):
    planned = "planned"
    deploying = "deploying"
    deployed = "deployed"
    failed = "failed"


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Deployment(BaseModel): #Pydantic basic model for deployments
    id: int
    service_name: str
    environment: Environment
    version: str
    status: DeploymentStatus
    owner: str
    risk_level: RiskLevel

class DeploymentStatusUpdate(BaseModel): #model for status update
    status: DeploymentStatus

deployments = []
@app.get("/")
def root():
    return {"message": "Deployment Tracker API is running"}

@app.post("/deployments")  #endpoint for adding new deployment
def create_deployment(deployment: Deployment): #data must fit the model
    deployments.append(deployment)
    return deployment

@app.get("/deployments") #get all deployments
def get_deployments():
    return deployments

@app.get("/deployments/{deployment_id}") #endpoint to get deployment by id
def get_deployment(deployment_id: int):
    for deployment in deployments: #loop to find and return needed depl
        if deployment.id == deployment_id:
            return deployment

    raise HTTPException(status_code=404, detail="Deployment not found") #in case not found

@app.patch("/deployments/{deployment_id}") #endpoint for status updates
def update_deployment_status(deployment_id: int, update: DeploymentStatusUpdate):
    for deployment in deployments:
        if deployment.id == deployment_id: #if deployment found - update its status
            deployment.status = update.status
            return deployment

    raise HTTPException(status_code=404, detail="Deployment not found")

@app.delete("/deployments/{deployment_id}") #endpoint to delete deployment by id
def delete_deployment(deployment_id: int):
    for index, deployment in enumerate(deployments): #get positions and IDs of objects in the list
        if deployment.id == deployment_id: #id check
            deleted_deployment = deployments.pop(index) #delete deployment using .pop (relocate into deleted_deployment)
            return deleted_deployment #show client which deployment deleted

    raise HTTPException(status_code=404, detail="Deployment not found")