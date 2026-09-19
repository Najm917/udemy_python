class Car:
    def __init__(self, brand, modle):
        self.__brand = brand  # Private attribute
        self.modle = modle 
        
    def car_name(self):
        return f"{self.__brand} {self.modle}"
        
    # encapsulates
    def get_brand(self):
        return self.__brand

### Inherit from main class
class ElectricCar(Car):
    def __init__(self, brand, modle, battery_size):
        super().__init__(brand, modle)
        self.battery_size = battery_size
         
     
# Creating instances
my_car = Car("Toyota", "Corolla")
my_c = ElectricCar("Tesla", "Model 3", "75 kWh")

# Testing the code
print(my_car.get_brand())
print(my_car.car_name())   
print(my_c.get_brand())    