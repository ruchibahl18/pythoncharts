import matplotlib.pyplot as plt
import numpy as np
import sys
from mpl_toolkits.mplot3d import Axes3D

class MyPlot:
    def __init__(self, type_of_graph, clr, data):
        self.type_of_graph = type_of_graph
        self.clr = clr
        self.data = data
    
    def plot_graph(self):
        #fig = plt.figure()
        #ax = fig.gca(projection='3d')

        if self.type_of_graph == 1:
            plt.hist(self.data[0], color=self.clr)
        elif self.type_of_graph == 2:
            plt.bar(self.data[0],self.data[1], color=self.clr)
        elif self.type_of_graph == 3:
            plt.scatter(self.data[0],self.data[1], color=self.clr)
        elif self.type_of_graph == 4:
            plt.plot(self.data[0],self.data[1], color=self.clr)
        elif self.type_of_graph == 5:
            plt.hist(self.data[0], color=self.clr)
        elif self.type_of_graph == 6:
            plt.pie(self.data[0])
        else:
            print("Incorrect input")
        plt.show()
        
        