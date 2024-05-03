import hashlib

def descrifrar_hash(hash_input, archivo):
    crackeada = False

    with open(archivo, "r") as f:
        diccionario = [x.strip() for x in f.readlines()]

        for contraseña in diccionario:
            if hashlib.sha256(contraseña.encode()).hexdigest() == hash_input:
                crackeada = True
                print(f"La contraseña es: {contraseña}")
                break
        
        if not crackeada:
            print("La contraseña no se encuentra en el diccionario")

if __name__ == "__main__":
    descrifrar_hash(input("Introduce el hash a descifrar (sha256): "), input("Introduce el nombre del archivo del diccionario: "))