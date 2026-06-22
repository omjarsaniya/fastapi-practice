from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
### EmailStr, AnyUrl this are custome datatypes...
### Field(not custome) is useful for numerical and string based datatypes for custome data validation
from typing import List , Dict , Optional , Annotated

class Address(BaseModel):

    city: str
    state: str
    pin: str


class patient(BaseModel): ## BYDEFAULT ALL FIELDS ARE REQUIRED BUT CAN BE OPTIONAL USING OPTIONAL  BY GIVING DEFAULT VALUE NONE 

    ### TYPE VALIDATION
    name: Annotated[str, Field(max_length=50, title='name of the patient', description='give the name of the patient in less than 50 chars', examples=['om','foram'])]
    age: int = Field(gt=0 ,lt=120)
    email: EmailStr
    ### COMPLEX TYPE VALIDATION
    weight: Annotated[float, Field(gt=0, strict=True)] #kgs
    height: float #meters
    married: Optional[bool] = None
    allergies: Annotated[Optional[list[str]], Field(default=None, max_length=5)] 
        #values in allergies list should be string 
        #there is optional there for if there in no allergies then it will show None          
    contact_details: Dict[str,str] #values in contect detail dictionary should be string and string
    address: Address




    ### FIELD VALIDATOR (SHOULD BE INSIDE CLASS)
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        ## abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value
    
    ### MODEL VALIDATOR
    @model_validator(mode='after') ## DEFAULT MODE WILL BE AFTER (and it should be...)
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('patients older than 60 must have an emergency contact in contact details')
        return self

    ### COMPUTED FIELDS
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    


address_dict = {'city':'surat', 'state':'gujarat', 'pin':'395010'}
address1 = Address(**address_dict)


patient_info = {'name':'om', 'age':65, 'weight':65.0, 'height':1.69, 'email':'abc@hdfc.com', 'married':True, 'allergies':['pollen','dust'], 'contact_details':{'email':'abc@gamil.com','phone':'9876543210','emergency':'565656'},'address':address1}

### INSERTING 
def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('BMI',patient.calculate_bmi)
    print(patient.address)
    print('inserted patient data')

patient1 = patient(**patient_info)

insert_patient_data(patient1)

### UPDATING
def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print('updated patient data')

update_patient_data(patient1)


### SERIALIZATION (FOR EXPORTING PYDANTIC MODEL OBJECTS)

# PYTHON DICTIONARY FORMAT
temp = patient1.model_dump() ## we can include and exclude fields on our own way
print(temp)
print(type(temp))

# JSON FORMAT
temp = patient1.model_dump_json() ## we can include and exclude fields on our own way
print(temp)
print(type(temp))

