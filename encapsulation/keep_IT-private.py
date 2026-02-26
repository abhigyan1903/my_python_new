#making a class ussing private attributer
class my_class:
    __private_inf=67
    def __private_2(self):
        print("This is private you cannot acces this !!!")
    def hello(self):
        print("public,but inside the class orivate variable can be accessed:",self.__private_inf)
        print(my_class.__private_2)
        
obj_1=my_class()
obj_1.hello()