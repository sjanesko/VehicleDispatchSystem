# Graph template code from https://www.bogotobogo.com/python/python_graph_data_structures.php
import math


class Vertex:
    def __init__(self, node):
        self.zipcode = node
        self.adjacent = {}
        self.visited = False
        self.distance = math.inf
        self.previous = None

    def __repr__(self):
        return str(self.zipcode) + ' adjacent: ' + str([x.zipcode for x in self.adjacent])

    def addAdjacentVertex(self, node, weight):
        self.adjacent[node] = weight

    def getAdjNodes(self):
        return self.adjacent.keys()

    def getZipcode(self):
        return self.getZipcode

    def getWeight(self, node):
        return self.adjacent[node]

    def setPrev(self, current):
        self.previous = current

    def getPrev(self, current):
        return self.previous


class Graph:
    def __init__(self):
        self.vertDict = {}
        self.numVerts = 0

    def __iter__(self):
        return iter(self.vertDict.values())

    def addVert(self, node):
        self.numVerts = self.numVerts + 1
        newVert = Vertex(node)
        self.vertDict[node] = newVert
        return newVert

    def addEdge(self, firstNode, secondNode, cost=0):
        if firstNode not in self.vertDict:
            self.addVert(firstNode)
        if secondNode not in self.vertDict:
            self.addVert(secondNode)

        # Add both paths since its undirected
        self.vertDict[firstNode].addAdjacentVertex(self.vertDict[secondNode], cost)
        self.vertDict[secondNode].addAdjacentVertex(self.vertDict[firstNode], cost)

    def getVerts(self):
        return self.vertDict.keys()

    def resetGraph(self):
        for vert in self.vertDict:
            vert.visited = False
            vert.distance = math.inf

    def fillGraph(self):
        '''Hard coded zipCode graph'''
        # First row of zipCodes
        self.addVert('64111')
        self.addVert('64112')
        self.addVert('64113')
        self.addVert('64114')
        self.addVert('64115')

        # Second row of zipCodes
        self.addVert('65111')
        self.addVert('65112')
        self.addVert('65113')
        self.addVert('65114')
        self.addVert('65115')

        # Third row of zipCodes
        self.addVert('65211')
        self.addVert('65212')
        self.addVert('65213')
        self.addVert('65214')
        self.addVert('65215')

        # Fourth row of zipCodes
        self.addVert('66111')
        self.addVert('66112')
        self.addVert('66113')
        self.addVert('66114')
        self.addVert('66115')

        # Fifth row of zipCodes
        self.addVert('67311')
        self.addVert('67312')
        self.addVert('67313')
        self.addVert('67314')
        self.addVert('67315')

        # Add edges for first row of zipCodes
        self.addEdge('64111', '64112', 3)
        self.addEdge('64112', '64113', 7)
        self.addEdge('64113', '64114', 2)
        self.addEdge('64114', '64115', 1)

        self.addEdge('64111', '65111', 9)
        self.addEdge('64112', '65112', 1)
        self.addEdge('64113', '65113', 3)
        self.addEdge('64114', '65114', 7)
        self.addEdge('64115', '65115', 2)

        # Add edges for second row of zipCodes
        self.addEdge('65111', '65112', 2)
        self.addEdge('65112', '65113', 5)
        self.addEdge('65113', '65114', 11)
        self.addEdge('65114', '65115', 10)

        self.addEdge('65111', '65211', 1)
        self.addEdge('65112', '65212', 2)
        self.addEdge('65113', '65213', 1)
        self.addEdge('65114', '65214', 2)
        self.addEdge('65115', '65215', 4)

        # Add edges for third row of zipCodes
        self.addEdge('65211', '65212', 8)
        self.addEdge('65212', '65213', 3)
        self.addEdge('65213', '65214', 5)
        self.addEdge('65214', '65215', 1)

        self.addEdge('65211', '66111', 3)
        self.addEdge('65212', '66112', 2)
        self.addEdge('65213', '66113', 6)
        self.addEdge('65214', '66114', 7)
        self.addEdge('65215', '66115', 4)

        # Add edges for fourth row of zipCodes
        self.addEdge('66111', '66112', 7)
        self.addEdge('66112', '66113', 1)
        self.addEdge('66113', '66114', 4)
        self.addEdge('66114', '66115', 2)

        self.addEdge('66111', '67311', 4)
        self.addEdge('66112', '67312', 3)
        self.addEdge('66113', '67313', 7)
        self.addEdge('66114', '67314', 1)
        self.addEdge('66115', '67315', 3)

        # Add edges for fifth row of zipCodes
        self.addEdge('67311', '67312', 1)
        self.addEdge('67312', '67313', 5)
        self.addEdge('67313', '67314', 10)
        self.addEdge('67314', '67315', 11)

        # print(self.vertDict['test'].getAdjNodes())


if __name__ == '__main__':
    g = Graph()
    g.fillGraph()
