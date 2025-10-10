from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


def input_patient(patient: Patient):
    print(patient.name)

    print(patient.age)

    return patient


patient_data={"name":"Udit","age":30}

patient1=input_patient(Patient(**patient_data))

print(patient1)

print(type(patient1))