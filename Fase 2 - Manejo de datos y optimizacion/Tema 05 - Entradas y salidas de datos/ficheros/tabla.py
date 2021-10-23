import sys
print(sys.argv) # argumentos enviados
if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    if (num1 and num2) >= 0 and (num1 and num2) <= 9:
        for i in range(num1):
            for y in range(num2):
                print(" * ", end='')
            print("")
    else: print("Los números tienen que ser enteros entre 0 y 9.")
else: print("Error, el programa necesita 3 argumentos. Y estos tienen que ser números enteros entre 0 y 9.")