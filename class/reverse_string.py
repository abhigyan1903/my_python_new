#code for reversing the string in python very easily            
def reverse_string(string):
    return string[::-1]                 
string=input("enter the string you want to reverse :")
reversed_string=reverse_string(string)
print("the reversed string is :",reversed_string)