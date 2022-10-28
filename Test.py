
from Network import Network
from Network import Node
from Network import Road
from Network import Lane
from Network import Cell
class Test:


    def __init__(self):
        pass

    def printDefaultSimParameters(currentSim):
        print("\n***TEST-printDefaultSimParameters STARTS***")
        print("-------------------------------------")
        print("Default duration of the current sim = {duration} steps".format(duration=currentSim.simDuration))
        print("Default length of each cell in the current sim = {length} meters".format(length=currentSim.cellLength))
        Test.printDefaultSimUnites(currentSim)


        print("-------------------------------------")
        print("***TEST-printDefaultSimParameters ENDS***\n")

    def printCurrentSimParameters(currentSim):
        print("\n***TEST-printCurrentSimParameters STARTS***")
        print("-------------------------------------")
        print("Duration of the current sim = {duration} steps".format(duration=currentSim.simDuration))
        print("Length of each cell in the current sim = {length} meters".format(length=currentSim.cellLength))
        print("-------------------------------------")
        print("***TEST-printCurrentSimParameters ENDS***\n")
    def printCurrentSimStep(currentSim):
        print("\n***TEST-printCurrentSimStep STARTS***")
        print("-------------------------------------")
        print("Current Step = {step}".format(step=currentSim.currentStep))
        print("-------------------------------------")
        print("***TEST-printCurrentSimStep ENDS***\n")
    
    def printSimulationElapsedTime(currentSim):
        #this method gets the currentSim.elapsedTime property 
        #and prints the elapsed time in minutes and seconds
        print('Total elapsed time = : ', currentSim.elapsedTime[0], 'minutes',currentSim.elapsedTime[1], 'seconds')


    
    
    
    
    def printNetworkNodeInfo(currentSim):
        #this method will print number of nodes info and ID of each node
        print("\n***TEST-printNetworkNodeInfo STARTS***")
        print("-------------------------------------")
        print("Total number of Nodes in this network is = {node}".format(node=len(currentSim.network.nodeList)))
        for nodeID in currentSim.network.nodeList:
            print("Node ID= {id}".format(id=nodeID.id))

        print("-------------------------------------")
        print("***TEST-printNetworkNodeInfo ENDS***")
    
    def printNetworkRoadInfo(currentSim):
        #this method prints the IDs, names, lengths and Slope of the Roads
        print("\n***TEST-printNetworkRoadInfo STARTS***")
        print("-------------------------------------")
        print("Total number of Roads in this network is = {node}".format(node=len(currentSim.network.roadList)))
        for Road in currentSim.network.roadList:
            print("| Name= {name} | Lane needed = {laneNum} | Lane = {lane} | cellNum = {cellNum}".format(name=Road.name, laneNum=Road.numberOfLanes, lane=len(Road.laneList), cellNum=len(Road.laneList[0].cellList)))

        print("-------------------------------------")
        print("***TEST-printNetworkRoadInfo ENDS***")
    def printNetworkRouteInfo(currentSim):
        print("\n***TEST-printNetworkRouteInfo STARTS***")
        print("-------------------------------------")
        print("Total number of Roads in this network is = {node}".format(node=len(currentSim.network.roadList)))
        for route in currentSim.network.routeList:
            routePath=""
            for node in route.nodeList:
                routePath = routePath + " " + str(node.id) +" "
            print("| Route id= {id} | Origin = {origin} | Destination= {destination} | path = {path}".format(id=route.id, origin=route.origin, destination=route.destination, path=routePath))

        print("-------------------------------------")
        print("***TEST-printNetworkRouteInfo ENDS***")
    def printDefaultSimUnites(currentSim):
        print("\nxxTest printDefaultSimUnitesxx")
        print("\n ---Currency Units--- ")
        if len(currentSim.possibleUnits.currency)>0:
            for unit in currentSim.possibleUnits.currency:
                print(unit)
        print("\n ---Distance Units--- ")
        if len(currentSim.possibleUnits.distance)>0:
            for unit in currentSim.possibleUnits.distance:
                print(unit)
        print("\n ---Time Units--- ")
        if len(currentSim.possibleUnits.time)>0:
            for unit in currentSim.possibleUnits.time:
                print(unit)
        print("\n ---Mass Units--- ")
        if len(currentSim.possibleUnits.mass)>0:
            for unit in currentSim.possibleUnits.mass:
                print(unit)
        print("\n ---Speed Units--- ")
        if len(currentSim.possibleUnits.speed)>0:
            for unit in currentSim.possibleUnits.speed:
                print(unit)
        print("\n ---Acceleration Units--- ")
        if len(currentSim.possibleUnits.acceleration)>0:
            for unit in currentSim.possibleUnits.acceleration:
                print(unit)
        print("\n ---Volume Units--- ")
        if len(currentSim.possibleUnits.volume)>0:
            for unit in currentSim.possibleUnits.volume:
                print(unit)
        print("\nxxTest printDefaultSimUnitesxx")