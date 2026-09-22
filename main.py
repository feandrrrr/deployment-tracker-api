from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Deployment Tracker API is running"}