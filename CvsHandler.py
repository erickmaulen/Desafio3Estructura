import pandas as pd
import numpy as np

class DataHandler:
    data : pd.DataFrame

    def __init__(self):
        datos = pd.read_csv('Desafio3.csv',engine='python',index_col=0)
        datos = datos.replace(np.nan,"0")
        
        #Retorna los nombres de las columnas y los valores.
        #Aqui se reinician los indices que tiene el CSV, porque 
        #algunos estan desordenados
        #ademas, se eliminara la columna de indices :)
        self.data = datos.reset_index().drop(axis=0, columns='index')

    def get_points(self):
        primegenre_dummy = pd.get_dummies(self.data['prime_genre'], prefix="prime_genre")
        datos = pd.concat([self.data, primegenre_dummy], axis = 1)

        points = datos.loc[
            :,
            ['size_bytes', 
            'price', 
            'user_rating',
            'sup_devices.num',
            'lang.num',
            'prime_genre_Book', 'prime_genre_Business', 'prime_genre_Catalogs',
            'prime_genre_Education', 'prime_genre_Entertainment',
            'prime_genre_Finance', 'prime_genre_Food & Drink', 'prime_genre_Games',
            'prime_genre_Health & Fitness', 'prime_genre_Lifestyle',
            'prime_genre_Medical', 'prime_genre_Music', 'prime_genre_Navigation',
            'prime_genre_News', 'prime_genre_Photo & Video',
            'prime_genre_Productivity', 'prime_genre_Reference',
            'prime_genre_Shopping', 'prime_genre_Social Networking',
            'prime_genre_Sports', 'prime_genre_Travel', 'prime_genre_Utilities',
            'prime_genre_Weather'
            ]
        ]

        #norm = (points-points.min())/(points.max()-points.min())
        #(df-df.min())/(df.max()-df.min())
        points['price'] = ((points['price'] - points['price'].min())/(points['price'].max()-points['price'].min()))

        points['size_bytes'] = ((points['size_bytes'] - points['size_bytes'].min())/(points['size_bytes'].max()-points['size_bytes'].min()))

        points['user_rating'] = ((points['user_rating'] - points['user_rating'].min())/(points['user_rating'].max()-points['user_rating'].min()))

        points['sup_devices.num'] = ((points['sup_devices.num'] - points['sup_devices.num'].min())/(points['sup_devices.num'].max()-points['sup_devices.num'].min()))

        points['lang.num'] = ((points['lang.num'] - points['lang.num'].min())/(points['lang.num'].max()-points['lang.num'].min()))

        return points



