import sys
print(sys.argv) # argumentos enviados
if len(sys.argv) == 2:
    num1 = int(sys.argv[1])
    if num1 > 0:
        n = str(num1)
        for i in range(len(n)):
            print("{:03d}".format(int(n[(len(n))-1-i])*10**i))
    else: print("El número tiene que ser entero positivo, mayor que cero.")
else: print("Error, el programa necesita 2 argumentos. El nombre del archivo + el número entero positivo.")