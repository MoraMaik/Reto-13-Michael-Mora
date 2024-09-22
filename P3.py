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
