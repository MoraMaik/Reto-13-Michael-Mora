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
