from enum import Enum, auto

class Subjects(Enum):
    MATH=auto()
    SCIENCE=auto()
    
    
variable = Subjects.SCIENCE
if variable == Subjects.MATH:
    print("Hello world")
else:
    print("Hi there")