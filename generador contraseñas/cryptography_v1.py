from cryptography.fernet import Fernet

texto = "Hola mundo"
cifrado = Fernet(Fernet.generate_key())
texto_encriptado = cifrado.encrypt(texto.encode('utf-8'))
print(texto_encriptado)

texto_desencriptado = cifrado.decrypt(texto_encriptado).decode('utf-8')
print(texto_desencriptado)