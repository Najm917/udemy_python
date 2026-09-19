# constructor:----In Python, the constructor is a special method known as __init__(). It is automatically executed when an instance (object) of a class is created, and its primary role is to initialize the attributes (state) of the newly formed object.

#  The self Parameter: The first parameter is always self, which represents the current instance being initialized.

class Student:
    # Parameterized constructor
    def __init__(self, name, roll_no):
        self.name = name          # Instance variable
        self.roll_no = roll_no    # Instance variable

# Creating an object automatically calls __init__
s1 = Student("Amit", 101)

s2=Student("arif",55)

print(s1.name, s1.roll_no)  
print(s2.name, s2.roll_no) 