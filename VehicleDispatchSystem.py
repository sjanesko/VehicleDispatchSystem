import Graph
import Vehicles
import VRequests
import pprint

# Creates and fills Graph with stored data
g = Graph.Graph()
g.fillGraph()

# Gets array of vehicles
vehicleArr = Vehicles.vehicleArray()

# Gets array of requests
requestsArr = VRequests.reqArr()

pprint.pprint(vehicleArr)
pprint.pprint(requestsArr)
pprint.pprint(g.vertDict)
