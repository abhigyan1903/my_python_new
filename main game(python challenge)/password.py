#making a random password of nine characters
import random

list_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_2=[1,2,3,4,5,6,7,8,9]
list_3=list_1+list_2
password=''

for i in range(9):
    password+=str(random.choice(list_3))
print("Your password is:",password)