#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 4: Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad de simplificaciones.
#              Desarrolle y utilice una función que reciba dos números naturales y retorne el menor
#              factor común. Ej: 360/60 = 180/30 = 90/15 = 30/5 = 6/1
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
P=-1
Q=-1
def fraccion(P,Q): #Defino la función
    resto=P%Q
    numerador=0
    denominador=0
    if resto==0:
        mcd=Q
        numerador=P/mcd
        denominador=Q/mcd
        print("La fracción simplificada es {0}/{1}".format(numerador,denominador)) #Salida por pantalla
    else:
        for i in range(int(Q/2),0,-1):
            if P%i==0 and Q%i==0:
                mcd=i
                numerador=P/mcd
                denominador=Q/mcd
                print("La fracción simplificada es {0}/{1}".format(numerador,denominador)) #Salida por pantalla
                break
    from fractions import Fraction
    minimofactorcomun=Fraction(P,Q)
    print("El minimo factor común es: {0}".format(minimofactorcomun)) #Salida por pantalla

while P<0: #Validaciones
    try:
        P=int(input("Ingrese el valor de P: ")) #Ingreso de dato
        if P<0: # Validacion
            print("Error. Ingrese un valor mayor a 0")
    except ValueError:
        print("Error. Tiene que ingresar un número.")
    
while Q<=0: #Validaciones
    try:
        Q=int(input("Ingrese el valor de Q: "))
        if Q<=0:
            print("Error. Tiene que se un número mayor que 0")
    except ValueError:
        print("Error. Tiene que ingresar un número")
fraccion(P,Q) #Llamo a la función