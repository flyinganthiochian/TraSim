import math
import copy
from Demand import Route
#-------------------------------------------------------
# Network Class Starts Here
class Network:
    """This is the main Class for Network elements
    All Simulations will have 1 network"""
    id=0
    

    def __init__(self,givenSimulation):
        self.nodeList =[] #all the nodes of this network will be stored in this list
        self.roadList=[] #all the roads of this network will be stored in this list
        self.connectorList=[] #all the connectors of the network will be stored in this list
        Network.id +=1
        self.id=Network.id #id of the network is given by the creation order
        givenSimulation.network=self #network is set as the simulation's network
        self.simulation = givenSimulation
        self.routeList=[] # this list will hold the all the routes of the network
    def createRoadLaneCells(self):

        for roadCounter in range(len(self.roadList)):
            Lane.createRoadLanes(self.roadList[roadCounter])

    

    def createSiouxFallsNetwork(currentSimulation):
        #this method creates default Sioux-Falls network
        siouxFallsNetwork = Network(currentSimulation)

        #below all the nodes of the Sioux-Falls network is created
        Node.createSiouxFallsNodes(siouxFallsNetwork)
        Road.createSiouxFallsRoads(siouxFallsNetwork)
        siouxFallsNetwork.createRoadLaneCells()
    
    def createBasicNetwork1(currentSimulation):
        #this method creates the basic test network number 1
        # 5 Nodes 12 Roads
        siouxFallsNetwork = Network(currentSimulation)

        #below all the nodes of the Sioux-Falls network is created
        Node.createBasicNetwork1Nodes(siouxFallsNetwork)
        Road.createBasicNetwork1Roads(siouxFallsNetwork)
        siouxFallsNetwork.createRoadLaneCells()
        Connector.createBasicNetwork1Connectors(siouxFallsNetwork)

        #calculate all possibleRoutes in the network
        #for startNode in siouxFallsNetwork.nodeList:
        #   siouxFallsNetwork.findRoutesFromNode(startNode)
            


    def setRouteRoadListFromNodeList(self,nodeList,route):
        roadList=[]
        for counter in range(0,len(nodeList)-1):

                startNode=nodeList[counter]
                endNode=nodeList[counter+1]
                road = Road.getRoadByNodes(self,startNode,endNode)
                roadList.append(road)
        route.roadList=copy.deepcopy(roadList)

                    
        
    
    def updateQueueAndVisitedList(self,queueList, visitedNodeList):
        

        if len(queueList[-1]) == 0:
             route = Route()
             route.setRouteOrigin(visitedNodeList[-1][0])
             route.setRouteDestination(visitedNodeList[-1][-1])
             self.setRouteRoadListFromNodeList(visitedNodeList[-1],route)
             route.nodeList=copy.deepcopy(visitedNodeList)
             self.routeList.append(route)
             queueList.pop()
             visitedNodeList.pop()
             queueList[-1].pop(0)
             
        else:
            currentNode=queueList[-1][0]
            visitedNodesInStep=copy.deepcopy(visitedNodeList[-1])
            visitedNodesInStep.append(currentNode)
            visitedNodeList.append(visitedNodesInStep)
            connectedList=copy.deepcopy(currentNode.connectedNodeList)
            nodeToRemove=[]
            for connectedNode in connectedList:
                if connectedNode in visitedNodesInStep:
                    nodeToRemove.append(connectedNode)
            if len(nodeToRemove)>0:
                for node in nodeToRemove:
                    connectedList.remove(node)
            queueList.append(connectedList)
        





    
    def findRoutesFromNode(self,node):

        #this method finds routes from the given node (startNode) to all other nodes on the network (self)
        visitedNodesInStep=[]
        visitedNodesInStep.append(node)
        visitedNodeList=[]
        queueList=[]
        queuedNodesInStep=copy.deepcopy(node.connectedNodeList)
        
        queueList.append(queuedNodesInStep)
        visitedNodeList.append(visitedNodesInStep)
        while len(queueList) > 0:
            self.updateQueueAndVisitedList(queueList,visitedNodeList)
        
       
        
        
        
        
        
        
        
            

               
               



                





#Network Class Ends Here
#-------------------------------------------------------


#-------------------------------------------------------
#Node Class Starts Here
class Node:
    id=0
    
    


    def __init__(self,givenNetwork,givenAbcissa,givenOrdinate,givenElevation=0,givenName="") -> None:
        Node.id +=1
        self.id=Node.id #id of the node is given by the order of creation
        self.abcissa = givenAbcissa #X coordinate of the Node in meters
        self.ordinate = givenOrdinate # Y coordinate of the Node in meters
        self.elevation = givenElevation #elevation above the Sea Level (experimental feature)
        self.name = givenName #set the user name as the Node name
        self.inRoadList=[]#all the roads which ends in this Node will be hold in this List<>
        self.outRoadList=[]#all the roads which starts in this Node will be hold in this List<>
        self.connectedNodeList=[] # all the connected nodes to this node. This list is updated eveytime a road which starts from this Node is created
        self.connectorList=[] #all the connectors are in this list
        
        if self.name == "":
            self.name = str(Node.id) #if no name is given then  the node ID is set as the Node name
        givenNetwork.nodeList.append(self) #this node is added to the nodeList of the Network
    
    def __repr__(self):
        return ("Node id: {id}".format(id=self.id))
    def __eq__(self, other):
        return self.id == other.id
    def createSiouxFallsNodes(network):
        #this method creates all the nodes of default sioux Falls network
        #Sioux-Falls network consists of 24 Nodes
        node1 = Node(network,0,0)
        node2 = Node(network,6000,0)
        node3 = Node(network,0,-2000)
        node4 = Node(network,2000,-2000)
        node5 = Node(network,4000,-2000)
        node6 = Node(network,6000,-2000)
        node7 = Node(network,8000,-4000)
        node8 = Node(network,6000,-4000)
        node9 = Node(network,4000,-4000)
        node10 = Node(network,4000,-6000)
        node11 = Node(network,2000,-6000)
        node12 = Node(network,0,-6000)
        node13 = Node(network,0,-14000)
        node14 = Node(network,2000,-10000)
        node15 = Node(network,4000,-10000)
        node16 = Node(network,6000,-6000)
        node17 = Node(network,6000,-8000)
        node18 = Node(network,8000,-6000)
        node19 = Node(network,6000,-10000)
        node20 = Node(network,6000,-14000)
        node21 = Node(network,4000,-14000)
        node22 = Node(network,4000,-12000)
        node23 = Node(network,2000,-12000)
        node24 = Node(network,2000,-14000)
    def createBasicNetwork1Nodes(network):
        # this method will create 5 Nodes of the basic network number 1
        node1 = Node(network,0,0)
        node2 = Node(network,0,5000)
        node3 = Node(network,5000,5000)
        node4 = Node(network,0,10000)
        node5 = Node(network,-5000,5000)



#Node Class Ends Here
#-------------------------------------------------------





#-------------------------------------------------------
#Road Class Starts Here
class Road:
    id=0 

    def __init__(self, givenNetwork,givenStartingNode,givenEndingNode,givenNumberOfLanes=1, givenName="",givenLength=0, givenPrice=0, givenSpeedLimit =0):
        Road.id +=1
        self.roadPrice=givenPrice
        self.id=Road.id #id of the Road is given by the order of creation
        self.laneList = [] #all the lanes will be stored in this List<>
        self.startingNode=givenStartingNode #road's starting node is set
        self.endingNode=givenEndingNode #road's ending node is set
        self.numberOfLanes=givenNumberOfLanes #number of lanes is set
        self.speedLimit = givenSpeedLimit # max Allowed speed limit for the road
        
        defaultLength=self.calculateDefaultRoadLength() # calculating road length by given Node coordinates
        #below in the inside if case it checked whether the given Length is
        #less than the calculated default length
        #given length CAN NOT be less than the shortest distance between nodes
        #in this case length of the road is equal to the line distance between nodes
        #but given length can be bigger than the line distance
        #in this case road length is equal to the user defined length
        if givenLength < defaultLength:
            self.length = defaultLength
        else:
            self.length=givenLength

        self.slope=self.calculateDefaultRoadSlope() #road's slope is set (+ values for incline, - values for decline as percentage)

        #here we check if the user is given a specific Name for the Road
        #if Not Road will be named with the IDs of the starting and ending Nodes
        #letter F than Starting Node ID, letter T and than ending Node ID
        #for example if the Road is starting from node ID 1 and end at the Node ID 2
        #the name of the Road Will be F1T2...
        if givenName == "":
            self.name="F"+str(givenStartingNode.id)+"T"+str(givenEndingNode.id)
        else:
            self.name=givenName
        givenStartingNode.connectedNodeList.append(givenEndingNode) # here we add the ending node to the starting node's connected nodes list            
        self.network=givenNetwork
        self.setNumberOfRoadCells() #calculates and sets the number of Cell property of Road

        
        givenNetwork.roadList.append(self)
    def __repr__(self):
        return ("F"+str(self.startingNode.id)+"T"+str(self.endingNode.id))
    def setNumberOfRoadCells(self):
        #this method takes road lengths in meters and sets the number of Cell property of Road
        self.numberOfCells=round(self.length/self.network.simulation.cellLength)
    def calculateDefaultRoadLength(givenRoad):
        #this method calculates the Road's length by using the Node's abcissa and ordinate
        #and sets the value as Road's length
        #!!This method should be called after the Road's starting and ending Node's are created
        #lenth between two nodes is = sqrt((x1-x2)**2+(y1-y2)**)
        
        length=math.sqrt((givenRoad.startingNode.abcissa-givenRoad.endingNode.abcissa)**2 + (givenRoad.startingNode.ordinate-givenRoad.endingNode.ordinate)**2)
        length = round(length)
        return length

    def calculateDefaultRoadSlope(givenRoad):
        #this method calculates the slope of the given road by using the elevation of starting and ending Nodes
        # formula -> slope = ((elevation2 -elevation1)*100/length)
        #it returns the slope in percantage
        #IMPORTANT!! This Method can be called only after the road length is SET

        
        slope = ((givenRoad.startingNode.elevation-givenRoad.endingNode.elevation)*100)/givenRoad.length
        return slope
    def createRoadLanes(self):
        for laneCounter in range(self.numberOfLanes):
            createdLane=Lane(self)
    
    def getRoadByNodes(network,startingNode,endingNode):
        #this method returns the road between given Nodes

        for road in network.roadList:
            if road.startingNode == startingNode and road.endingNode==endingNode:
                ourRoad = road
                break
            else:
                ourRoad=None
        return ourRoad


    def createSiouxFallsRoads(network):
        #this method creates all the roads of the default Sioux Falls Network
        #Sioux falls Network consists of 76 roads

        #creating roads starting from Node 1
        road12=Road(network,network.nodeList[0],network.nodeList[1],3)
        
        road21=Road(network,network.nodeList[1],network.nodeList[0],3)

        road13=Road(network,network.nodeList[0],network.nodeList[2],3)
        road31=Road(network,network.nodeList[2],network.nodeList[0],3)

        road26=Road(network,network.nodeList[1],network.nodeList[5],3)
        road62=Road(network,network.nodeList[5],network.nodeList[1],3)

        road34=Road(network,network.nodeList[2],network.nodeList[3],3)
        road43=Road(network,network.nodeList[3],network.nodeList[2],3)

        road312=Road(network,network.nodeList[2],network.nodeList[11],3)
        road122=Road(network,network.nodeList[11],network.nodeList[2],3)

        road45=Road(network,network.nodeList[3],network.nodeList[4],3)
        road54=Road(network,network.nodeList[4],network.nodeList[3],3)

        road411=Road(network,network.nodeList[3],network.nodeList[10],3)
        road114=Road(network,network.nodeList[10],network.nodeList[3],3)

        road56=Road(network,network.nodeList[4],network.nodeList[5],3)
        road65=Road(network,network.nodeList[5],network.nodeList[4],3)

        road59=Road(network,network.nodeList[4],network.nodeList[8],2)
        road95=Road(network,network.nodeList[8],network.nodeList[4],2)

        road68=Road(network,network.nodeList[5],network.nodeList[7],2)
        road86=Road(network,network.nodeList[7],network.nodeList[5],2)

        road78=Road(network,network.nodeList[6],network.nodeList[7],2)
        road87=Road(network,network.nodeList[7],network.nodeList[6],2)

        road718=Road(network,network.nodeList[6],network.nodeList[17],2)
        road187=Road(network,network.nodeList[17],network.nodeList[6],2)

        road89=Road(network,network.nodeList[7],network.nodeList[8],2)
        road98=Road(network,network.nodeList[8],network.nodeList[7],2)

        road816=Road(network,network.nodeList[7],network.nodeList[15],2)
        road168=Road(network,network.nodeList[15],network.nodeList[7],2)

        road910=Road(network,network.nodeList[8],network.nodeList[9],2)
        road109=Road(network,network.nodeList[9],network.nodeList[8],2)

        road1011=Road(network,network.nodeList[9],network.nodeList[10],2)
        road1110=Road(network,network.nodeList[10],network.nodeList[9],2)

        road1015=Road(network,network.nodeList[9],network.nodeList[14],2)
        road1510=Road(network,network.nodeList[14],network.nodeList[9],2)

        road1016=Road(network,network.nodeList[9],network.nodeList[15],2)
        road1610=Road(network,network.nodeList[15],network.nodeList[9],2)

        road1017=Road(network,network.nodeList[9],network.nodeList[16],2)
        road1710=Road(network,network.nodeList[16],network.nodeList[9],2)

        road1112=Road(network,network.nodeList[10],network.nodeList[11],2)
        road1211=Road(network,network.nodeList[11],network.nodeList[10],2)

        road1114=Road(network,network.nodeList[10],network.nodeList[13],2)
        road1411=Road(network,network.nodeList[13],network.nodeList[10],2)

        road1213=Road(network,network.nodeList[11],network.nodeList[12],2)
        road1312=Road(network,network.nodeList[12],network.nodeList[11],2)

        road1324=Road(network,network.nodeList[12],network.nodeList[23],2)
        road2413=Road(network,network.nodeList[23],network.nodeList[12],2)

        road1415=Road(network,network.nodeList[13],network.nodeList[14],2)
        road1514=Road(network,network.nodeList[14],network.nodeList[13],2)

        road1423=Road(network,network.nodeList[13],network.nodeList[22],2)
        road2314=Road(network,network.nodeList[22],network.nodeList[13],2)

        road1519=Road(network,network.nodeList[14],network.nodeList[18],2)
        road1915=Road(network,network.nodeList[18],network.nodeList[14],2)

        road1522=Road(network,network.nodeList[14],network.nodeList[21],2)
        road2215=Road(network,network.nodeList[21],network.nodeList[14],2)

        road1617=Road(network,network.nodeList[15],network.nodeList[16],2)
        road1716=Road(network,network.nodeList[16],network.nodeList[15],2)

        road1618=Road(network,network.nodeList[15],network.nodeList[17],2)
        road1816=Road(network,network.nodeList[17],network.nodeList[15],2)

        road1719=Road(network,network.nodeList[16],network.nodeList[18],2)
        road1917=Road(network,network.nodeList[18],network.nodeList[16],2)

        road1820=Road(network,network.nodeList[17],network.nodeList[19],2)
        road2018=Road(network,network.nodeList[19],network.nodeList[17],2)

        road1920=Road(network,network.nodeList[18],network.nodeList[19],2)
        road2019=Road(network,network.nodeList[19],network.nodeList[18],2)

        road2021=Road(network,network.nodeList[19],network.nodeList[20],2)
        road2120=Road(network,network.nodeList[20],network.nodeList[19],2)

        road2022=Road(network,network.nodeList[19],network.nodeList[21],2)
        road2220=Road(network,network.nodeList[21],network.nodeList[19],2)

        road2122=Road(network,network.nodeList[20],network.nodeList[21],2)
        road2221=Road(network,network.nodeList[21],network.nodeList[20],2)

        road2124=Road(network,network.nodeList[20],network.nodeList[23],2)
        road2421=Road(network,network.nodeList[23],network.nodeList[20],2)

        road2223=Road(network,network.nodeList[21],network.nodeList[22],2)
        road2322=Road(network,network.nodeList[22],network.nodeList[21],2)

        road2324=Road(network,network.nodeList[22],network.nodeList[23],2)
        road2423=Road(network,network.nodeList[23],network.nodeList[22],2)

    def createBasicNetwork1Roads(network):
        #this method will create 14 roads of the Basic Test Network 1
        road12=Road(network,network.nodeList[0],network.nodeList[1],2)
        road21=Road(network,network.nodeList[1],network.nodeList[0],2)

        road13=Road(network,network.nodeList[0],network.nodeList[2],2)
        road31=Road(network,network.nodeList[2],network.nodeList[0],2)

        road23=Road(network,network.nodeList[1],network.nodeList[2],2)
        road32=Road(network,network.nodeList[2],network.nodeList[1],2)

        road24=Road(network,network.nodeList[1],network.nodeList[3],2)
        road42=Road(network,network.nodeList[3],network.nodeList[1],2)

        road25=Road(network,network.nodeList[1],network.nodeList[4],2)
        road52=Road(network,network.nodeList[4],network.nodeList[1],2)

        road34=Road(network,network.nodeList[2],network.nodeList[3],2)
        road43=Road(network,network.nodeList[3],network.nodeList[2],2)

        road45=Road(network,network.nodeList[3],network.nodeList[4],2)
        road54=Road(network,network.nodeList[4],network.nodeList[3],2)

#Road Class Ends Here
#-------------------------------------------------------





#-------------------------------------------------------
#Lane Class Starts Here
class Lane:
    id=0
    

    def __init__(self,givenRoad):
        Lane.id +=1
        self.id = Lane.id
        self.cellList = []
        self.road=givenRoad


    def createRoadLanes(givenRoad):

        for counter in range(givenRoad.numberOfLanes):
            
            givenRoad.laneList.append(Lane(givenRoad))
            Cell.createLaneCells(givenRoad.laneList[counter])
#Lane Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#Cell Class Starts Here
class Cell:
    id=0

    def __init__(self,givenLane):
        Cell.id +=1
        self.id = Cell.id
        
        self.lane=givenLane
    
    def createLaneCells(givenLane):
        for cellCounter in range(givenLane.road.numberOfCells):
            #print("Number of Cells = " + str(givenLane.road.numberOfCells))
            givenLane.cellList.append(Cell(givenLane))
#Cell Class Ends Here
#-------------------------------------------------------

#-------------------------------------------------------
#Connector Class Starts Here
class Connector:
    id=0

    def __init__(self,inRoad,outRoad,connectionType="S"):
        Connector.id +=1
        self.id =Connector.id
        self.node=inRoad.endingNode # this is the node that the connector is located inRoad's ending node 
        self.inRoad=inRoad #road that enters the connector
        self.outRoad=outRoad #road that leaves the connector
        self.connectionType=connectionType #S for straight R for Right Turn L for Left Turn, U for U turn
        inRoad.endingNode.connectorList.append(self)
    def __repr__(self):
        return ("Connector id: {id}| from road: {sRoad} to road :{eRoad} type: {type}".format(id=self.id, sNode=self.inRoad, eNode=self.outRoad, type=self.connectionType))
    
    def createBasicNetwork1Connectors(network):
        con12_23=Connector(network.roadList[0],network.roadList[4],"R")
        con12_24=Connector(network.roadList[0],network.roadList[6],"S")
        con12_25=Connector(network.roadList[0],network.roadList[8],"L")
        
        con13_34=Connector(network.roadList[2],network.roadList[10],"S")
        con13_32=Connector(network.roadList[2],network.roadList[5],"L")

        con21_13=Connector(network.roadList[1],network.roadList[2],"S")

        con23_34=Connector(network.roadList[4],network.roadList[10],"L")
        con23_31=Connector(network.roadList[4],network.roadList[3],"R")

        con24_43=Connector(network.roadList[6],network.roadList[11],"R")
        con24_45=Connector(network.roadList[6],network.roadList[12],"L")

        con31_12=Connector(network.roadList[3],network.roadList[0],"S")
        con32_21=Connector(network.roadList[5],network.roadList[1],"L")
        con32_24=Connector(network.roadList[5],network.roadList[6],"R")
        con34_42=Connector(network.roadList[10],network.roadList[7],"L")
        con34_45=Connector(network.roadList[10],network.roadList[12],"S")

        con42_23=Connector(network.roadList[7],network.roadList[4],"L")
        con42_21=Connector(network.roadList[7],network.roadList[1],"S")
        con42_25=Connector(network.roadList[7],network.roadList[8],"R")

        con43_32=Connector(network.roadList[11],network.roadList[5],"R")
        con43_31=Connector(network.roadList[11],network.roadList[3],"S")

        con52_21=Connector(network.roadList[9],network.roadList[1],"R")
        con52_23=Connector(network.roadList[9],network.roadList[4],"S")
        con52_24=Connector(network.roadList[9],network.roadList[6],"L")

        con54_42=Connector(network.roadList[13],network.roadList[7],"R")
        con54_43=Connector(network.roadList[13],network.roadList[11],"S")



        
        
#Connector Class Ends Here
#-------------------------------------------------------



