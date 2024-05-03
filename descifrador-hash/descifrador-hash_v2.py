import hashlib

def tipos_hash():
    algoritmos = [
        'blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256',
        'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
        'sha512', 'shake_128', 'shake_256'
    ]
    print("Algoritmos de Hash disponibles:")
    for indice, nombre in enumerate(algoritmos):
        print(f"{indice}. {nombre}")
    return algoritmos

def verificar_tipo_hash(algoritmos):
    indice = int(input("Ingrese el número del algoritmo seleccionado: "))
    if indice < 0 or indice >= len(algoritmos):
        print("Selección inválida.")
        return None
    else:
        return algoritmos[indice]
def generar_hash():
    texto = input("Introduce el texto a cifrar: ")
    algoritmos = tipos_hash()
    algoritmo_seleccionado = verificar_tipo_hash(algoritmos)
    if not algoritmo_seleccionado:
        return
    
    if 'shake' in algoritmo_seleccionado:
        longitud = int(input("Introduce la longitud del hash para SHAKE: "))
        funcion_hash = hashlib.new(algoritmo_seleccionado)
        funcion_hash.update(texto.encode())
        hash_cifrado = funcion_hash.hexdigest(longitud)
    else:
        funcion_hash = hashlib.new(algoritmo_seleccionado)
        funcion_hash.update(texto.encode())
        hash_cifrado = funcion_hash.hexdigest()

    print(f"Hash generado usando {algoritmo_seleccionado}: {hash_cifrado}")

def crackear_hash():
    dic = input("Introduce el nombre del archivo del diccionario: ")
    hash_value = input("Introduce el hash a descifrar: ")
    algoritmos = tipos_hash()
    algoritmo_seleccionado = verificar_tipo_hash(algoritmos)
    if not algoritmo_seleccionado:
        return  # Terminar la ejecución si la selección del hash es inválida

    try:
        funcion_hash = hashlib.new(algoritmo_seleccionado)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    try:
        with open(dic, "r") as f:
            diccionario = f.readlines()
    except IOError:
        print("Error al abrir el archivo del diccionario.")
        return

    crackeada = False
    longitud = None
    if 'shake' in algoritmo_seleccionado:
        longitud = int(input("Introduce la longitud del hash para SHAKE: "))

    for contraseña in diccionario:
        contraseña = contraseña.strip()
        funcion_hash.update(contraseña.encode())
        if 'shake' in algoritmo_seleccionado:
            if funcion_hash.hexdigest(longitud) == hash_value:
                crackeada = True
                break
        else:
            if funcion_hash.hexdigest() == hash_value:
                crackeada = True
                break
        funcion_hash = hashlib.new(algoritmo_seleccionado)  # Reset hash object for next iteration

    if crackeada:
        print(f"La contraseña es: {contraseña}")
    else:
        print("Contraseña no encontrada")

if __name__ == "__main__":
    inicio = input("¿Desea generar o crackear un hash existente? (g/c): ")
    if inicio == "g":
        generar_hash()
    elif inicio == "c":
        crackear_hash()
    else:
        print("Selección inválida.")
