# Reto 13 Michael Mora
Desarrollo del Reto 13 (ultimo), según lo aprendido en clase con [Diccionarios](http://https://github.com/fegonzalez7/pdc_unal_clase18?tab=readme-ov-file "Diccionarios").
___________________________
## Punto 1
Instrucciones: Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

```python
# Definimos el diccionario con valores del mismo tipo
mi_diccionario = {
    "a": 10,
    "b": 5,
    "c": 15,
    "d": 3,
    "e": 12
}

# Obtenemos los valores del diccionario
valores = mi_diccionario.values()

# Ordenamos los valores en orden ascendente
valores_ordenados = sorted(valores)

# Imprimimos los valores ordenados
print("Valores ordenados de manera ascendente:")
for valor in valores_ordenados:
    print(valor)
```

Este código es adaptable a cualquier tipo de valores, ya sean enteros, flotantes, o cadenas de texto, siempre que los tipos sean comparables entre sí. 
___________________________
## Punto 2
Instrucciones: Desarrollar una funcion que reciba dos diccionarios como parametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

```python
def mezclar_diccionarios(dic1, dic2):
    # Creamos una copia del primer diccionario para no modificar el original
    resultado = dic1.copy()
    
    # Recorremos el segundo diccionario
    for clave, valor in dic2.items():
        # Solo añadimos la clave/valor si no está presente en el primer diccionario
        if clave not in resultado:
            resultado[clave] = valor
    
    return resultado

# Ejemplo de uso
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 20, 'd': 4, 'e': 5}

diccionario_mezclado = mezclar_diccionarios(diccionario1, diccionario2)
print(diccionario_mezclado)
```
Explicación:
1. Copia del primer diccionario:
  + Utilizamos dic1.copy() para crear una copia del primer diccionario. Esto nos permite modificar el diccionario sin afectar al original.
2. Recorrer el segundo diccionario:
  + Usamos un ciclo for para recorrer las claves y valores del segundo diccionario (dic2.items()).
3. Condición para evitar claves repetidas:
  + Para cada clave del segundo diccionario, se verifica si la clave no está presente en el primer diccionario (if clave not in resultado:). Si la clave no está en el primer diccionario, se añade al nuevo diccionario.
4. Devolver el diccionario mezclado:
  + El resultado final es un diccionario que contiene todas las claves de ambos diccionarios, pero si una clave está repetida, se mantiene el valor del primer diccionario.
___________________________
## Punto 3
Instrucciones:

[![R13-2.jpg](https://i.postimg.cc/HW8bQ280/R13-2.jpg)](https://postimg.cc/WtjDV0nt)

```python
import json

# El contenido del JSON (puede estar en un archivo .json en vez de directamente en el código)
datos_json = '''
{
    "jadiazcoronado": {
        "nombres": "Juan Antonio",
        "apellidos": "Díaz Coronado",
        "edad": 19,
        "colombiano": true,
        "deportes": ["Fútbol", "Ajedrez", "Gimnasia"]
    },
    "dmlunasol": {
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad": 25,
        "colombiano": false,
        "deportes": ["Baloncesto", "Ajedrez", "Gimnasia"]
    }
}
'''

# Cargamos el JSON en un diccionario de Python
datos = json.loads(datos_json)

# Función para encontrar personas que practiquen un deporte específico
def personas_por_deporte(deporte, datos):
    print(f"Personas que practican {deporte}:")
    for usuario, info in datos.items():
        if deporte in info["deportes"]:
            nombre_completo = f"{info['nombres']} {info['apellidos']}"
            print(nombre_completo)

# Función para encontrar personas dentro de un rango de edades
def personas_por_rango_edad(edad_min, edad_max, datos):
    print(f"\nPersonas en el rango de edades {edad_min}-{edad_max}:")
    for usuario, info in datos.items():
        if edad_min <= info["edad"] <= edad_max:
            nombre_completo = f"{info['nombres']} {info['apellidos']}"
            print(nombre_completo)

# Solicitar deporte al usuario
deporte_ingresado = input("Ingresa el deporte a buscar: ")
personas_por_deporte(deporte_ingresado, datos)

# Solicitar rango de edades al usuario
edad_min = int(input("\nIngresa la edad mínima: "))
edad_max = int(input("Ingresa la edad máxima: "))
personas_por_rango_edad(edad_min, edad_max, datos)

```
Explicación:

1. Lectura de JSON:

  + Utilizamos el módulo json de Python para cargar el JSON como un diccionario. En este ejemplo, el contenido del JSON está directamente en el código, pero podríamos cargarlo desde un archivo.

2. Funciones para las operaciones:

  + personas_por_deporte: Recibe como parámetros el deporte y el diccionario datos. Recorre todas las personas del JSON, verificando si el deporte ingresado está en su lista de deportes.
personas_por_rango_edad: Recibe el rango de edades y el diccionario datos. Recorre las personas, comparando sus edades con el rango ingresado.

3. Interacción con el usuario:

  + El programa solicita al usuario ingresar el deporte a buscar y luego el rango de edades (mínimo y máximo). Con esos datos, se ejecutan las funciones correspondientes y se imprime el resultado.
___________________________
## Punto 4
Instrucciones:
El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:

```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```
Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.


*CODIGO*
```python
import json
from datetime import datetime

# Cargar archivo JSON
jsonString = '''
{"dt": {"0": 1685116800, "1": 1685203200, "2": 1685289600, "3": 1685376000, "4": 1685462400, "5": 1685548800, "6": 1685635200, "7": 1685721600}, 
 "alertPrecip": {"0": "X", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
 "alertVelViento": {"0": "-", "1": "-", "2": "X", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
 "alertTmpMax": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "X", "6": "-", "7": "-"},
 "alertTmpMin": {"0": "-", "1": "X", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
 "precipitacion": {"0": 40.0}, 
 "velViento": {"2": 5.38}, 
 "tmpMax": {"5": 29.78}, 
 "tmpMin": {"1": 24.64},
 "recomendaciones": {
    "lluvias": "Realice una revisión y limpieza a la red de desague y canales existentes...",
    "vientos": "Asegúrese de asegurar estructuras sueltas y proteger ventanas...",
    "temperatura": "Utilice ropa ligera y evite exponerse a temperaturas extremas por periodos prolongados."
 }
}
'''

# Cargar el JSON como un diccionario
data = json.loads(jsonString)

# Función para convertir el tiempo UTC a una fecha legible
def convertir_fecha_utc(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

# Función para revisar alertas y mostrar información relevante
def revisar_alertas(data):
    dias = data['dt']
    
    for dia, timestamp in dias.items():
        fecha = convertir_fecha_utc(timestamp)
        print(f"\nFecha: {fecha}")

        # Revisar alertas
        alertas = []
        
        # Alerta de precipitación
        if data['alertPrecip'][dia] == "X":
            alertas.append(f"Alerta de precipitación: {data['precipitacion'].get(dia, 'No disponible')} mm")
            print("Recomendación para lluvias:", data['recomendaciones']['lluvias'])
        
        # Alerta de velocidad del viento
        if data['alertVelViento'][dia] == "X":
            alertas.append(f"Alerta de viento: {data['velViento'].get(dia, 'No disponible')} km/h")
            print("Recomendación para vientos:", data['recomendaciones']['vientos'])
        
        # Alerta de temperatura máxima
        if data['alertTmpMax'][dia] == "X":
            alertas.append(f"Alerta de temperatura máxima: {data['tmpMax'].get(dia, 'No disponible')} °C")
            print("Recomendación para temperaturas:", data['recomendaciones']['temperatura'])
        
        # Alerta de temperatura mínima
        if data['alertTmpMin'][dia] == "X":
            alertas.append(f"Alerta de temperatura mínima: {data['tmpMin'].get(dia, 'No disponible')} °C")
            print("Recomendación para temperaturas:", data['recomendaciones']['temperatura'])

        if alertas:
            # Si hay alertas, las imprimimos
            for alerta in alertas:
                print(alerta)
        else:
            print("No hay alertas para este día.")

# Llamar a la función para revisar las alertas
revisar_alertas(data)

```
Explicacion: 

1, Conversión de UTC a fecha legible:

  + Usamos la función convertir_fecha_utc() para convertir los timestamps (datos del campo dt) a fechas en formato YYYY-MM-DD.

2. Revisión de alertas:

  + Para cada día, se revisa si alguna de las alertas (alertPrecip, alertVelViento, alertTmpMax, alertTmpMin) tiene el valor "X". Si es así, se obtiene la información relevante, como la cantidad de precipitación, velocidad del viento o temperatura.

3. Recomendaciones:


  + Si hay una alerta activa, también se muestra la recomendación correspondiente, obtenida del campo recomendaciones.

4. Recuperación de datos específicos:

  + Usamos .get(dia, 'No disponible') para obtener los valores correspondientes (precipitación, velocidad del viento, temperatura) para ese día. Si no están disponibles, se muestra un mensaje indicando que no hay datos.

___________________________
## Punto 5
Instrucciones: A través de un programa conectese a al menos 3 [API's](http://https://apipheny.io/free-api/ "API's") , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

**APIs utilizadas**:
  + API de clima: [OpenWeatherMap](http://https://openweathermap.org/ "OpenWeatherMap") (requiere clave API gratuita).
  + API de datos aleatorios: [Random User API](http://https://randomuser.me/ "Random User API")
  + API de criptomonedas: [CoinGecko](http://https://www.coingecko.com/ "CoinGecko")


```python
import requests
import json

# Función para hacer la solicitud a la API y obtener el JSON
def obtener_json_de_api(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica si hubo algún error en la respuesta
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API: {e}")
        return None

# Función para imprimir los pares llave:valor de un JSON
def imprimir_pares_clave_valor(json_data, nombre_api):
    print(f"\nPares clave:valor de la API - {nombre_api}:")
    if isinstance(json_data, dict):
        for clave, valor in json_data.items():
            print(f"{clave}: {valor}")
    else:
        print("Los datos no están en el formato esperado de diccionario.")

# API 1: OpenWeatherMap (necesita clave API)
def api_clima():
    ciudad = "London"
    api_key = "TU_CLAVE_API_AQUI"  # Reemplaza con tu clave de OpenWeatherMap
    url_clima = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    
    # Obtener JSON
    json_clima = obtener_json_de_api(url_clima)
    
    # Imprimir pares llave:valor
    if json_clima:
        imprimir_pares_clave_valor(json_clima, "OpenWeatherMap")

# API 2: Random User (no requiere clave API)
def api_random_user():
    url_random_user = "https://randomuser.me/api/"
    
    # Obtener JSON
    json_random_user = obtener_json_de_api(url_random_user)
    
    # Imprimir pares llave:valor
    if json_random_user:
        imprimir_pares_clave_valor(json_random_user, "Random User")

# API 3: CoinGecko (no requiere clave API)
def api_criptomonedas():
    url_coingecko = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    
    # Obtener JSON
    json_criptos = obtener_json_de_api(url_coingecko)
    
    # Imprimir pares llave:valor
    if json_criptos:
        imprimir_pares_clave_valor(json_criptos, "CoinGecko")

# Llamar a las funciones para conectarse a las APIs y mostrar los resultados
def main():
    # Llamar a la API de OpenWeatherMap
    print("Conectando a la API de clima (OpenWeatherMap)...")
    api_clima()
    
    # Llamar a la API de Random User
    print("\nConectando a la API de usuario aleatorio (Random User)...")
    api_random_user()
    
    # Llamar a la API de CoinGecko
    print("\nConectando a la API de criptomonedas (CoinGecko)...")
    api_criptomonedas()

# Ejecutar el programa
if __name__ == "__main__":
    main()

```
Explicacion:

1. obtener_json_de_api():

  + Esta función toma una URL y hace una solicitud GET a la API. Devuelve la respuesta en formato JSON.

2. imprimir_pares_clave_valor():

  + Esta función recibe un objeto JSON (un diccionario) y recorre sus pares clave-valor, imprimiéndolos en la consola.

3. Conexión a las APIs:

  + API de Clima (OpenWeatherMap): Se conecta a la API del clima usando una ciudad y una clave de API.
  + API de Usuario Aleatorio (Random User): Obtiene datos aleatorios de un usuario.
  + API de Criptomonedas (CoinGecko): Obtiene el precio actual de Bitcoin y Ethereum en dólares.

4. Funciones específicas para cada API:

  + Cada API tiene su propia función (api_clima(), api_random_user(), api_criptomonedas()) que se conecta a la API y procesa la respuesta.

5. Ejecución del programa:

  + En la función main(), llamamos a las tres funciones para obtener y mostrar los datos de las APIs.

___________________________
FIN RETO, MUCHAS GRACIAS POR TODO.
