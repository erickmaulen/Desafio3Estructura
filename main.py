from CvsHandler import DataHandler
from KDTree import KDTree
import os
import numpy as np
import pandas as pd

#Para borrar la pantalla
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

tree = KDTree()
datos = DataHandler()
points = datos.get_points()

print('Loading Dataset...')
cont=0
for data in datos.data.values:
    #Insert into KDTree
    tree.insert(points.values[cont], data)
    cont+=1
print('Dataset Loaded.')

#Menu de Switch bien nitido
while True:
    cls()
    print('Que deseas hacer?')
    print('a : Buscar Información por ID o Nombre')
    print('b : Buscar 10 más parecidas por ID')
    print('c : Buscar 10 más parecidas por datos')
    print('x : Salir')
    print('Ingrese la opcion: ', end='')

    option = input()

    if option == 'x':
        break    
    elif option == 'a':
        print('Ingresa el nombre o la ID: ', end='')
        idorname = input() 
        if idorname.isnumeric():
            index = datos.data.index[datos.data['id'] == int(idorname)]
            if len(index) > 0:
                index = index[0]
        else:
            index = datos.data.index[datos.data['track_name'] == idorname]
            if len(index) > 0:
                index = index[0]

        if type(index) == np.int64 and index <= points.size:
            #Existe y es un numero, por lo tanto seguimos la busqueda...
            #Obtenemos el punto a traves de points
            tree.search(points.values[int(index)])
        else:
            print('No se encontro App con esa ID o Nombre!')

    elif option == 'b':
        print('Ingresa la ID: ', end='')
        idorname = input() 
        if idorname.isnumeric():
            index = datos.data.index[datos.data['id'] == int(idorname)]
            if len(index) > 0:
                index = index[0]
                if type(index) == np.int64 and index <= points.size:
                    #Existe y es un numero, por lo tanto seguimos la busqueda...
                    #Obtenemos el punto a traves de points
                    apps = tree.search_KNN(points.values[index],10)
                    for app in apps:
                        app[1].print_data()

        else:
            print('Esa ID no es valida. Ingrese SOLO NUMEROS')
    elif option == 'c':
        dictPoint = {}

        print('Ingrese tamano en bytes: ', end='')
        inp = input()
        try:
            dictPoint['size_bytes'] =[float(inp)]
        except ValueError:
            print('El valor no es correcto. Saliendo...')
            break

        print('Ingrese el Precio: ', end='')
        inp = input()
        try:
            dictPoint['price'] = [float(inp)]
        except ValueError:
            print('El valor no es correcto. Saliendo...')
            break

        print('Ingrese el rating de usuarios: ', end='')
        inp = input()
        try:
            dictPoint['user_rating'] = [float(inp)]
        except ValueError:
            print('El valor no es correcto. Saliendo...')
            break

        print('Ingrese la cantidad de dispositivos soportados: ', end='')
        inp = input()
        try:
            dictPoint['sup_devices.num'] =[float(inp)]
        except ValueError:
            print('El valor no es correcto. Saliendo...')
            break

        print('Ingrese la cantidad de lenguajes disponibles: ', end='')
        inp = input()
        try:
            dictPoint['lang.num'] =[float(inp)]
        except ValueError:
            print('El valor no es correcto. Saliendo...')
            break

        print('Ahora, deberas ingresar el genero que deseas que tenga: ')
        
        #Se inicializan los puntos... De un manera muy bonita (:
        dictPoint['prime_genre_Book'] = [0]
        dictPoint['prime_genre_Business'] = [0]
        dictPoint['prime_genre_Catalogs'] = [0]
        dictPoint['prime_genre_Education'] = [0]
        dictPoint['prime_genre_Entertainment'] = [0]
        dictPoint['prime_genre_Finance'] = [0]
        dictPoint['prime_genre_Food & Drink'] = [0]
        dictPoint['prime_genre_Games'] = [0]
        dictPoint['prime_genre_Health & Fitness'] = [0]
        dictPoint['prime_genre_Lifestyle'] = [0]
        dictPoint['prime_genre_Medical'] = [0]
        dictPoint['prime_genre_Music'] = [0]
        dictPoint['prime_genre_Navigation'] = [0]
        dictPoint['prime_genre_News'] = [0]
        dictPoint['prime_genre_Photo & Video'] = [0]
        dictPoint['prime_genre_Productivity'] = [0]
        dictPoint['prime_genre_Reference'] = [0]
        dictPoint['prime_genre_Shopping'] = [0]
        dictPoint['prime_genre_Social Networking'] = [0]
        dictPoint['prime_genre_Sports'] = [0]
        dictPoint['prime_genre_Travel'] = [0]
        dictPoint['prime_genre_Utilities'] = [0]
        dictPoint['prime_genre_Weather'] = [0]

        #Dejamos de intentarlo, perdon
        print('Book = 0')
        print('Business = 1')
        print('Catalogs = 2')
        print('Education = 3')
        print('Entertainment = 4')
        print('Finance = 5')
        print('Food & Drink = 6')
        print('Games = 7')
        print('Health & Fitness = 8')
        print('Lifestyle = 9')
        print('Medical = 10')
        print('Music = 11')
        print('Navigation = 12')
        print('News = 13')
        print('Photo & Video = 14')
        print('Productivity = 15')
        print('Reference = 16')
        print('Shopping = 17')
        print('Social Networking = 18')
        print('Sports = 19')
        print('Travel = 20')
        print('Utilities = 21')
        print('Weather = 22')
        print('Cual quieres que sea?: ', end='')
        try:
            value = [float(input())+5]
        except ValueError:
            print('El valor no es correcto. Saliendo...')
            break
        
        cont = 0
        for key in dictPoint:
            if value == cont:
                dictPoint[key] = 1
                break
            cont += 1

        #Get the array of data, and we normalize it.
        pandaQuery = pd.DataFrame.from_dict(dictPoint)

        pandaQuery['price'] = (pandaQuery['price']-datos.data['price'].min())/(datos.data['price'].max()-datos.data['price'].min())

        pandaQuery['size_bytes'] = (pandaQuery['size_bytes']-datos.data['size_bytes'].min())/(datos.data['size_bytes'].max()-datos.data['size_bytes'].min())

        pandaQuery['user_rating'] = (pandaQuery['user_rating']-datos.data['user_rating'].min())/(datos.data['user_rating'].max()-datos.data['user_rating'].min())

        pandaQuery['sup_devices.num'] = (pandaQuery['sup_devices.num']-datos.data['sup_devices.num'].min())/(datos.data['sup_devices.num'].max()-datos.data['sup_devices.num'].min())

        pandaQuery['lang.num'] = (pandaQuery['lang.num']-datos.data['lang.num'].min())/(datos.data['lang.num'].max()-datos.data['lang.num'].min())

        #It's normalized with min/max data of the points array.

        pointToSearch = pandaQuery.values[0]

        print('=== TOP 10 MAS CERCANOS POR DROSS ===')
        apps = tree.search_KNN(pointToSearch, 10)
        for app in apps:
            app[1].print_data()

    print('Enter para continuar...') 
    input()
    



#tree.searchName('猎魔传奇-塔塔&推塔挂机私服手游')
    
#"8447","1108939718","猎魔传奇-塔塔&推塔挂机私服手游",255946752,"USD",0,0,0,0,0,"1.2.3","12+","Games",40,5,1,1

# tree = KDTree()
# 
# for dato in datos.values:
#     tree.insert(tree.root.point,dato,0)




#def insert(self, point, data : np.ndarray, depth : int):  