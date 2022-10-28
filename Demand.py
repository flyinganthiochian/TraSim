


#-------------------------------------------------------
#Route Class Starts Here

class Route:
    id=0

    def __init__(self):
        Route.id +=1
        self.id = Route.id
        self.nodeList=[]
        self.roadList=[]
        

    def __repr__(self) :
        return ("Route id: {id}, from {sNode} to {eNode}".format(id=self.id, sNode=self.origin, eNode=self.destination))
    
    def setRouteOrigin(self,startNode):
        self.origin=startNode
    def setRouteDestination(self,endNode):
        self.destination=endNode
    
    
        




    




    
            

                

            


                

                
                

        


        
           
                    
                
                     




            


                

                        

            

#Route Class Ends Here
#-------------------------------------------------------