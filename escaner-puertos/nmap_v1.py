import nmap

def banner():
    print("\n||Escaner de puertos de una dirección IP||\n")

def estado(ip_host:str,scanner:nmap.nmap.PortScanner):
    print(f"\nIP : {ip_host}")
    print(f"ESTADO : {scanner[ip_host].state()}")

def resultado_puertos(ip_host:str,scanner:nmap.nmap.PortScanner):
    puertos, aux = "-p", True
    for proto in scanner[ip_host].all_protocols():
        lport = scanner[ip_host][proto].keys()
        sorted(lport)
        print('--' * 20)
        print(f"Protocolo : {proto}")
        for port in lport:
            print(f"-\nPuerto : {port}")
            print(f'Nombre : {scanner[ip_host][proto][port]["name"]}')
            print(f"Estado : {scanner[ip_host][proto][port]['state']}")
            print(f"Version : {scanner[ip_host][proto][port]['version']}")
            if scanner[ip_host][proto][port]:print(f"Producto : {scanner[ip_host][proto][port]['product']}") 
            puertos += " " + str(port) if aux else "," + str(port)
            aux = False 
        print('--' * 20)
    return puertos

def analisis(ip_host:str):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=ip_host,ports='1-1024', arguments='-sT -sV -A -O T4')

    estado(ip_host,scanner)
    puertos = resultado_puertos(ip_host,scanner)

    return f'Puertos abiertos: {puertos} {ip_host}'


if __name__ == '__main__':
    banner()
    puertos = analisis(input("Ingrese la dirección IP: "))
    print(puertos)