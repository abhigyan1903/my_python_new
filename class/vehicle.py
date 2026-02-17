#using init method in clear
class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
bmw=vehicle(240,30)
print("The max speed of the bmw is: ",bmw.max_speed)
print("The mileage of the bmw is:",bmw.mileage)
