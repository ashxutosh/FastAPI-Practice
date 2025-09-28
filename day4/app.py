from fastapi import FastAPI ,Path , Query , HTTPException
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
def patient_id(patient_id: str = Path(...,description="This is the Patient_Id", example="P001")):
    data= patient()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=400, detail="Bad Request")