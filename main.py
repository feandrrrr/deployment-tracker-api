from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Deployment(BaseModel): #Pydantic basic model for deployments
    id: int
    service_name: str
    environment: str
    version: str
    status: str
    owner: str
    risk_level: str

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

    return {"error": "Deployment not found"} #in case not found