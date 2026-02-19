#making a pair of elements in a class using enumerate
class paair_elements:
    
    def two_sum(self,nums,targets):
        lookup={}
        for i,num in enumerate(nums):
            if targets-num in lookup:
                return(lookup[targets-nums],i)
            lookup[num]=i

target=int(input("Enter your target number- "))
print("index1=%d,index2=%d"% paair_elements().two_sum([10,20,30,40,50,60,70,80,90,100],target))