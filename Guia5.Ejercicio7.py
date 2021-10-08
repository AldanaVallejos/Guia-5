#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 7: Desarrollar una rutina tal que dados una base y un exponente, enteros positivos, calcule  y retorne la potencia.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
base=0
exponente=0

while base<=0 or exponente<=0: # Validaciones
    try:
        base=int(input("Ingrese el número base: "))
        if base<0:
            print("Error.Ingrese un número entero positivo")
        exponente=int(input("Ingrese el número exponente: "))
        if exponente<0:
            print("Error.Ingrese un número entero positivo")
    except ValueError:
        print("Error. Tiene que ingresar números enteros positivos.")


def potencia(base,exponente): # Defino la función
    resultado= base**exponente
    print("La potencia entre {0} elevado a la {1} es: {2}".format(base,exponente,resultado)) # Salida por pantalla
    return resultado

potencia(base,exponente) # Llamo a la función