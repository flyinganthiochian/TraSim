import datetime
from Unit import *
from Network import Network
from Network import Node
from Network import Road
from Network import Lane
from Network import Cell
from Test import Test


class Simulation:
    currentStep=0
    print("\n\n=================================================================")
    print("Welcome to [C]ellular [A]utomata [T]raffic [S]imulation - CATS")
    print("=================================================================")
    
    def __init__(self,givenSimDuration=100, givenSimLength=5):
        self.simDuration=givenSimDuration #number of simulation steps
        self.cellLength=givenSimLength #length of each cell in meters
        
        SimulationUnit.setDefaultPossibleSimUnits(self)

        
         
        
        self.defaultDriverTypes=[] # List<> of default simulation driver types
        self.defaultVehicleTypes=[] # List<> of default Vehicle types
        self.preSimVehiclelist=[] # List<> of vehicles that not started in their journeys
        self.activeSimvehicleList=[] # List<> of vehicles currently active in the sim
        self.postSimVehicleList=[] # List <> of vehicles that endded their journeys
        
    def updateSimulationStep(self):
        #this method will update sim one step
        self.currentStep +=1 #here the current step is increased by 1
        #Test.printCurrentSimStep(self)

    def calculateSimulationElapsedTime(self):
        #this method will calculate and update the simulation's elapsed time at the end of the simulation
        timeDifference=self.endTime-self.startTime #this is the difference between two dateTimes
        #Below this difference will be converted to minutes and seconds
        self.elapsedTime = divmod(timeDifference.seconds, 60)

    def makeInitialTests(self):
        #this method will print Simulator parameters (default or user defined values) at the beginning of the simulation
        print("\n==================================================")
        print("Simulation is Started With The Following Parameters")
        Test.printDefaultSimParameters(self)
        Test.printCurrentSimParameters(self)
        print("\n==================================================")


    def makeEndTests(self):
        #this method will do the tests after the simulation is finished

        #total simulation elapsed time is printed

        print("\n==================================================")
        print("Simulation is Ended With The Following Parameters")
        Test.printSimulationElapsedTime(self)
        print("\n==================================================")

    def makeNetworkTests(self):
        print("\n==================================================")
        print("This Network has Following Elements")
        print("\n*****Node INFO*****")
        Test.printNetworkNodeInfo(self)
        Test.printNetworkRoadInfo(self)
        Test.printNetworkRouteInfo(self)


