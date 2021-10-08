#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 6: Desarrollar un procedimiento que imprima una fecha en
#              formato DD/MM/AA. El dato que recibe es un longint con una fecha en formato aaaammdd.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
f=0

def fechas(f): #Defino la función
    import datetime 
    f=datetime.datetime.strptime(f, '%Y%m%d').date()
    tiempo=datetime.datetime.strftime(f,'%d/%m/%y') #Cambio el formato de la fecha
    print("La fecha ingresada en formato DD/MM/AA es: {0}".format(tiempo)) # Salida por pantalla
     
try:# Validación
    f=int(input("Ingrese una fecha en formato (aaaammdd): ")) #Ingreso de dato
except ValueError:
    print("Error. Ingrese un numero tipo longint")
    f=int(input("Ingrese una fecha en formato (aaaammdd): "))
f=str(f)
fechas(f)