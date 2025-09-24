from fastapi import FastAPI
import json

app= FastAPI()

def patient_data():
    with open("patients.json", "r") as f:
        patients=json.load(f)
        return patients

@app.get("/")
def all_patient():
    data= patient_data()

    return data
