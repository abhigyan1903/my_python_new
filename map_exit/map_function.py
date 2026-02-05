#using the map functtion to add two numbers of a list
list_1={3,6,9,2,7}
list_2={2,5,7,9,11}

result=map(lambda a,b:a+b,list_1,list_2)

print("the addition of two lists is :",list(result))

#using the map function to multiply or find the square of the numbers of the list in a different way
number_list={2,4,6,8,3,5,7,9}
def square(n):
    return n*n
product=list(map(square,number_list))
print("the square of all the numbers in this list are :",product)