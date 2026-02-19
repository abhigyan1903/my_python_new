#converting the ;etters to upper case

class upper_case:
    
     def __init__(self):
         self.string=""
         
     def input_1(self):
         self.string=input("Enter your string:")
     def upper_case_1(self):
         print("the number converted to upper case is- ",self.string.upper())
         
str1=upper_case()
str1.input_1()
str1.upper_case_1()