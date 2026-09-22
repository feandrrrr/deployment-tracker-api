from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Deployment(BaseModel):
    service_name: str
    environment: str
    version: str
    status: str
    owner: str
    risk_level: str

@app.get("/")
def root():
    return {"message": "Deployment Tracker API is running"}