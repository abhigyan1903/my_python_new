#making an array and practising with it
import array as ar
array_num=ar.array('i' ,[3,6,4,7,5,4,3,2,5,2,3,3])
print("The original array is:",array_num)
print("The number of times the number 3 has been repeated in this array is : ",array_num.count(3))
array_num.reverse()
print("The reversal of this array is :",array_num)