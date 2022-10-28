#-------------------------------------------------------
#SimulationUnit  Class Starts Here
from this import d
from turtle import st


class SimulationUnit:
    #this class holds the Units of the Simulation (Length, Volume, Currency etc)
    def __init__(self, givenName, distance=[], mass=[], time=[] ,speed=[], acceleration=[], force=[], energy=[], power=[], volume=[], currency=[]):
        self.name = givenName
        self.distance = distance
        self.mass = mass
        self.time = time
        self.speed = speed
        self.acceleration = acceleration
        self.force = force
        self.energy= energy
        self.power = power
        self.volume = volume
        self.currency = currency
    

    def setDefaultPossibleSimUnits(givenSimulation):
        defaultCurrencyList = Currency.createDefaultSimCurrencies()
        defaultDistanceList=Distance.createDefaultSimDistances()
        defaultTimeList=Time.createDefaultSimTimes()
        defaultMassList=Mass.createDefaultSimMass()
        defaultSpeedList = Speed.createDefaultSimSpeed()   
        defaultAccelerationList=Acceleration.createDefaultSimAcceleration()
        defaultVolumeList = Volume.createDefaultSimVolume()

        defaultSimulationUnit = SimulationUnit("Default Possible Units",defaultDistanceList,defaultMassList, defaultTimeList,defaultSpeedList, defaultAccelerationList, [],[],[],defaultVolumeList,defaultCurrencyList)
        givenSimulation.possibleUnits=defaultSimulationUnit
#SimulationUnit Class Ends Here
#-------------------------------------------------------



#-------------------------------------------------------
#Currency  Class Starts Here
class Currency:
    id=0

    def __init__(self,givenName, givenSymbol, turkishLiraRate):
        Currency.id +=1
        self.id = Currency.id
        self.name=givenName #name of the currency
        self.symbol=givenSymbol #symbol of the currency
        self.turkishLiraRate=turkishLiraRate # equavalent Turkish Lira of unit this currency for exp: 18.50 for US Dollar
    def __repr__(self) -> str:
        return ("Currency Unit: {name}({symbol})".format(name=self.name,symbol=self.symbol))
    def createDefaultSimCurrencies():

        #this method creates US DOllar, Turkish Lira and Euro currencies as default
        defaultCurrencyList=[]
        dollar = Currency("US Dollar", "$", 18.50)
        tl= Currency("Turkish Lira", "TL", 1)
        euro = Currency("Euro", "€", 1.02)
        defaultCurrencyList.append(dollar)
        defaultCurrencyList.append(tl)
        defaultCurrencyList.append(euro)
        return defaultCurrencyList

#Currency Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#distance  Class Starts Here
class Distance:
    def __init__(self, givenName, symbol, equivalentMeter) -> None:
        self.name = givenName
        self.symbol = symbol
        self.equivalentMeter = equivalentMeter # for cantimeter this will be 0.01
    def __repr__(self) -> str:
        return ("Distance Unit: {name}({symbol})".format(name=self.name,symbol=self.symbol))
    def createDefaultSimDistances():
        #this method creates meter and kilometer distance units for default sim values

        defaultDistanceList = []

        meter=Distance("Meters", "m", 1)
        kilometer=Distance("Kilometers", "km", 1000)
        defaultDistanceList.append(meter)
        defaultDistanceList.append(kilometer)

        return defaultDistanceList

#distance Class Ends Here
#-------------------------------------------------------



#-------------------------------------------------------
#Time  Class Starts Here
class Time:
    def __init__(self,givenName, symbol, equivalentSeconds):
        self.name=givenName
        self.symbol = symbol
        self.equivalentSeconds=equivalentSeconds
    def __repr__(self) -> str:
        return ("Time Unit: {name}({symbol})".format(name=self.name,symbol=self.symbol))
    def createDefaultSimTimes():
        defaultTimeList=[]
        seconds = Time("seconds", "s",1)
        minutes = Time("minutes", "m", 60)
        hour = Time("hour", "hr", 3600)

        defaultTimeList.append(seconds)
        defaultTimeList.append(minutes)
        defaultTimeList.append(hour)
        return defaultTimeList
#Time Class Ends Here
#-------------------------------------------------------



#-------------------------------------------------------
#mass  Class Starts Here
class Mass:
    def __init__(self,givenName, symbol, equivalentGram):
        self.name=givenName
        self.symbol = symbol
        self.equivalentGram=equivalentGram
    def __repr__(self) -> str:
        return ("Mass Unit: {name}({symbol})".format(name=self.name,symbol=self.symbol))
    def createDefaultSimMass():
        defaultMassList=[]
        miligram = Mass("miligram", "mg",0.001)
        gram = Mass("gram", "gr", 1)
        kilogram = Mass("kilogram", "kg", 1000)

        defaultMassList.append(miligram)
        defaultMassList.append(gram)
        defaultMassList.append(kilogram)
        return defaultMassList
#mass Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#Speed  Class Starts Here
class Speed:
    def __init__(self,givenName, symbol, equivalentKPH):
        self.name=givenName
        self.symbol = symbol
        self.equivalentKPH=equivalentKPH
    def __repr__(self) -> str:
        return ("Speed Unit: {name}({symbol})".format(name=self.name,symbol=self.symbol))
    def createDefaultSimSpeed():
        defaultSpeedList=[]
        kph = Speed("Kilometers per Hour", "km/h",1)
        meterPs = Speed("meters per Second", "m/s", 3.6)
        

        defaultSpeedList.append(kph)
        defaultSpeedList.append(meterPs)
        
        return defaultSpeedList
#Speed Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#distance  Class Starts Here
class Acceleration:
    def __init__(self,givenName, symbol, equivalentMetersPerSeconds2):
        self.name=givenName
        self.symbol = symbol
        self.equivalentMetersPerSeconds2=equivalentMetersPerSeconds2
    def __repr__(self) -> str:
        return ("Acceleration Unit: {name}({symbol})".format(name=self.name,symbol=self.symbol))
    def createDefaultSimAcceleration():
        defaultAccelerationList=[]
        
        meterPs2 = Acceleration("meters per Second square", "m/s^2", 1)
        

        defaultAccelerationList.append(meterPs2)
        
        
        return defaultAccelerationList
#distance Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#distance  Class Starts Here
class Volume:
    def __init__(self,givenName, symbol, equivalentliter):
        self.name=givenName
        self.symbol = symbol
        self.equivalentliter=equivalentliter
    def __repr__(self) -> str:
        return ("Volume Unit: {name}({symbol})".format(name=self.name,symbol=self.symbol))
    def createDefaultSimVolume():
        defaultVolumeList=[]
        
        liter = Volume("Liter", "l", 1)
        cc = Volume("cubic cantimeter", "cc", 0.001)
        mc = Volume("cubic meter", "m^3", "1000")

        defaultVolumeList.append(liter)
        defaultVolumeList.append(cc)
        
        
        return defaultVolumeList
#distance Class Ends Here
#-------------------------------------------------------