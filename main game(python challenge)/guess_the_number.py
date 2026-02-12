#making a guessing game
import random
import time
#making a number
number=random.randint(1,100)

#starting with makingh the functions
def intro():
    global name
    name=input("what is your name?:")
    print("Welcome"+name+"to the guessing game")
    
    print("I am thinking of a numberr betwween 1 and 100,can you guess it?")
    if number%2==0:
         x='even'
    else:
        x='odd'
    print("The number i have chosen is :",x)
    time.sleep(0.5)
    print("Lets start the guessing game")
    print("You haver 7 chances to guess")
def guess():
    
    guesstaken=0
    while guesstaken<7:
        time.sleep(0.5)
        enter=input("Take your guess:")
        try:
            guess=int(enter)
            if guess>=1 and guess<=100:
                guesstaken+=1
                if guess<number:
                    print("Your guess is too low")
                if guess>number:
                    print("Your guess is too high")
                if guess!=number:
                    print("Try again")
                if guess==number:
                    break
            if guess<1 or guess>100:
                print("oh silly goose,this number is out of range,try again(1-100)")
        except:
            print("I dont think that"+enter+"is a number,try again")
    if guess==number:
        print("Good job"+name+"!!!You have guessed the number in "+str(guesstaken)+"tries")
    if guess!=number:
        print("The number i was thinking of was"+str(number) )
play_again="yes"
while play_again=="yes" or play_again=="y" or play_again=="Yes":
    intro()
    guess()
    play_again=input("Do you want to play again?")