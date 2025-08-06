class jungle():
    def __init__(self):

        print('This is my jungle. Let me take you to my jungle safari!!!')
jungle = jungle()        

# class commonmeta(type):
    # pass

class animal():
    def __init__(self):
    
        print("these are of different types that are birds and mammals")
        self.typee = None
        self.habitat = None
        self.feeding = None
        self.gender = None
        self.age = None
        self.kill = None  

    
        print("these are of different types that are birds and mammals")

    def kll(self):
        print(f'they come in the category of {self.kill}')


    def tp(self):
        print(f"the types are {self.typee}")    

    def live(self):
        print(f"they live on {self.habitat}")

    def eat(self):
        print(f"they are a {self.feeding} speacies")

    def gndr(self):
        print(f"they are {self.gender} in gender")

    def agee(self):
        print(f"they are {self.age} years old")                

    def types(self):
        print(f"There are different types of animals such as birds and mammals")

    def speak(self):
        print("every animal speaks different languages in their own habitat")

    def get_info(self):
        print("now we will study these categories further and get info about them")

animal_1 = animal()  
# animal_1.types()
animal_1.speak()
animal_1.get_info()              

class mammal(animal):
    def __init__(self):
        # self.intro = name
        # self.eat = name
        # self.speed = name    
        print('mammals is one sub category  of animals which have lions, tigers , zebra etc.')

    def have(self,have):
        self.have = name

    def nature(self):
        print(f" eat {self.have} for a living")

    def speed(self, speed):
        self.speed = speed    

    def spd(self):
        print(f"they are {self.speed} in nature")


mammal_1 = mammal()

mammal_1.typee = 'different'
mammal_1.tp()
mammal_1.habitat = 'land'
mammal_1.live()
mammal_1.feeding = 'carnivores and herbivores'
mammal_1.eat()
mammal_1.gender = 'male or female'
mammal_1.gndr()
mammal_1.age = 'depends of different mammals'
mammal_1.agee()
mammal_1.have = 'different mammals eat different'
mammal_1.nature()
mammal_1.speed = ' fast or slow depending on different mammals '
mammal_1.spd()

class birds(animal):
    def __init__(self):
        print("Another sub category of animals is birds. ")

    def color(self,color):
        self.color = color

    def colour(self):
        print(f"birds have  {self.color} colour as per their nature")
    
    def nests(self,nest):
        self.nest = nest

    def build_nests(self):    
        print(f'they {self.nest} nests as per their nature ')

birds_1 = birds()
birds_1.typee = 'parrot eagle hawk'
birds_1.tp()
birds_1.habitat = 'air'
birds_1.live()
birds_1.feeding = 'carnivores and herbivores'
birds_1.eat()
birds_1.gender = 'male or female'
birds_1.gndr()
birds_1.age = 'depends of different mammals'
birds_1.agee()
birds_1.color('different')
birds_1.colour()
birds_1.nests(' depending on their types build')
birds_1.build_nests()


class Metalion(type):
    pass
class Metatiger(type):
    pass


class lion(mammal, metaclass=Metalion):
    def __init__(self):
        print('lions are one sub type of mammals')
    
    def hunt(self):
        print('lions hunt other animals for their living')

lion = lion()
lion.typee = 'variety of '
lion.tp()
lion.habitat = 'land'
lion.live()
lion.feeding = 'carnivores'
lion.eat()
lion.gender = 'male'
lion.gndr()
lion.age = '20'
lion.agee()
lion.have = '  different animals'
lion.nature()
lion.speed = ' fast  '
lion.spd()      
lion.kill = 'predators'
lion.kll()  
lion.hunt()

class tiger(mammal, metaclass=Metatiger):
    def __init__(self):
        print('Another sub type of mammals is tiger')


    def cmflg(self):
        print ('they camouflage in the wild to find their prey')       

tiger = tiger()
tiger.typee = 'variety of '
tiger.tp()
tiger.habitat = 'land'
tiger.live()
tiger.feeding = 'carnivores'
tiger.eat()
tiger.gender = 'male'
tiger.gndr()
tiger.age = '20'
tiger.agee()
tiger.have = '  different animals'
tiger.nature()
tiger.speed = ' fast  '
tiger.spd()      
tiger.kill = 'predators'
tiger.kll()  
tiger.cmflg()

class bear(mammal):
    def __init__(self):
        print('bears are another sub category of mammals')

    def sleep(self):
        print('they hibernate a lot')  

# bear = bear()
# bear.typee = 'variety of '
# bear.tp()
# bear.habitat = 'land'
# bear.live()
# bear.feeding = 'carnivores'
# bear.eat()
# bear.gender = 'male'
# bear.gndr()
# bear.age = '20'
# bear.agee()
# bear.have = '  different animals'
# bear.nature()
# bear.speed = ' fast  '
# bear.spd()      
# bear.kill = 'predators'
# bear.kll()            
        
class parrot(birds):
    def __init__(self):
        print('one sub class of birds are parrot.')

    def speak_words(self):
        print('parrot speaks words')

# parrot = parrot()
# parrot.typee = 'parrot '
# parrot.tp()
# parrot.habitat = 'air'
# parrot.live()
# parrot.feeding = ' herbivores'
# parrot.eat()
# parrot.gender = 'male '
# parrot.gndr()
# parrot.age = 'depends of different mammals'
# parrot.agee()
# parrot.color('')
# parrot.colour()
# parrot.nests('  build')
# parrot.build_nests()
# parrot.kill = 'prey'
# parrot.kll()   
# parrot.speak_words()

class eagle(birds):
    def __init__(self):
        print(' another sub class type of birds are eagles ')

    def soar_high(self):
        print('eagles soar high in the sky')    

# eagle = eagle()
# eagle.typee = 'eagle '
# eagle.tp()
# eagle.habitat = 'air'
# eagle.live()
# eagle.feeding = ' carnivores'
# eagle.eat()
# eagle.gender = 'male '
# eagle.gndr()
# eagle.age = 'depends of different mammals'
# eagle.agee()
# eagle.color('white')
# eagle.colour()
# eagle.nests('  build')
# eagle.build_nests()
# eagle.kill = 'predators'
# eagle.kll()   
# eagle.soar_high()

# print(type(lion) is type(tiger))

class MetaLiger(Metalion, Metatiger):
    pass

class liger(lion , tiger, metaclass=MetaLiger):
    pass
    # def __init__(self):
    #     print('liger is a baby class animal of lion and tiger')

    # def info(self):
    #     print('liger has high strength qualities from both parents. it is a hybrid of lion and tiger')   

    # def sterile(self):
    #     print('they are sterile in nature')     

liger = liger()
# liger.info()
# liger.sterile()
# liger.typee = 'variety of '
# liger.tp()
# liger.habitat = 'land'
# liger.live()
# liger.feeding = 'carnivores'
# liger.eat()
# liger.gender = 'male'
# liger.gndr()
# liger.age = '20'
# liger.agee()
# liger.have = '  different animals'
# liger.nature()
# liger.speed = ' fast  '
# liger.spd()      
# liger.kill = 'predators'
# liger.kll()  
# liger.cmflg()        
# liger.hunt()


      