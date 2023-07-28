import requests as requests
import json

def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        print(f"Nombre Oficial en Español:{pais['translations']['spa']['official']}")
        print(f"Poblacion:{pais['population']}")
        print(f"Area:{pais['area']}")

        poblacion_max = max(paises, key=lambda pais:pais['population'])
        print("PAIS CON MAYOR POBLACION :",poblacion_max['translations']['spa']['official'],"con una polacion",poblacion_max['population'])

        area_max = max(paises, key=lambda pais:pais['area'])
        print("PAIS CON MAYOR AREA", area_max['translations']['spa']['official'], " area:", area_max['area'])


        total = sum(pais['population'] for pais in paises)
        print("POBLACION TOTAL:",total)

        media = total/ len(paises)
        print("MEDIA DE LA POBLACION:",media)

        mediana = paises[len(paises) //2] ['population']
        print("MEDIANA DE LA POBLACION:",mediana)

        moda = max(pais['population'] for pais in paises)
        print("MODA DE LA POBLACION",moda)




url = 'https://restcountries.com/v3.1/all'
listar_nombre_paises(url)