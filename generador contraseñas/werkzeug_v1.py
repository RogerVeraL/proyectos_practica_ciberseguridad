# 2 werkzeug
from werkzeug.security import generate_password_hash, check_password_hash

def encriptar(texto):
    return generate_password_hash(texto, method='pbkdf2:sha256', salt_length=30)

def descencriptar(textoEncriptado, hash):
    return check_password_hash(hash, textoEncriptado)

if __name__ == '__main__':
    if input("Desea encriptar o desencriptar? (e/d): ").lower() == 'e':
        print(encriptar(input("Introduce la contraseña a encriptar: ")))    
    else:
        print(descencriptar(input("Introduce la contraseña a desencriptar: "), input("Introduce el hash: ")))
