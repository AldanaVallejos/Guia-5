#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 3: Dada una serie de números enteros, informar:
#              a)	su factorial
#              b)	cuantos múltiplos de 3
#              c)	cuantos múltiplos de 5
#              d)	cuantos múltiplos de 3 y de 5
#              Utilice las funciones de ejercicios anteriores.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
multiplo=0
n=0
def factorialymultiplos(): #Defino la función
    #Declaro variables
    factorial=1
    contadorm3=-1
    contadorm5=-1
    contadorm3y5=-1
    continuar=True
    n=0

    while continuar==True:
        try: 
            n=int(input("Ingrese un número entero (finaliza con un 0): ")) #Ingreso de dato
        except ValueError:
            print("Error. Tiene que ingresar números") #Validacion
    
        if n>0: #a)
            for i in range(1,n+1):
                factorial=factorial*i
            print("El factorial de {0} es {1}".format(n,factorial))
            factorial=1
        
        if n%3==0:
            contadorm3=contadorm3+1
        
        if n%5==0:
            contadorm5=contadorm5+1
        
        if n%3==0 and n%5==0:
            contadorm3y5=contadorm3y5+1
        
        if n==0:
            break

    #Salidas por pantalla
    print("Hay {0} múltiplos de 3".format(contadorm3))
    print("Hay {0} múltiplos de 5".format(contadorm5))
    print("Hay {0} múltiplos de 3 y de 5".format(contadorm3y5))
    
    return factorial,contadorm3y5,contadorm3,contadorm5

factorialymultiplos()  #Llamo a la función