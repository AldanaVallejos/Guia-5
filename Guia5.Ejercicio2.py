#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 2: Desarrollar una función tal que dado un  número entero positivo calcule y retorne su factorial.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: 
# Salidas: 
# Procesos: 
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
n=-1

def factorial(n): #Defino la función
    factorial=1
    if n!=0:
        for i in range(1,n+1):
            factorial=factorial*i
    print("El factorial de {0} es {1}".format(n,factorial)) #Salida por pantalla
    return factorial #Retorno el factorial

try: #Validacion
    while n<0:
        n=int(input("Ingrese un entero positivo para calcular su factorial: ")) #Ingreso de dato
        if n<0:
            print("Error. Tiene que ser un número positivo") #Validacion
except ValueError:
    print("Error. Ingrese un número entero positivo")
    n=int(input("Ingrese un entero positivo para calcular su factorial: "))

factorial(n)