#making a bird class thruogh inheritance
class bird:
    def __init__(self):
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def whoisthis(self):
        print("penguin")
    def swim(self):
        print("fastest swimmer")
        
peggy=penguin()
peggy.whoisthis()
peggy.swim()