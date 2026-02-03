#making  dictionarys and trying to not duplicate the values
student_data={
    "id1": {"name":"Steve","class":"v","subject":['maths','biology','history']},
    "id2": {"name":"Alex","class":"v","subject":['maths','biology','history']},
    "id3": {"name":"Steve","class":"v","subject":["matths,biology,history"]},
    "id4": {"name":"Alex","class":"v","subject":['maths','biology','history']},
}
result={}
for key,values in student_data.items():
    if values not in result.values():
         result[key]=values
print(result)