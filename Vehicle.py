

#-------------------------------------------------------
#Vehicle Class Starts Here



class Vehicle:
    id =0

    def __init__(self, givenSimulation, numberOfSeats):
        Vehicle.id +=1
        self.id = Vehicle.id
        self.currentSpeed=0 #current speed of the vehicle
        self.numberOfSeats = numberOfSeats
        
        self.simulation = givenSimulation
        self.simulation.preSimVehiclelist.append(self)
    def __repr__(self):
        return ("Vehicle id: {id}".format(id=self.id))
    def setVehicleEngine(self, givenEngine):
        self.engine=givenEngine
    def setvehicleType(self,giventype):
        self.type=giventype
    def setVehiclePassangerCapacity(self,capacity):
        self.passangerCapacity=capacity
    def setVehicleDriver(self,driver):
        self.driver=driver
    

#Vehicle Class Ends Here
#-------------------------------------------------------







#-------------------------------------------------------
#Vehicle Type Class Starts Here
class VehicleType:
    id=0

    def __init__(self, givenName, maxSpeed, givenEngine, isPublic = False):
        VehicleType.id +=1
        self.name = givenName # name of the Vehicle Type
        self.isPublicTransport = isPublic # if this type is a public transport vehicle
        self.engine=givenEngine #Engine type of the vehicle
        self.maxSpeed = maxSpeed# generic max speed for this type of vehicles
#Vehicle Type Class Ends Here
#-------------------------------------------------------






#-------------------------------------------------------
#Engine Class Starts Here
class Engine:
    id=0

    def __init__(self, fuelType,givenName,unitFuelConsumption, emissionCO, emissionTHC, emissionVOC, emissionNOx, emissionHCNOx, emissionP,emissionPN):
        Engine.id += 1
        self.name = givenName
        self.fuel=fuelType #type of the fuel
        self.unitFuelConsumption = unitFuelConsumption #unit consumption of volume per km
        #all the emissions are g/km except PN (number/km)
        self.emissionCO=emissionCO #carbon monoxide
        self.emissionTHC=emissionTHC #total hydrocarbon
        self.emissionVOC=emissionVOC #volatile organic compounds
        self.emissionNOx=emissionNOx #Nitrogene Oxide
        self.emissionHCNOx=emissionHCNOx # Hydrocarbone + Nitrogene Oxide
        self.emissionP=emissionP # particules
        self.emissionPN=emissionPN # particule Number

#Engine Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#Fuel  Class Starts Here
class Fuel:
    id=0

    def __init__(self, givenName, unitPrice, unitVolume):
        Fuel.id +=1
        self.id=Fuel.id
        self.name=givenName
        self.price = unitPrice
        self.volume = unitVolume
#Fuel Class Ends Here
#-------------------------------------------------------








