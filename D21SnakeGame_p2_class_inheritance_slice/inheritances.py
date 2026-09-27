# inheritance in python is a fundamental oop concept where is a new class (chil or drived class) derives attributs and method from an existing class (parents or boss class ) 

class Animal:
  def __init__(self):
    self.num_eye=2
    
  def breathing(self):
    print("inhel","exhel")
    
class Fish(Animal):  # inherit from main class Animal
  def __init__(self):
    super().__init__()
    
  def swing(self):
    print("moving in water")
    
abc=Fish()
xyz=Animal()
print(abc.num_eye)
print(xyz.breathing())