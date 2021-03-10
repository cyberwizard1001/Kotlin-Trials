import networkx as nx
import matplotlib.pyplot as plt

class City:
    def __init__(self,start,end,name,time):
        self.name = name
        self.start = start
        self.end = end
        self.time = time
         
lst = []
lst.append(City(2,0,"rue-de-londers",1))
lst.append(City(0,1,"rue-d-amsterdam",1))
lst.append(City(3,1,"rue-d-athenes",1))
lst.append(City(2,3,"rue-d-rome",2))
lst.append(City(1,2,"rue-d-moscou",3))

G = nx.DiGraph()
for i in lst: #work in progress
    G.add_edges_from([(i.start,i.end)])