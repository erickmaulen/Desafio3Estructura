from typing import List
import numpy as np
from ColaPrioridad import ColaPrioridad
import math as mt


class listeishon:
    
    
    def __init__(self) -> None:
        self.listeishon = []
    
    def search_KNN(self, point: np.ndarray, n: int ):
        
        queue = ColaPrioridad()
        distanceMaxFinally = 0
        distanceAux= 0

        for data in self.listeishon:         
            distanceAux = self.distance(point,data.point)
            print(distanceAux)
            if distanceAux > distanceMaxFinally:
                distanceMaxFinally = distanceAux
                
        print(distanceMaxFinally)      

        for data in self.listeishon:
            if len(queue)<=n:  
                pointDistance = self.distance(point,data.point)
                if (pointDistance - distanceMaxFinally) < 0:
                    queue.push(data,pointDistance)
                    

        
        #Retorna la cola como una lista, para poder
        #ser transformada a una lista de aplicaciones.
        return queue.as_list()


    def distance(self, point1,point2):
        distancia = 0
        for i in range(0,28): #Ese 5 dependeria de las dimensiones del vector   (caracteristicas)
            distancia += (point1[i] - point2[i])**2

        return mt.sqrt(distancia)



        

    
    