# class jungle():
#     def __init__(self):
#         print("welcome to the jungle")

# class animal():
#     def hi(self,name):
#         self.name = name
#         self.type = None
#         self.color = None

#     def hello(self):
#         print(f"helllo my name is {self.name}")

#     def type1(self):
#         print(f"my type is {self.type}")

#     def colour(self):
#         print(f"my colour is {self.color}")        
# animal_1 = animal()
# animal_1.hi('brian')
# animal_1.hello()

# class lion(animal):
#     def roar(self):
#         print('im the king of the jungle and i roar')
# lion_1 = lion()
# lion_1.type('carnivore')
# lion_1.type1()
# lion_1.color("brown")
# lion_1.colour()
# lion_1.roar()


# class tiger(animal):
#     def hunt(self):
#         print('im a tiger and i hunt')

# tiger_1 = tiger()
# tiger_1.type('carnivore')
# tiger_1.type1()
# tiger_1.color("white")        
# tiger_1.colour()
# tiger_1.hunt()
    


class jungle():
    def __init__(self):
        print("welcome to jungle")

jungle = jungle()

class animal():
    def __init__(self,name):
        self.name = name
        self.type = None
        
        self.color = None

    def hello(self):
        print(f"i am a visitor of animals my name is {self.name}")

    def type1(self):
        print(f"im a {self.type}")    

    def colour(self):
        print(f"my colour is {self.color}")    

animal_1 = animal('brian')

animal_1.hello()            

class lion(animal):
    def roar(self):
        print('im the king and i roar')

lion_1 = lion('abc')
lion_1.type = 'carnivore'   
lion_1.type1()
lion_1.color = 'white'
lion_1.colour()    
lion_1.roar()

class tiger(animal):
    def hunt(self):
        print("i hunt animals because im a tiger")

tiger_1 = tiger('bnm')
tiger_1.type = 'carnivore'
tiger_1.type1()
tiger_1.color = 'brown'
tiger_1.colour()
tiger_1.hunt()        