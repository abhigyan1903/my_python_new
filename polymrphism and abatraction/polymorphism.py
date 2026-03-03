#polymormhism
class India():
    def capital(self):
        print("Capital of india is Delhi")
    def language(self):
        print("Hindi is widely spoken in India")
    def type(self):
        print("India is a developing country")
        
class USA:
    def capital(self):
        print("Capital of USA is Washington D.C")
    def language(self):
        print("English is spoken in USA")
    def type(self):
        print("USA is a developed country")
        
obj_india=India()
obj_usa=USA()

for country in (obj_india, obj_usa):
    country.capital()
    country.language()
    country.type()
