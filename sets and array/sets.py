#printing the set
my_set={1,2,3,4,5,6,7}
print(my_set)

#making another set
my_set_2={4,5,"hello world",False,67.67}
print(my_set_2)

#sets do not duplicate
my_set_3={1,2,3,3,3,3,3,6,6,6,6,6,7,7,7,7}
print(my_set_3)

my_set_list=set([1,1,1,1,3,3,3,3,3,2,2,2,2,6,6,6,6,7,7,7,7])
print(my_set_list)

#deleating the first element of the set
my_set_list.pop()
print(my_set_list)