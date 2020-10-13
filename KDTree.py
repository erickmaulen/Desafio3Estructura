import pandas as pd
from Node import Node
import numpy as np
import math as mt
from ColaPrioridad import ColaPrioridad

K = 7

class KDTree(Node):
    root : Node

    def __init__(self, data=None):
        self.root = None
 
    def insert(self,point: np.ndarray, data : np.ndarray):  
        auxNode = self.root
        contDim = 0      
        while True:
            if self.root is None:
                self.root = Node(data, point)
                break
            
            if(point[contDim] < auxNode.point[contDim]):
                if (auxNode.node_left is None):
                    auxNode.node_left = Node(data, point)
                    break
                else:
                    auxNode = auxNode.node_left
            else:
                if (auxNode.node_right is None):
                    auxNode.node_right = Node(data, point)
                    break
                else:
                    auxNode = auxNode.node_right
            contDim += 1
            if(contDim >= 28):
                contDim = 0
        


    def search_KNN(self, point: np.ndarray, n: int ):
        auxNode = self.root
        stack = []
        queue = ColaPrioridad()
        stack.append(auxNode)

        cont = 0
        while(len(stack)>0):
            nodeFinally = stack[0]
            node = stack.pop()
            if node is None:
                break               

            if len(queue)<=n:  
                pointDistance = self.distance(point,node.point)
                maxDistance   = self.distance(point,nodeFinally.point)
                if (pointDistance - maxDistance) < 0:
                    queue.push(node,pointDistance)
                
            if (point[cont]-node.point[cont]) < 0:
                stack.append(node.node_right)
                stack.append(node.node_left)

            else:
                stack.append(node.node_left)
                stack.append(node.node_right)

            cont +=1
            if cont >= 28:
                cont = 0
            
        #Retorna la cola como una lista, para poder
        #ser transformada a una lista de aplicaciones.
        return queue.as_list()


    def distance(self, point1,point2):
        distancia = 0
        for i in range(0,28): #Ese 5 dependeria de las dimensiones del vector   (caracteristicas)
            distancia += (point1[i] - point2[i])**2

        return mt.sqrt(distancia)


    def search(self, point: np.ndarray):
        auxNode = self.root
        contDim = 0      
        while True:
            if (auxNode.point == point).all():
                auxNode.print_data()
                break
            
            if(point[contDim] < auxNode.point[contDim]):
                if (auxNode.node_left is None):
                    print('No existe una aplicacion con esa ID o Nombre.')
                    break
                else:
                    auxNode = auxNode.node_left
            else:
                if (auxNode.node_right is None):
                    print('No existe una aplicacion con esa ID o Nombre.')
                    break
                else:
                    auxNode = auxNode.node_right
            contDim += 1
            if(contDim >= 28):
                contDim = 0

    













