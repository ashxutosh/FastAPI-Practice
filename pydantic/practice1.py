from pydantic import BaseModel

class Patient(BaseModel):
    
    age: int


def input_patient(patient: Patient):
    

    print(patient.age)

    return patient


patient_data={"age":30}

patient1=input_patient(Patient(**patient_data))

print(patient1)

print(type(patient1.age))