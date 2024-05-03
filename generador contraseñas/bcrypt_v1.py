# 1 bcrypt
from bcrypt import hashpw, gensalt, checkpw

def encriptar(texto):
    texto = texto.encode('utf-8')
    sal = gensalt() 
    return hashpw(texto, sal)

def descencriptar(textoEncriptado, hash):
    textoEncriptado = textoEncriptado.encode('utf-8')
    hash = hash.encode('utf-8')
    return checkpw(textoEncriptado, hash)

if __name__ == '__main__':
    if input("Desea encriptar o desencriptar? (e/d): ").lower() == 'e':
        print(encriptar(input("Introduce la contraseña a encriptar: ")))
    else:
        print(descencriptar(input("Introduce la contraseña a desencriptar: "), input("Introduce el hash: ")))