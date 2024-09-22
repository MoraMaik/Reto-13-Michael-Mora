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
