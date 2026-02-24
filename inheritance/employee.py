#making a vclass to derive an employee
class person:
    def __init__(self,idnumber,name):
         self.name=name
         self.idnumber=idnumber
         
    def display(self):
              print("name:",self.name)
              print("idnumber:",self.idnumber)
class employee(person):
    def __init__(self, idnumber, name,salary,age):
            self.salary=salary
            self.age=age
            
            person.__init__(self,idnumber,name)
object=employee(652385,'rahul',330000,23)

object.display()
                
        