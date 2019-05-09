class Request():
    def __init__(self, id, type, zipCode):
        self.id = id
        self.type = type
        self.zipCode = zipCode
        self.vehicleID = None
        self.distance = 0

    def setDist(self, dist):
        self.distance = distance

    def setVehicleID(self, vid):
        self.vehicleID = vid

    def __repr__(self):
        return ("ID: " + str(self.id) + " Type: " + str(self.type) + " Zipcode: " + self.zipCode + " VehicleID: " + str(self.vehicleID) + " Distance: " + str(self.distance))


def reqArr():
    '''Returns request array'''
    reqArr = []

    # Request ID order randomized
    # Place Ambulances reqs
    reqArr.append(Request(9, 1, '64112'))
    reqArr.append(Request(4, 1, '65214'))
    reqArr.append(Request(1, 1, '66113'))
    reqArr.append(Request(11, 1, '66111'))

    # Place Fire Truck reqs
    reqArr.append(Request(10, 2, '64115'))
    reqArr.append(Request(8, 2, '67312'))
    reqArr.append(Request(3, 2, '65212'))
    reqArr.append(Request(5, 2, '67315'))

    # Place Police car reqs
    reqArr.append(Request(12, 3, '65113'))
    reqArr.append(Request(7, 3, '65111'))
    reqArr.append(Request(2, 3, '66114'))
    reqArr.append(Request(6, 3, '67313'))

    # Sort array by ID
    reqArr.sort(key=lambda x: x.id)

    return reqArr
