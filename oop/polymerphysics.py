class Car:
    toat=0
    def __init__(self, brand, modle):
        self.__brand = brand  # Private attribute
        self.modle = modle 
        Car.toat+=1
        
    def car_name(self):
        return f"{self.__brand} {self.modle}"
    #polymorphism
    def fule_type(self):
        return "petrol or deisel"  
         
    

### Inherit from main class
class ElectricCar(Car):
    def __init__(self, brand, modle, battery_size):
        
        super().__init__(brand, modle)
        self.battery_size = battery_size
        
        
    #polymorphism
    def fule_type(self):
        return "Electric charge"
         
     
# Creating instances
my_car = Car("Toyota", "Corolla")
my_c = ElectricCar("Tesla", "Model 3", "75 kWh")

# Testing the code
print(my_car.fule_type()) 
print(my_c.fule_type()) 
print(Car.toat)