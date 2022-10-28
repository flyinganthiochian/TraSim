import random
from Vehicle import *


#-------------------------------------------------------
#Driver Class Starts Here

class Driver:
    id=0

    def __init__(self):
        Driver.id +=1
        self.id=Driver.id
        self.deceleration={"min":1, "max":2} #minimum and maximum deceleration allowed for a driver (cellSpeed per Step)
    def __repr__(self):
        return ("Driver id: {id}".format(id=self.id))
    def setDriverVehicle(self,vehicle):

        self.vehicle = vehicle
        Vehicle.setVehicleDriver(self)
    def setDriverType(self,type):
        self.type=type
    def setDriverFollowingDistanceRandimizerCoefficient(self):
        #NOTE: this method can ONLY be called after the driver type is assigned
        #This method sets the Random coefficient for safe driving distance
        #this coefficient is added to the minimum safe distance in order to calculate 
        #preffered following distance for the particular Driver
        try:
            randomDenominator = random.choice[10,15,20,25]
            self.followingDistanceRandomCoefficient=round(self.type.cautiousness/randomDenominator)
        except:
            print(self + "'s setDriverFollowingDistanceRandimizerCoefficient didn't work")
           



#Vehicle Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#DriverType Class Starts Here

class DriverType:
    id=0

    def __init__(self,name,patienceCoefficient,aggressivenessCoefficient,cautiousnessCoefficient):
        DriverType.id +=1
        self.id=DriverType.id
        self.name=name
        self.patience=patienceCoefficient #per cent
        self.aggressiveness=aggressivenessCoefficient #per cent
        self.cautiousness=cautiousnessCoefficient # per cent
        
    def __repr__(self):
        return ("DriverType id: {id}, name: {name}".format(id=self.id,name=self.name))
    
#DriverType Class Ends Here
#-------------------------------------------------------