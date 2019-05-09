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


if __name__ == '__main__':
    g = Graph()
    g.addVert('a')
    g.addVert('b')
    g.addVert('c')
    g.addVert('d')
    g.addVert('e')
    g.addVert('f')

    g.addEdge('a', 'b', 7)
    g.addEdge('a', 'c', 9)
    g.addEdge('a', 'f', 14)
    g.addEdge('b', 'c', 10)
    g.addEdge('b', 'd', 15)
    g.addEdge('c', 'd', 11)
    g.addEdge('c', 'f', 2)
    g.addEdge('d', 'e', 6)
    g.addEdge('e', 'f', 9)

    print(g.vertDict['a'].getAdjNodes())
