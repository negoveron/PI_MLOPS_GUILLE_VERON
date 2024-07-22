import pandas as pd
from fastapi import FastAPI

app = FastAPI()



# Endpoints de la API
# @profile
@app.get('/cantidad_filmaciones_mes/{mes}')
async def cantidad_filmaciones_mes(mes: str):           
    return {f"21 películas fueron estrenadas en el mes de {mes}"}

@app.get('/cantidad_filmaciones_dia/{dia}')
async def cantidad_filmaciones_dia(dia: str):   
    return {f"21 películas fueron estrenadas en los días {dia}"}
    

@app.get('/score_titulo/{titulo_de_la_filmacion}')
async def score_titulo(titulo_de_la_filmacion: str):   
    return {f"La película {titulo_de_la_filmacion} fue estrenada en el año 2018 con un score/popularidad de 7.8"}


@app.get('/votos_titulo/{titulo_de_la_filmacion}')
async def votos_titulo(titulo_de_la_filmacion: str):
    return {f"La película {titulo_de_la_filmacion} fue estrenada en el año 2018 .La misma cuenta con un total de 2500 valoraciones,"\
            " con un promedio de 6.3"}


@app.get('/get_actor/{nombre_actor}')
async def get_actor(nombre_actor: str):
    return {f"El actor {nombre_actor} ha participado de 12 filmaciones, el mismo ha conseguido un retorno de 1200 "\
            "con un promedio de 350 por filmación"}

@app.get('/get_director/{nombre_director}')
async def get_director(nombre_director: str):
    return  {"director" : nombre_director, "retorno": 45857 , "peliculas":[
                {"nombre":"Pelicula 1","lanzamiento":"12/06/2018","retorno":2547,"costo":1254, "ganancia":854},
                {"nombre":"Pelicula 2","lanzamiento":"11/07/2018","retorno":2547,"costo":1254, "ganancia":854},
                {"nombre":"Pelicula 3","lanzamiento":"13/08/2018","retorno":2547,"costo":1254, "ganancia":854}
            ]}

@app.get('/recomendacion/{titulo}')
async def recomendacion(titulo: str):
    return ["Pelicula 1","Pelicula 2","Pelicula 3","Pelicula 4","Pelicula 5"]
    
