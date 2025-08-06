# NOTES OF THIS -

# practice getter and setter methods
# focus on attributes
# engine on and off in function

# attributes of car - engine, handle, mirror
# function of car -  engine off/on , moving , stopped
# attributes of dog - eye colour , nose ,ear shape
# functions of dog - eating, sleeping , playing , running , hair shedding(seasonal)

# PRACTICE OF CODE-

class vehicle():
    def __init__(self):
        print("This is a vehicle and now we are talking about vehicle family tree")
        self.type = None
        self.fuel = None
        self.no_of_wheels = None
    

    def type1(self):
        print(f"{self.type} is the type of  this vehicle ")  

    

    def nfuel(self):
        print(f"{self.fuel} is the fuel in it")       

   

    def wheelertype(self):    
        print(f"{self.no_of_wheels} is the wheelertype of this vehicle")   

    

    def nfuel(self):
        print(f"{self.fuel} is the fuel in it")     
      
             
vehicle_1 = vehicle()    

class car(vehicle):
    def __init__(self):
        print("TYPE 1 OF VEHICLES - CAR. There are different types of car ")

    def seats(self,name):
        self.name = name 

    def sts(self):
        print(f"{self.name} are the seats in there")      

    def  version(self, versionname):
        self.versionname = versionname

    def vrs(self):    
        print(f"  {self.versionname} version of this vehicle")   

car_1 = car()

car_1.fuel = 'Petrol'
car_1.nfuel()
car_1.no_of_wheels = 'four'
car_1.wheelertype()
car_1.seats('four')
car_1.sts()
car_1.version('different type have')
car_1.vrs()



class muv(car):
    def __init__(self):
        print('now we will talk about firs sub class of car-  muvs')

    def color(self,name):
        self.name = name

    def colour(self):
        print(f"{self.name} is the colour of this vehicle")

    def spd(self,speedname):
        self.speedname = speedname

    def speed(self):
        print(f"It is a {self.speedname} speed vehicle")  

muv_1 = muv()
muv_1.type = 'muv'
muv_1.type1()
muv_1.fuel='petrol'
muv_1.nfuel()
muv_1.no_of_wheels= 'four'
muv_1.wheelertype()
muv_1.seats('four seated')
muv_1.sts()
muv_1.version('old')
muv_1.vrs()      
muv_1.spd('moderate')
muv_1.speed()        
muv_1.color('red')
muv_1.colour()

class suv(car):
    def __init__(self):
        print('suvs are another sub type of this vehicle')

    def ftr(self,ftrname):
        self.ftrname = ftrname

    def feature(self):
        print(f"It has {self.ftrname} feautures")

    def ntr(self,ntrname):
        self.ntrname = ntrname

    def nature(self):
        print(f"it has {self.ntrname} nature")                

suv_1 = suv()
suv_1.type = 'suv'
suv_1.type1()
suv_1.fuel = 'petrol'
suv_1.nfuel()
suv_1.no_of_wheels = 'four'
suv_1.wheelertype()
suv_1.seats('four seated')
suv_1.sts()
suv_1.version('newer')
suv_1.vrs()      
suv_1.ftr('advanced')
suv_1.feature()
suv_1.ntr('ecofriendly')
suv_1.nature()

class bike(vehicle):
    def __init__(self):
        print('TYPE 2 OF VEHICLES - BIKE. There are different types of bikes.')

    def color(self,clrname):
        self.clrname = clrname 

    def colour(self):
        print('{self.clrname} is the colour of this vehicle.')

    def spd(self,spdname):
        self.spdname = spdname 

    def speed(self):
        print("It is a {self.spdname} speed bike.")

bike_1 = bike()
bike_1.type = 'many'
bike_1.type1()
bike_1.fuel= ' diesel and petrol'
bike_1.nfuel()
bike_1.no_of_wheels = 'two'
bike_1.wheelertype()

class scooty(bike):
    def __init__(self):
        print('scooty is one sub type of bike')

    def sts(self,stsname):
        self.stsname = stsname

    def seats(self):
        print(f"{self.stsname}are the seats in it")

    def vrs(self,vrsname):
        self.vrsname = vrsname

    def version(self):
        print(f"it is a {self.vrsname} version")

scooty_1 = scooty()
scooty_1.type = 'scooty'
scooty_1.type1()
scooty_1.fuel  = ' diesel and petrol'
scooty_1.nfuel()
scooty_1.no_of_wheels = "two"
scooty_1.wheelertype()
scooty_1.vrs('regular use')
scooty_1.version()
scooty_1.sts('two')
scooty_1.seats()

class sportsbike(bike):
    def __init__(self):
        print('another sub type of bike is sports bike')

    def colorr(self,colorrname):
        self.colorrname = colorrname 

    def colourn(self):
        print(f"{self.colorrname} is its colour")

sportsbike_1 = sportsbike()
sportsbike_1.type = 'sportsbike'
sportsbike_1.type1()
sportsbike_1.fuel = ' diesel and petrol'
sportsbike_1.nfuel()
sportsbike_1.no_of_wheels = 'two-wheeler'
sportsbike_1.wheelertype() 
sportsbike_1.colorr('green')
sportsbike_1.colourn()      



