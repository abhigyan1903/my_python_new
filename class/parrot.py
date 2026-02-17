#making a class using init
class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

void=parrot("Void",3)
katie=parrot("Katie",9)

print("{} is {} years old".format(void.name,void.age))
print("{} is {} years old".format(katie.name,katie.age))