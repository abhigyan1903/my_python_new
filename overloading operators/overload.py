#practisin overloading operators

class greater:
    def __init__(self,a):
        self.a=a
    def __gt__(ob1,ob2):
        if ob1.a>ob2.a:
            return ob1.a,"is greater than:",ob2.a
        else:
            return ob2.a,"is greater than:",ob1.a
    def __eq__(ob1, ob2):
        if ob1.a==ob2.a:
            return ob1.a,"is equal to:",ob2.a
        else:
            return ob1.a,"Is not equal to :",ob2.a
        
ob1=greater(2000)
ob2=greater(5800)
print(ob1>ob2)
print(ob1==ob2)

