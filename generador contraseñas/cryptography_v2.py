# 4 cryptography
from cryptography.fernet import Fernet

def clave():
    return Fernet.generate_key()

def encriptar(texto, key):
    cifrado = Fernet(key)
    return cifrado.encrypt(texto.encode('utf-8')),key

def descencriptar(textoEncriptado, key):
    cifrado = Fernet(key)
    return cifrado.decrypt(textoEncriptado).decode('utf-8')

if __name__ == '__main__':
    if input("Desea encriptar o desencriptar? (e/d): ").lower() == 'e':
        texto = input("Introduce la contraseña a encriptar: ")
        texto_encriptado, key = encriptar(texto, clave())
        print("Texto encriptado:", texto_encriptado)
        print("Clave:", key)    
    else:
        texto_encriptado = input("Introduce el texto encriptado: ")
        key = input("Introduce la clave: ")
        texto_desencriptado = descencriptar(texto_encriptado, key)
        print("Texto desencriptado:", texto_desencriptado)