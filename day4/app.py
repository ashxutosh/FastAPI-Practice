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

@app.get("/sort")
def sorting(sort_by: str = Query(...,description="sort by bmi,height,weight",),order: str =Query("asc" , description="asc or desc order")):
     data= patient()

     fields= ["bmi","height","weight"]

     if sort_by not in fields:
         raise HTTPException(status_code=400, detail="Bad Request")
     if order not in ["asc","desc"]:
            raise HTTPException(status_code=400, detail="Bad Request")
     
     sort_order= False if order=="desc" else True

     sorted_data= sorted(data.items(), key=lambda x: x.get(sort_by,0), reverse=sort_order)

     return sorted_data