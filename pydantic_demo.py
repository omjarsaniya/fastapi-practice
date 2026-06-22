from pydantic import BaseModel

class patient(BaseModel):

    ### TYPE VALIDATION
    name: str
    age: int

patient_info = {'name':'om' , 'age':20}

### INSERTING 
def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print('inserted patient data')

patient1 = patient(**patient_info)

insert_patient_data(patient1)

### UPDATING
def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print('updated patient data')

update_patient_data(patient1)


