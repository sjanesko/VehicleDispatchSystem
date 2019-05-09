import Graph
import Vehicles
import pprint
# Creates and fills Graph with stored data
g = Graph.Graph()
g.fillGraph()

# Gets array of vehicles
vehicleArr = Vehicles.vehicleArray()


pprint.pprint(vehicleArr)
pprint.pprint(g.vertDict)
