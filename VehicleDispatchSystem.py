import Graph
import Vehicles
import VRequests
import pprint


def findVehicles(type, zipcode, graph):
    '''Finds all available vehicles that match type if available'''
    # Select vehicle needed if available
    availableVehicles = [v for v in vehicleArr if v.type == type and v.available]

    if availableVehicles:
        # Call dijkstras algorithm and find distances from
        # every node starting at given zipcode
        graph.dijkstra(zipcode)

        # Sets vehicle distance using distance calculated by dijkstras
        for v in availableVehicles:
            v.distance = g.vertDict[v.vehicleZipCode].distance
        # Sort the array in place
        availableVehicles.sort(key=lambda x: x.distance)
    return availableVehicles


# Creates and fills Graph with stored data
g = Graph.Graph()
g.fillGraph()

# Gets array of vehicles
vehicleArr = Vehicles.vehicleArray()

# Gets array of requests
requestsArr = VRequests.reqArr()

# Iterate through all requests(requests are in order of call time (ID))
for r in requestsArr:

    # Retrieves vehicles and their distances from the zipcode
    availableVehiclesArr = findVehicles(r.type, r.reqZipCode, g)

    # Make vehicle unavailable
    availableVehiclesArr[0].available = False

    # First index will be the min result since array is sorted
    r.vehicleID = availableVehiclesArr[0].id
    r.distance = availableVehiclesArr[0].distance

for r in requestsArr:
    pprint.pprint(r)
