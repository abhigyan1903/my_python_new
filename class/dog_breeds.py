#dog breeds
#homework
class dog:
    type="dog"
    def __init__(self,breed,max_age,color):
        self.breed=breed
        self.max_age=max_age
        self.color=color
german_shepherd=dog("german shepherd",14,"black and tan")
labrador_retrirever=dog("labrador rertreiver",12,"yellow")

print("German Shepherd, Max age:",german_shepherd.max_age,", color:",german_shepherd.color)
print("Labrador Retriever, Max age:",labrador_retrirever.max_age,", color:",labrador_retrirever.color)
