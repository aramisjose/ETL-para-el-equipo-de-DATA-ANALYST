import pandas as pd
from fastapi import FastAPI

#Extrames el csv creado en el cuaderno de transformaciones
data = pd.read_csv('datos_plataformas.csv')


##creo un objecto de la clase fastapi
apply = FastAPI()



##1Esta funcion retornara la cantidad de veces que aparece una keyword por plataforma

@apply.get("/Cantidad de veces que aparece una keyword en una plataforma por peliculas/series")
def get_word_count(plataforma,keyword):
    plataforma = plataforma.lower() #usamos la funcion lower para cambiar todo a minusculas en caso de que el usuario ingrese mayusculas
    keyword = keyword.lower() ##usamos la funcion lower para cambiar todo a minusculas en caso de que el usuario ingrese mayusculas
        
    if plataforma == 'netflix':
        veces = list(data['show_id'].str.contains('n') & data['title'].str.contains(keyword))
        return plataforma, veces.count(True)
        
    elif plataforma == 'amazon':
        veces = list(data['show_id'].str.contains('a') & data['title'].str.contains(keyword))
        return plataforma, veces.count(True)
        
    elif plataforma == 'hulu':
        veces = list(data['show_id'].str.contains('h') & data['title'].str.contains(keyword))
        return plataforma, veces.count(True)
        
    elif plataforma == 'disney':
        veces = list(data['show_id'].str.contains('d') & data['title'].str.contains(keyword))
        return plataforma, veces.count(True)
        
    else:
        return 'no existe esta plataforma de peliculas en la base de datos'
    
#2
@apply.get("/Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año")
def get_score_count(plataforma,score,year):
    plataforma = plataforma.lower() #usamos la funcion lower para cambiar todo a minusculas en caso de que el usuario ingrese mayusculas
        
    if plataforma == 'netflix':
        veces = data[(data['show_id'].str.contains('n')) & (data['score'] > score) & (data['release_year'] == year)]
        return plataforma, veces.shape[0]
        
    elif plataforma == 'amazon':
        veces = data[(data['show_id'].str.contains('a')) & (data['score'] > score) & (data['release_year'] == year)]
        return plataforma, veces.shape[0]
        
    elif plataforma == 'hulu':
        veces = data[(data['show_id'].str.contains('h')) & (data['score'] > score) & (data['release_year'] == year)]
        return plataforma, len(veces)
        
    elif plataforma == 'disney':
        veces = data[(data['show_id'].str.contains('d')) & (data['score'] > score) & (data['release_year'] == year)]
        return plataforma, len(veces)
        
    else:
        return 'No existe esta plataforma en la base de datos'
    
#3
@apply.get("/La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.")
def get_second_score(plataforma):
    try:
        plataforma = plataforma.lower() #cambiamos todo el parametro a minusculas esto es por si acaso el usuario ingresa alguna letra mayuscula
        
        if plataforma == 'netflix':
            filtro = data[data['show_id'].str.contains('n')].sort_values(by=['score'], ascending=False)
            return filtro.iloc[1,2], filtro.iloc[1,12]
        
        elif plataforma == 'disney':
            filtro = data[data['show_id'].str.contains('d')].sort_values(by=['score'], ascending=False)
            return filtro.iloc[1,2], filtro.iloc[1,12]
        
        elif plataforma == 'amazon':
            filtro = data[data['show_id'].str.contains('a')].sort_values(by=['score'], ascending=False)
            return filtro.iloc[1,2], filtro.iloc[1,12]
        
        elif plataforma == 'hulu':
            filtro = data[data['show_id'].str.contains('h')].sort_values(by=['score'],ascending=False)
            return filtro.iloc[1,2], filtro.iloc[1,12]
        
        else:
            return "No existe la plataforma que ingresaste en la base de datos"
    except:
        print("Error! ha ingresado mal el parametro")


#4 Se creará una función que retorne la pelicula que más duró, según la plataforma que ingrese el usuario
@apply.get("/Película que más duró según año, plataforma y tipo de duración")
def get_longest(plataforma,time,year):
    try:
        plataforma = plataforma.lower() #normalizamos el parametro plataforma que ingrese el usuario a minusculas

        if plataforma == 'netflix':
            filtro = data[(data['show_id'].str.contains('n')) &
                          (data['release_year'] == year) &
                          (data['duration_type'] == time)].sort_values(by=['duration_int'], ascending=False)
            return filtro.iloc[0]['title'], filtro.iloc[0]['duration_int'], filtro.iloc[0]['duration_type']
        
        elif plataforma == 'amazon':
            filtro = data[(data['show_id'].str.contains('a')) &
                          (data['release_year'] == year) &
                          (data['duration_type'] == time)].sort_values(by=['duration_int'], ascending = False)
            return filtro.iloc[0]['title'], filtro.iloc[0]['duration_int'], filtro.iloc[0]['duration_type']
        
        elif plataforma == 'hulu':
            filtro = data[(data['show_id'].str.contains('h')) &
                          (data['release_year'] == year) &
                          (data['duration_type'] == time)].sort_values(by=['duration_int'], ascending=False)
            return filtro.iloc[0]['title'], filtro.iloc[0]['duration_int'], filtro.iloc[0]['duration_type']
        
        elif plataforma == 'disney':
            filtro = data[(data['show_id'].str.contains('d')) &
                          (data['release_year'] == year) &
                          (data['duration_type'] == time)].sort_values(by=['duration_int'], ascending=False)
            return filtro.iloc[0]['title'], filtro[0]['duration_int'], filtro[0]['duration_type']
        
        else:
            print("No existe la plataforma que ingresaste en la base de datos")
    except:
        print("Error! ha ingresado mal los parametros.")
    
    
#5 Creare la función que retorne la cantidad de series y peliculas por rating
@apply.get("/Cantidad de peliculas y series por rating")
def get_rating_count(rating):
    suma = 0
    if data['rating'].isin([rating]).any():
        for item in data['rating']:
            if item == rating:
                suma +=1  
        return rating, suma
    else:
        return 'No existe el rating ingresado en la base de datos'
    







