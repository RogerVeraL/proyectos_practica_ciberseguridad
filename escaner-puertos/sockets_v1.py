import socket

def banner():
    print("\n|| Escáner de puertos de una dirección IP ||\n")
    
def analisis(ip_host:str,rango:str):
    rango = rango.split("-")
    for puerto in range(int(rango[0]),int(rango[1])+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        try:
            resultado = s.connect_ex((ip_host, puerto))
            if resultado == 0:
                print(f"El puerto {puerto} está abierto")
            # else:
            #     print(f"El puerto {puerto} está cerrado")
        except Exception as e:
            print(f"Error al escanear el puerto {puerto}: {e}")
        finally:
            s.close()

if __name__ == '__main__':
    banner()
    ip = input("Ingrese la dirección IP para escanear: ")
    rango = input("Ingrese el rango de puertos a escanear (1-1024): ")
    puertos = analisis(ip,rango)
    print("\nEscaneo finalizado")
