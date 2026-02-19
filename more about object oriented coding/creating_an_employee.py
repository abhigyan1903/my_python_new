#Employee ina nd out through classes
class Employee:
    def __init__(self):
        print("Employee has been created")
    def __del__(self):
        print("you have called the destrtructor ,object is deleted")
def create_call():
    print("function has started.....")
    obj_1=Employee()
    print("Function is ending.....")


print("The program has started....")
obj_1=create_call()
print("the program has ended ....")