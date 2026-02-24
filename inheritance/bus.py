#making a parent and a child class
class vehicle:
    def __init__(self,name,mileage,max_speed):
        self.name=name
        self.mileage=mileage
        self.max_speed=max_speed
class bus(vehicle):
    pass
object_1=bus('tata',230,160)
print("max speed:",object_1.max_speed)
print("mileage:",object_1.mileage)
print("name:",object_1.name)
