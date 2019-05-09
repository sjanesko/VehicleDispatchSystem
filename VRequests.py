class Requests():
    def __init__(self, id, type, zipCode, vehicleID, distance):
        self.id = id
        self.type = type
        self.zipCode = zipCode
        self.vehicleID = None
        self.distance = distance

    def setDist(self, dist):
        self.distance = distance

    def setVehicleID(self, vid):
        self.vehicleID = vid
