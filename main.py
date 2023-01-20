import pandas as pd
from fastapi import FastAPI

##Aqui abro el archivo csv ya limpio
data = pd.read_csv('data_plataformas_movies.csv')

##creo un objecto de la clase fastapi
app = FastAPI()


##Esta funcion retornara la cantidad de veces que aparece una keyword por plataforma

@app.get("/Cantidad de veces que aparece una keyword en una plataforma por peliculas/series")
def get_word_count(plataforma,keyword):
    parametro1 = plataforma.lower()
    if parametro1 == 'nexflix' or parametro1 == 'neflix':
        lista = list(data['id'].str.contains('n') & data['title'].str.contains(keyword))
        lista2 = []
        for item in lista:
            if item == True:
                lista2 = lista2 + [item]
        return parametro1, len(lista2)
    elif parametro1 == 'amazon':
        lista = list(data['id'].str.contains('a') & data['title'].str.contains(keyword))
        lista2 = []
        for item in lista:
            if item == True:
                lista2 = lista2 + [item]
        return parametro1, len(lista2)
    elif parametro1 == 'hulu':
        lista = list(data['id'].str.contains('h') & data['title'].str.contains(keyword))
        lista2 = []
        for item in lista:
            if item == True:
                lista2 = lista2 + [item]
        return parametro1, len(lista2)
    elif parametro1 == 'disney':
        lista = list(data['id'].str.contains('d') & data['title'].str.contains(keyword))
        lista2 = []
        for item in lista:
            if item == True:
                lista2 = lista2 + [item]
        return parametro1, len(lista2)
    else:
        return 'No existe la plataforma que buscas en nuestra base de datos'
    
    

## Aquí la segunda función devuelve la cantidad de peliculas por plataforma con un puntaje mayor al que el usuario ingrese

@app.get("/Cantidad de peliculas con un score mayor a que el usuario ingrese en un año determinado")
def get_score_count(plataforma,puntaje:int,anio:int):
    parametro1 = plataforma.lower()
    if parametro1 == 'nexflix' or parametro1 == 'neflix':
        data_filtro = data[(data['id'].str.contains('n')) & (data['score'] > puntaje)]
        data_filtro2 = data_filtro['release_year']
        lista_anios = list(data_filtro2)
        lista = []
        for item in lista_anios:
            if item == anio:
                lista = lista + [item]
        return parametro1, len(lista)
    elif parametro1 == 'hulu':
        data_filtro = data[(data['id'].str.contains('h')) & (data['score'] > puntaje)]
        data_filtro2 = data_filtro['release_year']
        lista_anios = list(data_filtro2)
        lista = []
        for item in lista_anios:
            if item == anio:
                lista = lista + [item]
        return parametro1, len(lista)
    elif parametro1 == 'disney':
        data_filtro = data[(data['id'].str.contains('d')) & (data['score'] > puntaje)]
        data_filtro2 = data_filtro['release_year']
        lista_anios = list(data_filtro2)
        lista = []
        for item in lista_anios:
            if item == anio:
                lista = lista + [item]
        return parametro1, len(lista)
    elif parametro1 == 'amazon':
        data_filtro = data[(data['id'].str.contains('a')) & (data['score'] > puntaje)]
        data_filtro2 = data_filtro['release_year']
        lista_anios = list(data_filtro2)
        lista = []
        for item in lista_anios:
            if item == anio:
                lista = lista + [item]
        return {parametro1, len(lista)}
    else:
        return 'No existe la plataforma que ingresaste en nuestra base de datos'
    

    
    
## Esta función retorna la pelicula con mayor score según la plataforma que el usuario ingrese

@app.get("/Segunda Pelicula con mayor score para una plataforma determinada")
def get_second_score(plataforma):
    parametro = plataforma.lower()
    if parametro == 'nexflix' or plataforma == 'neflix':
        data_filtrado = data[(data['id'].str.contains('n'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        df_filtrado3 = data_filtrado2.sort_values('title',ascending=True)
        pelicula = df_filtrado3.iloc[1]['title']
        puntaje = df_filtrado3.iloc[1]['score']
        return pelicula, puntaje
    elif parametro == 'amazon':
        data_filtrado = data[(data['id'].str.contains('a'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        df_filtrado3 = data_filtrado2.sort_values('title',ascending=True)
        pelicula = df_filtrado3.iloc[1]['title']
        puntaje = df_filtrado3.iloc[1]['score']
        return pelicula, puntaje
    elif parametro == 'hulu':
        data_filtrado = data[(data['id'].str.contains('h'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        df_filtrado3 = data_filtrado2.sort_values('title',ascending=True)
        puntaje = df_filtrado3.iloc[1]['score']
        pelicula = df_filtrado3.iloc[1]['title']
        return pelicula, puntaje
    elif parametro == 'disney':
        data_filtrado = data[(data['id'].str.contains('d'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        df_filtrado3 = data_filtrado2.sort_values('title',ascending=True)
        pelicula = df_filtrado3.iloc[1]['title']
        puntaje = df_filtrado3.iloc[1]['score']
        return pelicula, puntaje
    else:
        return 'No existe la plataforma que ingresaste en nuestra base de datos'
    
    
##Esta funcion devuelve la pelicula que más duro según año y plataforma

@app.get("/Pelicula que más duro segun el año y plataforma")
def get_longest(plataforma,min:int,anio:int):
    parametro = plataforma.lower()
    if parametro == 'nexflix':
        data_filtrado = data[(data['id'].str.contains('n'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        data_filtrado3 = data_filtrado2[(data_filtrado2['release_year'] == anio)]
        data_filter4 = data_filtrado3.sort_values('duration_int',ascending=False)
        titulo = data_filter4.iloc[0]['title']
        tiempo = data_filter4.iloc[0]['duration_int']
        tipo_duracion = data_filter4.iloc[0]['duration_type']
        return titulo, tiempo, tipo_duracion
    if parametro == 'hulu':
        data_filtrado = data[(data['id'].str.contains('h'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        data_filtrado3 = data_filtrado2[(data_filtrado2['release_year'] == anio)]
        data_filter4 = data_filtrado3.sort_values('duration_int',ascending=False)
        titulo = data_filter4.iloc[0]['title']
        tiempo = data_filter4.iloc[0]['duration_int']
        tipo_duracion = data_filter4.iloc[0]['duration_type']
        return titulo, tiempo, tipo_duracion
    if parametro == 'disney':
        data_filtrado = data[(data['id'].str.contains('d'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        data_filtrado3 = data_filtrado2[(data_filtrado2['release_year'] == anio)]
        data_filter4 = data_filtrado3.sort_values('duration_int',ascending=False)
        titulo = data_filter4.iloc[0]['title']
        tiempo = data_filter4.iloc[0]['duration_int']
        tipo_duracion = data_filter4.iloc[0]['duration_type']
        return titulo, tiempo, tipo_duracion
    if parametro == 'amazon':
        data_filtrado = data[(data['id'].str.contains('a'))]
        data_filtrado2 = data_filtrado[(data_filtrado['type'] == 'movie')]
        data_filtrado3 = data_filtrado2[(data_filtrado2['release_year'] == anio)]
        data_filter4 = data_filtrado3.sort_values('duration_int',ascending=False)
        titulo = data_filter4.iloc[0]['title']
        tiempo = data_filter4.iloc[0]['duration_int']
        tipo_duracion = data_filter4.iloc[0]['duration_type']
        return titulo, tiempo, tipo_duracion
    else:
        return 'No existe la plataforma que ingresaste en nuestra base de datos'
    

##Esta función devuelve la cantidad de peliculas por rating que el usuario ingrese

@app.get("/Cantidad de series y peliculas por rating")
def get_rating_count(rating):
    rating1 = rating
    if rating == 'G':
        data_filtrado = data[(data['rating'] == 'G')]
        return rating1, len(data_filtrado)
    elif rating == '18+':
        data_filtrado = data[(data['rating'] == '18+')]
        return rating1, len(data_filtrado)
    elif rating == '13+':
        data_filtrado = data[(data['rating'] == '13+')]
        return rating1, len(data_filtrado)
    elif rating == 'ALL':
        data_filtrado = data[(data['rating'] == 'ALL')]
        return rating1, len(data_filtrado)
    elif rating == 'R':
        data_filtrado = data[(data['rating'] == 'R')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-Y':
        data_filtrado = data[(data['rating'] == 'TV_Y')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-Y7':
        data_filtrado = data[(data['rating'] == 'TV-Y7')]
        return rating1, len(data_filtrado)
    elif rating == 'NR':
        data_filtrado = data[(data['rating'] == 'NR')]
        return rating1, len(data_filtrado)
    elif rating == '16+':
        data_filtrado = data[(data['rating'] == '16+')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-PG':
        data_filtrado = data[(data['rating'] == 'TV-PG')]
        return rating1, len(data_filtrado)
    elif rating == '7+':
        data_filtrado = data[(data['rating'] == '7+')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-14':
        data_filtrado = data[(data['rating'] == 'TV-14')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-NR':
        data_filtrado = data[(data['rating'] == 'TV-NR')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-G':
        data_filtrado = data[(data['rating'] == 'TV-G')]
        return rating1, len(data_filtrado)
    elif rating == 'PG-13':
        data_filtrado = data[(data['rating'] == 'PG-13')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-MA':
        data_filtrado = data[(data['rating'] == 'TV-MA')]
        return rating1, len(data_filtrado)
    elif rating == 'PG':
        data_filtrado = data[(data['rating'] == 'PG')]
        return rating1, len(data_filtrado)
    elif rating == 'NC-17':
        data_filtrado = data[(data['rating'] == 'NC-17')]
        return rating1, len(data_filtrado)
    elif rating == 'UNRATED':
        data_filtrado = data[(data['rating'] == 'UNRATED')]
        return rating1, len(data_filtrado)
    elif rating == '16':
        data_filtrado = data[(data['rating'] == '16')]
        return rating1, len(data_filtrado)
    elif rating == 'AGES_16':
        data_filtrado = data[(data['rating'] == 'AGES_16')]
        return rating1, len(data_filtrado)
    elif rating == 'AGES_18':
        data_filtrado = data[(data['rating'] == 'AGES_18')]
        return rating1, len(data_filtrado)
    elif rating == 'ALL_AGES':
        data_filtrado = data[(data['rating'] == 'ALL_AGES')]
        return rating1, len(data_filtrado)
    elif rating == 'NOT_RATE':
        data_filtrado = data[(data['rating'] == 'NOT_RATE')]
        return rating1, len(data_filtrado)
    elif rating == 'TV-Y7-FV':
        data_filtrado = data[(data['rating'] == 'TV-Y7-FV')]
        return rating1, len(data_filtrado)
    elif rating == 'NOT RATED':
        data_filtrado = data[(data['rating'] == 'NOT RATED')]
        return rating1, len(data_filtrado)
    elif rating == '2 Seasons':
        data_filtrado = data[(data['rating'] == '2 Seasons')]
        return rating1, len(data_filtrado)
    elif rating == '93 min':
        data_filtrado = data[(data['rating'] == '93 min')]
        return rating1, len(data_filtrado)
    elif rating == '4 Seasons':
        data_filtrado = data[(data['rating'] == '4 Seasons')]
        return rating1, len(data_filtrado)
    elif rating == '136 min':
        data_filtrado = data[(data['rating'] == '136 min')]
        return rating1, len(data_filtrado)
    elif rating == '91 min':
        data_filtrado = data[(data['rating'] == '91 min')]
        return rating1, len(data_filtrado)
    elif rating == '85 min':
        data_filtrado = data[(data['rating'] == '85 min')]
        return rating1, len(data_filtrado)
    elif rating == '98 min':
        data_filtrado = data[(data['rating'] == '98 min')]
        return rating1, len(data_filtrado)
    elif rating == '89 min':
        data_filtrado = data[(data['rating'] == '89 min')]
        return rating1, len(data_filtrado)
    elif rating == '94 min':
        data_filtrado = data[(data['rating'] == '94 min')]
        return rating1, len(data_filtrado)
    elif rating == '86':
        data_filtrado = data[(data['rating'] == '86')]
        return rating1, len(data_filtrado)
    elif rating == '3 Seasons':
        data_filtrado = data[(data['rating'] == '3 Seasons')]
        return rating1, len(data_filtrado)
    elif rating == '121 min':
        data_filtrado = data[(data['rating'] == '121 min')]
        return rating1, len(data_filtrado)
    elif rating == '88 min':
        data_filtrado = data[(data['rating'] == '88 min')]
        return rating1, len(data_filtrado)
    elif rating == '101 min':
        data_filtrado = data[(data['rating'] == '101 min')]
        return rating1, len(data_filtrado)
    elif rating == '1 Season':
        data_filtrado = data[(data['rating'] == '1 Season')]
        return rating1, len(data_filtrado)
    elif rating == '83 min':
        data_filtrado = data[(data['rating'] == '83 min')]
        return rating1, len(data_filtrado)
    elif rating == '100 min':
        data_filtrado = data[(data['rating'] == '100 min')]
        return rating1, len(data_filtrado)
    elif rating == '95 min':
        data_filtrado = data[(data['rating'] == '95 min')]
        return rating1, len(data_filtrado)
    elif rating == '92 min':
        data_filtrado = data[(data['rating'] == '92 min')]
        return rating1, len(data_filtrado)
    elif rating == '96 min':
        data_filtrado = data[(data['rating'] == '96 min')]
        return rating1, len(data_filtrado)
    elif rating == '109 min':
        data_filtrado = data[(data['rating'] == '109 min')]
        return rating1, len(data_filtrado)
    elif rating == '99 min':
        data_filtrado = data[(data['rating'] == '99 min')]
        return rating1, len(data_filtrado)
    elif rating == '75 min':
        data_filtrado = data[(data['rating'] == '75 min')]
        return rating1, len(data_filtrado)
    elif rating == '87 min':
        data_filtrado = data[(data['rating'] == '87 min')]
        return rating1, len(data_filtrado)
    elif rating == '67 min':
        data_filtrado = data[(data['rating'] == '67 min')]
        return rating1, len(data_filtrado)
    elif rating == '104 min':
        data_filtrado = data[(data['rating'] == '104 min')]
        return rating1, len(data_filtrado)
    elif rating == '107 min':
        data_filtrado = data[(data['rating'] == '107 min')]
        return rating1, len(data_filtrado)
    elif rating == '84 min':
        data_filtrado = data[(data['rating'] == '84 min')]
        return rating1, len(data_filtrado)
    elif rating == '103 min':
        data_filtrado = data[(data['rating'] == '103 min')]
        return rating1, len(data_filtrado)
    elif rating == '105 min':
        data_filtrado = data[(data['rating'] == '105 min')]
        return rating1, len(data_filtrado)
    elif rating == '119 min':
        data_filtrado = data[(data['rating'] == '119 min')]
        return rating1, len(data_filtrado)
    elif rating == '114 min':
        data_filtrado = data[(data['rating'] == '114 min')]
        return rating1, len(data_filtrado)
    elif rating == '82 min':
        data_filtrado = data[(data['rating'] == '82 min')]
        return rating1, len(data_filtrado)
    elif rating == '90 min':
        data_filtrado = data[(data['rating'] == '90 min')]
        return rating1, len(data_filtrado)
    elif rating == '130 min':
        data_filtrado = data[(data['rating'] == '130 min')]
        return rating1, len(data_filtrado)
    elif rating == '110 min':
        data_filtrado = data[(data['rating'] == '110 min')]
        return rating1, len(data_filtrado)
    elif rating == '80 min':
        data_filtrado = data[(data['rating'] == '80 min')]
        return rating1, len(data_filtrado)
    elif rating == '6 Seasons':
        data_filtrado = data[(data['rating'] == '6 Seasons')]
        return rating1, len(data_filtrado)
    elif rating == '97 min':
        data_filtrado = data[(data['rating'] == '97 min')]
        return rating1, len(data_filtrado)
    elif rating == '111 min':
        data_filtrado = data[(data['rating'] == '111 min')]
        return rating1, len(data_filtrado)
    elif rating == '81 min':
        data_filtrado = data[(data['rating'] == '81 min')]
        return rating1, len(data_filtrado)
    elif rating == '49 min':
        data_filtrado = data[(data['rating'] == '49 min')]
        return rating1, len(data_filtrado)
    elif rating == '45 min':
        data_filtrado = data[(data['rating'] == '45 min')]
        return rating1, len(data_filtrado)
    elif rating == '41 min':
        data_filtrado = data[(data['rating'] == '41 min')]
        return rating1, len(data_filtrado)
    elif rating == '73 min':
        data_filtrado = data[(data['rating'] == '73 min')]
        return rating1, len(data_filtrado)
    elif rating == '40 min':
        data_filtrado = data[(data['rating'] == '40 min')]
        return rating1, len(data_filtrado)
    elif rating == '36 min':
        data_filtrado = data[(data['rating'] == '36 min')]
        return rating1, len(data_filtrado)
    elif rating == '39 min':
        data_filtrado = data[(data['rating'] == '39 min')]
        return rating1, len(data_filtrado)
    elif rating == '34 min':
        data_filtrado = data[(data['rating'] == '34 min')]
        return rating1, len(data_filtrado)
    elif rating == '47 min':
        data_filtrado = data[(data['rating'] == '47 min')]
        return rating1, len(data_filtrado)
    elif rating == '65 min':
        data_filtrado = data[(data['rating'] == '65 min')]
        return rating1, len(data_filtrado)
    elif rating == '37 min':
        data_filtrado = data[(data['rating'] == '37 min')]
        return rating1, len(data_filtrado)
    elif rating == '78 min':
        data_filtrado = data[(data['rating'] == '78 min')]
        return rating1, len(data_filtrado)
    elif rating == '102 min':
        data_filtrado = data[(data['rating'] == '102 min')]
        return rating1, len(data_filtrado)
    elif rating == '129 min':
        data_filtrado = data[(data['rating'] == '129 min')]
        return rating1, len(data_filtrado)
    elif rating == '115 min':
        data_filtrado = data[(data['rating'] == '115 min')]
        return rating1, len(data_filtrado)
    elif rating == '112 min':
        data_filtrado = data[(data['rating'] == '112 min')]
        return rating1, len(data_filtrado)
    elif rating == '61 min':
        data_filtrado = data[(data['rating'] == '61 min')]
        return rating1, len(data_filtrado)
    elif rating == '106 min':
        data_filtrado = data[(data['rating'] == '106 min')]
        return rating1, len(data_filtrado)
    elif rating == '76 min':
        data_filtrado = data[(data['rating'] == '76 min')]
        return rating1, len(data_filtrado)
    elif rating == '77 min':
        data_filtrado = data[(data['rating'] == '77 min')]
        return rating1, len(data_filtrado)
    elif rating == '79 min':
        data_filtrado = data[(data['rating'] == '79 min')]
        return rating1, len(data_filtrado)
    elif rating == '157 min':
        data_filtrado = data[(data['rating'] == '157 min')]
        return rating1, len(data_filtrado)
    elif rating == '28 min':
        data_filtrado = data[(data['rating'] == '28 min')]
        return rating1, len(data_filtrado)
    elif rating == '64 min':
        data_filtrado = data[(data['rating'] == '64 min')]
        return rating1, len(data_filtrado)
    elif rating == '7 min':
        data_filtrado = data[(data['rating'] == '7 min')]
        return rating1, len(data_filtrado)
    elif rating == '5 min':
        data_filtrado = data[(data['rating'] == '5 min')]
        return rating1, len(data_filtrado)
    elif rating == '6 min':
        data_filtrado = data[(data['rating'] == '6 min')]
        return rating1, len(data_filtrado)
    elif rating == '127 min':
        data_filtrado = data[(data['rating'] == '127 min')]
        return rating1, len(data_filtrado)
    elif rating == '142 min':
        data_filtrado = data[(data['rating'] == '142 min')]
        return rating1, len(data_filtrado)
    elif rating == '108 min':
        data_filtrado = data[(data['rating'] == '108 min')]
        return rating1, len(data_filtrado)
    elif rating == '57 min':
        data_filtrado = data[(data['rating'] == '57 min')]
        return rating1, len(data_filtrado)
    elif rating == '118 min':
        data_filtrado = data[(data['rating'] == '118 min')]
        return rating1, len(data_filtrado)
    elif rating == '116 min':
        data_filtrado = data[(data['rating'] == '116 min')]
        return rating1, len(data_filtrado)
    elif rating == '12 Seasons':
        data_filtrado = data[(data['rating'] == '12 Seasons')]
        return rating1, len(data_filtrado)
    elif rating == '71 min':
        data_filtrado = data[(data['rating'] == '71 min')]
        return rating1, len(data_filtrado)
    elif rating == '74 min':
        data_filtrado = data[(data['rating'] == '74 min')]
        return rating1, len(data_filtrado)
    elif rating == '66 min':
        data_filtrado = data[(data['rating'] == '66 min')]
        return rating1, len(data_filtrado)
    elif rating == 'UR':
        data_filtrado = data[(data['rating'] == 'UR')]
        return rating1, len(data_filtrado)
    else:
        return 'El rating que buscas no se encuentra en nuestra base de datos'
