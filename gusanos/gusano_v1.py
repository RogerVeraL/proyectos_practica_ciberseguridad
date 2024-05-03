import shutil
import sys

def gusano():
    if len(sys.argv) == 2:
        for i in range( 1 , int(sys.argv[1])+1 ):
            shutil.copy(sys.argv[0], sys.argv[0] + f".{i}.py")
    else:
        print("Uso: <python> gusano.py <número de copias>")

if __name__ == "__main__":
    gusano()
    