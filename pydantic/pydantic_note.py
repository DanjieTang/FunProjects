from pydantic import BaseModel

class Student(BaseModel):
    age: int
    height: int # In cm. That's right metrics system let's goooo.
    name: str
    
student1 = Student(age=19, height=175, name="Alex")
student2 = Student(age=20, height=180, name="Bob")