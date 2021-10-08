#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 1: Desarrollar una función que calcule el máximo común divisor de dos números enteros A, B con el siguiente algoritmo:
#1)	Dividir A por B, y calcular el resto (0 < R < B)
#2)	Si R = 0, el MCD es B, si no seguir en 3)
#3)	Reemplazar A por B, B por R, y volver al paso 1)
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
A=0
B=0
resto=0
mcd=0
continuar=True

def maximocomundivisor(A,B): #Defino la función
    resto=A%B
    if resto==0:
        mcd=B
        print("El máximo común divisor entre {0} y {1} es {2}".format(A,B,mcd)) #Salida por pantalla
    else:
        for i in range(int(B/2),0,-1): 
            if A%i==0 and B%i==0:
                mcd=i
                print("El máximo común divisor entre {0} y {1} es {2}".format(A,B,mcd)) #Salida por pantalla
                break
    return mcd

while continuar==True:
    continuar=False
    try:
        A=int(input("Ingrese un valor para A: "))
        B=int(input("Ingrese un valor para B: "))
    except ValueError:
        print("Error. Ingrese un número entero")
        A=int(input("Ingrese un valor para A: "))
        B=int(input("Ingrese un valor para B: "))

maximocomundivisor(A,B)