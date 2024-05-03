# 3 passlib

from passlib.context import CryptContext

def contexto():
    return CryptContext(schemes=["pbkdf2_sha256"], default="pbkdf2_sha256", pbkdf2_sha256__default_rounds=30000)

def encriptar(texto):
    return contexto().hash(texto)

def descencriptar(textoEncriptado, hash):
    return contexto().verify(textoEncriptado, hash)

if __name__ == '__main__':
    if input("Desea encriptar o desencriptar? (e/d): ").lower() == 'e':
        print(encriptar(input("Introduce la contraseña a encriptar: ")))    
    else:
        print(descencriptar(input("Introduce la contraseña a desencriptar: "), input("Introduce el hash: ")))
