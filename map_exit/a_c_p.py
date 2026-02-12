#list compredhension
list_1=[1,2,34,5,67,8,90,13,32,34,56,8,7,98,567,57,56,54,56,56367,582546,54680,7,568]
odd=(y for y in list_1 if y%2==1)
odds=list(odd)
print("the odd numberes in this list are",odds)

fruits=['apple','mango','banana','grapes']
fruits_capitalized=[fruits.capitalize() for fruits in fruits]
print("the capitaliozed foerm of ruits are :",fruits_capitalized)