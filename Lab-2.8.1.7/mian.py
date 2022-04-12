class Tires():
    def __init__(self, size) -> None:
        self.__size = size
        self.__preasure = 0
    
    def get_preasure(self):
        return self.__preasure

    def pump(self, preasure):
        self.__preasure = preasure

class Engine():
    def __init__(self, fuel_type) -> None:
        self.__fuel_type = fuel_type
        self.__state = 'stop'
    
    def start(self):
        self.__state = 'start'
    
    def stop(self):
        self.__state = 'stop'
    
    def get_state(self):
        return self.__state

class Vehicle():
    def __init__(self, VIN, engine, tires) -> None:
        self.VIN = VIN
        self.engine = engine
        self.tires = tires
    

tCity = Tires(15)
tOffRoad = Tires(18)

eElectric = Engine('Electric')
ePetrol = Engine('Petrol')

car1 = Vehicle(1,eElectric,tCity)
car2 = Vehicle(2,ePetrol, tOffRoad)

car1.engine.start()
print(car1.engine.get_state())