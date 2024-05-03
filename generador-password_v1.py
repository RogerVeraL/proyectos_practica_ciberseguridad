import string, secrets

def generar_password(longitud,min_numeros,min_letras_especiales):
    repertorio = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(repertorio) for i in range(longitud))
        if (
            sum(l.isdigit() for l in password) >= min_numeros and 
            sum(l in string.punctuation for l in password) >= min_letras_especiales):
                break

    return password


if __name__ == '__main__':
    longitud = int(input("Introduce la longitud de la contraseña: "))
    min_numeros = int(input("Introduce el número mínimo de números: "))
    min_letras_especiales = int(input("Introduce el número mínimo de letras especiales: "))
    print(generar_password(longitud,min_numeros,min_letras_especiales))
