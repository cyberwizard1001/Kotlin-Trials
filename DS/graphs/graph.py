"""The code is borrowed from the book "Problem Solving with Algorithms and Data Structures"
   http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html
   
"""
#from binheap import BinHeap
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
 #       self.front=[]
 #       self.back=[]
 #       self.depfs=[]
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):  #f is from node, t is to node
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def printdfs(self):
    	return
    
    def __iter__(self):
    	return iter(self.vertList.values())
    """
    Write a method to generate an adjacency matrix representation of the graph
    """
    def createAdjMatrix(self):
        return 

    """
    Write a method to traverse the graph using dfs from start node. 
    The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or backward edge.
    """
    def dfs(self,stnode):
        return
        
    """
    Write a method to traverse the graph using bfs from start node.  The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or cross edge.
    """
    def bfs(self,stnode):
        return
    
    """
    Write a method to generate the minimum spanning tree of the graph using Kruskal algorithm
    """
    def mstKruskal(self):
        return
