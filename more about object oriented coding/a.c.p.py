#area and circumfeence of a circle
class math_1:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius
objetc=math_1(21)
print("area:",objetc.area())
print("circumference:",objetc.circumference())

