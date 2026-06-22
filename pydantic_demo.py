from pydantic import BaseModel
from typing import List , Dict

class patient(BaseModel):

    ### TYPE VALIDATION
    name: str
    age: int
    ### COMPLEX TYPE VALIDATION
    weight: float
    married: bool
    allergies: List[str] #values in allergies list should be string
    contect_details: Dict[str,str] #values in contect detail dictionary should be string and string

patient_info = {'name':'om', 'age':20, 'weight':65, 'married':True, 'allergies':['pollen','dust'], 'contect_details':{'email':'abc@gamil.com','phone':'9876543210'}}

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


