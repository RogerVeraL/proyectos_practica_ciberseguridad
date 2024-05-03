from bcrypt import hashpw, gensalt, checkpw

def encriptar(texto):
    texto = texto.encode('utf-8')
    sal = gensalt()
    return hashpw(texto, sal), sal.decode('utf-8')

def descencriptar(textoEncriptado, sal):
    textoEncriptado = textoEncriptado.encode('utf-8')
    sal = sal.encode('utf-8')
    return checkpw(textoEncriptado, sal)

if __name__ == '__main__':
    if input("Desea encriptar o desencriptar? (e/d): ").lower() == 'e':
        texto = input("Introduce la contraseña a encriptar: ")
        texto_encriptado, sal = encriptar(texto)
        print("Texto encriptado:", texto_encriptado)
        print("Sal:", sal)    
    else:
        texto_encriptado = input("Introduce el texto encriptado: ")
        sal = input("Introduce la sal: ")
        if descencriptar(texto_encriptado, sal):
            print("La contraseña es correcta.")
        else:
            print("La contraseña es incorrecta.")
