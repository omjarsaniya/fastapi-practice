from pydantic import BaseModel, EmailStr, AnyUrl, Field
### EmailStr, AnyUrl this are custome datatypes...
### Field(not custome) is useful for numerical and string based datatypes for custome data validation
from typing import List , Dict , Optional , Annotated

class patient(BaseModel): ## BYDEFAULT ALL FIELDS ARE REQUIRED BUT CAN BE OPTIONAL USING OPTIONAL  BY GIVING DEFAULT VALUE NONE 

    ### TYPE VALIDATION
    name: Annotated[str, Field(max_length=50, title='name of the patient', description='give the name of the patient in less than 50 chars', examples=['om','foram'])]
    age: int = Field(gt=0 ,lt=120)
    ### COMPLEX TYPE VALIDATION
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='is the patient married or not')]
    allergies: Annotated[Optional[list[str]], Field(default=None, max_length=5)] 
        #values in allergies list should be string 
        #there is optional there for if there in no allergies then it will show None          
    contect_details: Dict[str,str] #values in contect detail dictionary should be string and string

patient_info = {'name':'om', 'age':20, 'weight':65.0, 'married':True, 'allergies':['pollen','dust'], 'contect_details':{'email':'abc@gamil.com','phone':'9876543210'}}

### INSERTING 
def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted patient data')

patient1 = patient(**patient_info)

insert_patient_data(patient1)

### UPDATING
def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print('updated patient data')

update_patient_data(patient1)
