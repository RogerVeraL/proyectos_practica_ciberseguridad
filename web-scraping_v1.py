import requests
from bs4 import BeautifulSoup


def busqueda(palabra,url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    respuesta = requests.get(url,headers=headers)

    if respuesta.status_code == 200:
        sopa = BeautifulSoup(respuesta.text, 'html.parser')
        if palabra in sopa.get_text().lower():
            print('La palabra', palabra, 'se encuentra en la página')
    else:
        print('Error en la petición:', respuesta.status_code)

if __name__ == '__main__':
    busqueda(input('Ingrese la palabra a buscar: '), input('Ingrese la url: '))
    print('Fin del programa')