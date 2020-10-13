from typing import List
import numpy as np
import ColaPrioridad 
import math as mt


class listeishon:
    
    
    def __init__(self) -> None:
        self.listeishon = []
    
    def search_KNN(self, point: np.ndarray, n: int ):
        auxNode = self.root
        stack = []
        queue = ColaPrioridad()
        stack.append(auxNode)

        cont = 0
        for data in self.listeishon:
            nodeFinally = stack[0]
            node = stack.pop()
            if node is None:
                break               

            if len(queue)<=n:  
                pointDistance = self.distance(point,node.point)
                maxDistance   = self.distance(point,nodeFinally.point)
                if (pointDistance - maxDistance) < 0:
                    queue.push(node,pointDistance)
        
        
           
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



        

    
    