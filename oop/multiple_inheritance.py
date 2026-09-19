class Car():
    def __init__(self,brand):
        self.brand=brand
        
    
class Battery:
    def battery_info(self):
        return "battery info"
class Engine:
    def engine_info(self):
        return "engine info"   
class ElectricCar(Battery,Engine,Car):
    def __init__(self,brand):
        super().__init__(brand)
        
my_car=ElectricCar("abc")  
my_c=Car("tata")
print(my_car.battery_info())      
print(my_car.engine_info())
print(my_car.brand)
#print(my_c.engine_info())
        