from fastapi import FastAPI ,Path , Query
import json

app=FastAPI()

def patient():
    with open("patients.json", "r") as f:
        patients=json.load(f)
        return patients

@app.get("/")  #root path for all patients data
def view():
    data= patient()
    return data

@app.get("/patient/{patient_id}")
def patient_id(patient_id: str):
    data= patient()

    if patient_id in data:
        return data[patient_id]
    return {"error": "patient not found"}
