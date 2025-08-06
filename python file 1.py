class vehicle():
    def __init__(self):
        print("This is a vehicle and now we are talking about vehicle family tree")
    
    def tp(self,name):
        self.name = name

    def type1(self):
        print(f"{self.name} is the type of  this vehicle ")  

    def update_fuel(self,fuelname):
        self.fuelname = fuelname 

    def nfuel(self):
        print(f"{self.fuelname} is the fuel in it")       

    def  wn(self,wheelername):
        self.wheelername = wheelername

    def wheelertype(self):    
        print(f"{self.wheelername} is the wheelertype of this vehicle")   

    def update_fuel(self,fuelname):
        self.fuelname = fuelname 

    def nfuel(self):
        print(f"{self.fuelname} is the fuel in it")     
      
             
vehicle_1 = vehicle()    

class car(vehicle):
    def __init__(self,name):
        self.type = name
        self.fuelname = None
        self.wheelername = None

    def welcome():
        print("our first type is car ")
        # super().__init__()

    def category(self,name):
        self.name = name 

    def ctg(self):
        print(f"{self.name} is the one category of car")     

    def  version(self, versionname):
        self.versionname = versionname

    def vrs(self):    
        print(f" it is an {self.versionname} version of this vehicle")    

car_1 = car('sedan')
car_1.type1()
car_1.update_fuel('diesel')
car_1.nfuel()
car_1.wn('Four-wheeler')
car_1.wheelertype()

car_2 = car('xuv')
car_2.type1()
car_2.update_fuel('diesel')
car_2.nfuel()
car_2.wn('Four-wheeler')
car_2.wheelertype()


class bike(vehicle):
    def __init(self,name):  #Constructor
        self.name = name 
        print('now we will talk about bikes')

    def type(self):
        print(f'{self.name} is the type of bike. ') 

    def color(self,name):
        self.name = name

    def colour(self):
        print(f"{self.name} is the colour of this vehicle ")        

bike_1 = bike('abc')
bike_1.type1() 
bike_1.wn('two-wheeler')
bike_1.wheelertype()            
bike_1.update_fuel('petrol')
bike_1.nfuel()  
bike_1.color('red')
bike_1.colour()

class truck(vehicle):
    def __init__(self,name):
        self.name = name

    def hi(self):
        print('now we will talk about trucks')

    def nm(self):
        print(f"{self.name} is the type of this truk")    


truck_1 = truck('mno')
truck_1.nm()
truck_1.wn('six-wheeler')
truck_1.wheelertype()
truck_1.hi()
truck_1.update_fuel('petrol')
truck_1.nfuel()
truck_1.color('yellow')
truck_1.colour()







    




