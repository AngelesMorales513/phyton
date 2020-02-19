#tablas_multiplicar.py
#Funcion que imprima las 10 tablas de multiplicar

def imprimir_tabla(numero):
    #Las tablas llegan hasta el 10
    LIMITE = 10
    # Comenzar en 1
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        # Incrementar contador para no caer en ciclo infinito
        contador = contador + 1

# Probar función
print("La tabla del 1 es: ")
imprimir_tabla(1)
print("La tabla del 2 es: ")
imprimir_tabla(2)
print("La tabla del 3 es: ")
imprimir_tabla(3)
print("La tabla del 4 es: ")
imprimir_tabla(4)
print("La tabla del 5 es: ")
imprimir_tabla(5)
print("La tabla del 6 es: ")
imprimir_tabla(6)
print("La tabla del 7 es: ")
imprimir_tabla(7)
print("La tabla del 8 es: ")
imprimir_tabla(8)
print("La tabla del 9 es: ")
imprimir_tabla(9)
print("La tabla del 10 es: ")
imprimir_tabla(10)
