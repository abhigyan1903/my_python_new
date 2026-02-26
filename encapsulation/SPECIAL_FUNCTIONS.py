#using special functions in python to print
class special:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "x={},y={}".format(self.x,self.y)
    
special_user=special(67)
print(special_user)