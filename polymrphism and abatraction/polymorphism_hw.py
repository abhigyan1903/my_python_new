#making a project on polymorphism(vehicle)
class BMW:
    def speed(self):
        print("max speed is 250km/hr")
    def engine(self):
        print("has a very powerful engine")
    def mileage(self):
        print("mileage is : 30km/hr")
    def color(self):
        print("Most popular color is black")
        
class lamborghini:
    def speed(self):
        print("max speed is 400km/hr")
    def engine(self):
        print("has a comparitavely way more powerful engine")
    def mileage(self):
        print("mileage is : 25km/hr")
    def color(self):
        print("MOst popular color is red")
        
object_BMW=BMW()
object_lambo=lamborghini()

for i in (object_BMW,object_lambo):
     i.speed()
     i.engine()
     i.mileage()
     i.color()
