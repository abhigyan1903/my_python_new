#parindrome tuples
def parindrome(tup):
    e=len(tup)-1
    s=0
    while s<e:
        if tup[s]!=tup[e]:
            return False
        s=s+1
        e=e-1
    return True
tuple_parindrome=(3,4,5,67,67,5,4,3)
if parindrome(tuple_parindrome):
      print("The tuple is flip flop and if inverted will hold the same value.")
else:
      print("The tuple is not flip flop and if inverted will not give the same value.")
