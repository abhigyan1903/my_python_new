#makingh a new flashcard  compiler
class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    
    def __str__(self):
        return self.word + '(' + self.meaning + ')'

flash=[]
print("welcome to flash card application,you can make flashcards here")
while(True):
        word=input("Enter the word you want to add a flashcard : ")
        meaning=input("Enter the meaning of the word : ")
        object_1=flashcard(word,meaning)
        flash.append(object_1)
        print("Flashcard has been successfully added!!")
        
        option=input("enter 1 to exit or 2 to add more flashcards : ")
        
        if option=='1':
            break
        
for i in flash:
    print("-------",i)