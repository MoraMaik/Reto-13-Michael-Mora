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
