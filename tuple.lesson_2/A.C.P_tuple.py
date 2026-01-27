#program to find the product of all numbers of the tuple
tuple_1=(1,3,6,8,23,89)
tuple_2=()
product=1
for i in tuple_1:
    product=product*i
    tuple_2=tuple_2+(product,)
     
    
print(tuple_2)