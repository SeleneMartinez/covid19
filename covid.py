import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
from matplotlib import dates

colores = ["r-","b-","y-","g-","c-","m-","k-"]


def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
archivo = pd.read_cvs("full_data.csv")

def obtener_paises():

    datos = archivo.to_dict("list")
    paises =[]
    contador = 0

    ingresar_pais =''
    otro_pais = True
    while((otro_pais)):
        contador+=1
        pais = (input("Ingrese pais: ")).capitalize()
        if (pais in datos['location'] ):
            paises.append(pais)
        else:
            print("Pais invalido")

        if  (contador < len(colores)):
            while ingresar_pais not in ('S','N'):
                ingresar_pais =input("Desea ingresar otro pais? S/N: ").upper()
        else:
            ingresar_pais = "N"

        if (ingresar_pais == "N"):
            otro_pais = False
        ingresar_pais = ''

    return paises







def obtener_casos(pais,color,fecha_inicial, fecha_final):
    data = archivo[(archivo["location"] == pais) & (archivo["date"]>fecha_inicial) & (archivo["date"] <fecha_final)].to_dict("list")

    fecha = data["date"]
    casos = np.log10(data["total_cases"])
    plt.plot(fecha,casos,color, label=pais)
    plt.legend()
def obtener_muertes(pais,color,fecha_inicial, fecha_final):
    data = archivo[(archivo["location"] == pais) & (archivo["date"]>fecha_inicial) & (archivo["date"] <fecha_final)].to_dict("list")

    fecha = data["date"]
    muertes = np.log10(data["total_deaths"])
    plt.plot(fecha,muertes,color, label=pais)
    plt.legend()

def obtener_fechas():
    fecha_inicial = input("ingrese fecha inicial formato YYYY-MM-DD: ")
    fecha_final = input("ingrese fecha final formato YYYY-MM-DD:" )

    return (fecha_inicial, fecha_final)

def graficar():
    plt.figure(figsize=(30,10))

    paises = obtener_paises()
    i = 0
    fecha_inicial = "2020-06-12"
    fecha_final = "2020-06-30"
    for pais in paises:

        color = colores[i]
        i+=1

        plt.xlabel("fecha")
        plt.xticks(rotation=60)
        plt.subplot(1,2,1)
        obtener_casos(pais,color,fecha_inicial, fecha_final)
        plt.subplot(1,2,2)
        obtener_muertes(pais,color,fecha_inicial, fecha_final)
    plt.show()

graficar()