class Request():
    def __init__(self, id, type, zipcode):
        self.id = id
        self.type = type
        self.reqZipCode = zipcode
        self.vehicleID = None
        self.distance = 0

    def setDist(self, dist):
        self.distance = distance

    def setVehicleID(self, vid):
        self.vehicleID = vid

    def __repr__(self):
        return ("ID: " + str(self.id) + " Type: " + str(self.type) + " Zipcode: " + self.reqZipCode + " VehicleID: " + str(self.vehicleID) + " Distance: " + str(self.distance))


def reqArr():
    '''Returns request array'''
    reqArr = []

    # Request ID order randomized
    # Place Ambulances reqs
    reqArr.append(Request(9, 1, '64111'))
    reqArr.append(Request(4, 1, '64114'))
    reqArr.append(Request(1, 1, '65213'))
    reqArr.append(Request(11, 1, '67311'))

    # Place Fire Truck reqs
    reqArr.append(Request(10, 2, '67314'))
    reqArr.append(Request(8, 2, '65215'))
    reqArr.append(Request(3, 2, '64113'))
    reqArr.append(Request(5, 2, '65115'))

    # Place Police car reqs
    reqArr.append(Request(12, 3, '65112'))
    reqArr.append(Request(7, 3, '65212'))
    reqArr.append(Request(2, 3, '66112'))
    reqArr.append(Request(6, 3, '66115'))

    # Sort array by ID
    reqArr.sort(key=lambda x: x.id)

    return reqArr
