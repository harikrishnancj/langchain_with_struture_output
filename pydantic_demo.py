from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):#in here ther is validation so in place of str ther could be only str
    name: str = 'nick'  # default value
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(default=5, gt=0, lt=10)  # validation

# Create a Student instance
data = {'age': '32', 'email': 'abc@gmail.com'}
student = Student(**data)

print(student)
