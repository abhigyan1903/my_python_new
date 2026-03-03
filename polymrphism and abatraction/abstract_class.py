#making an abstract class  

from abc import ABC,abstractmethod

class hello(ABC):
    def task1(self,x):
          print("passed value :", x)
    @abstractmethod
    def task(self):
        print("you cannot see this inner class")
    
class hello12(hello):
    def task(self):
        print("hello")
 
hello_object=hello12()
hello_object.task1(1784)
