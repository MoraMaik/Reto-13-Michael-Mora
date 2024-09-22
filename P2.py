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
