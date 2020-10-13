import numpy as np

class Node:
    def __init__(self,data,point: np.ndarray,hijoDerecho=None, hijoIzquierdo=None):
        self.node_right = hijoDerecho
        self.node_left = hijoIzquierdo
        self.data = data
        self.point = point


    def children(self):
        if self.node_left and self.node_left.data is not None:
            return self.node_left, 0
        if self.node_right and self.node_right.data is not None:
            return self.node_right, 1

    def getLeft(self):
        return self.node_left

    def getRight(self):
        return self.node_right

    def get_data(self):
        return self.data

    def get_id(self):
        return self.data[0]
    
    def get_name(self):
        return self.data[1]

    def print_data(self):
        print("id:\t", self.data[0])
        print("App Name:\t", self.data[1])
        print("App Size:\t", (int(self.data[2])/1000000), " MB")
        print("Genre:\t", self.data[11])
        print("Price:\t$", self.data[4], self.data[3])









