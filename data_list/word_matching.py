#matccing two words depending on their firt and last letters
def matching_word(words):
  counter_1=0
  lists=[]
  for w in words:
      if len(w)>1 and w[0]==w[-1]:
          counter_1+=1
          lists.append(w)
  print("the number which has both equal characters of first and last",lists)
  return counter_1
list_1=["csdsz","abaaa","buhbefv","khdsgxk","3465461543"]
print("the amtching numbers of this list are:",matching_word(list_1))
  