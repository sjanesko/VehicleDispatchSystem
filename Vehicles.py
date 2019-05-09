class Vehicle:
    def __init__(self, id, type, zipCode):
        self.id = id
        self.type = type
        self.zipCode = zipCode

    def __repr__(self):
        return ("ID: " + str(self.id) + ' ' + "Type: " + str(self.type) + ' ' + "Zipcode: " + self.zipCode)


def vehicleArray():
    '''Returns array full vehicles'''
    vehicleArr = []

    # Place Ambulances
    vehicleArr.append(Vehicle(1, 1, '64112'))
    vehicleArr.append(Vehicle(4, 1, '65214'))
    vehicleArr.append(Vehicle(7, 1, '66113'))
    vehicleArr.append(Vehicle(10, 1, '66111'))

    # Place Fire Trucks
    vehicleArr.append(Vehicle(2, 2, '64115'))
    vehicleArr.append(Vehicle(5, 2, '67312'))
    vehicleArr.append(Vehicle(8, 2, '65212'))
    vehicleArr.append(Vehicle(11, 2, '67315'))

    # Place Police car
    vehicleArr.append(Vehicle(3, 3, '65113'))
    vehicleArr.append(Vehicle(6, 3, '65111'))
    vehicleArr.append(Vehicle(9, 3, '66114'))
    vehicleArr.append(Vehicle(12, 3, '67313'))

    return vehicleArr
