import sys
if len(sys.argv) == 3:
    texto = sys.argv[1] #cogemos argumento uno
    repeticiones = int(sys.argv[2]) #cogemos argumento dos
    for r in range(repeticiones):
        print(texto)
else: print("Error, introduce bien los argumentos.")
#Imprimimos el texto del arg 1 las veces que hemos pasado en arg 2.

#Es importante tener en cuenta que el programa en este caso necesita de 3 argumentos, entonces fallará si no es así.
#Podemos comprobar que tenemos esa cantidad de argumentos antes de ejecutar nada.