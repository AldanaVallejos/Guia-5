#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 9: Desarrollar un procedimiento tal que dada una hora (HHMMSS)
#              y un tiempo también en formato HHMMSS devuelva la nueva hora
#              que surge de sumar el tiempo a la hora  inicial, considere también si cambió el día.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Inicialización de variables
horas1=-1
minutos1=-1
segundos1=-1
horas2=-1
minutos2=-1
segundos2=-1
def tiempohoras(horas1,minutos1,segundos1,horas2,minutos2,segundos2): #Defino la funcion
    #Declaro variables
    horaactual=0
    horanueva=0
    tiempo=0

    horaactual=(horas1)+(minutos1)+(segundos1)
    horanueva=(horas2*10000)+(minutos2*100)+(segundos2)
    print("Hora en formato HHMMSS: ",int(horanueva)) #Salida por pantalla
    tiempo= horaactual+horanueva

    if tiempo>240000:
        horario=tiempo-240000
        print("El tiempo superando un día es: {0}".format(int(horario))) #Salida por pantalla
        return horario
    else:
        print("La suma de el primer horario ingresado con el segundo es: {0}".format(int(tiempo))) #Salida por pantalla
        return tiempo
    
# Ingreso de datos
while horas1<0 and minutos1<0 and segundos1<0: #validaciones
    try:
        horas1=int(input("Ingrese valores para las horas: ")) # Ingreso de dato
        if horas1<0:
            print("Error. Ingrese una hora válida.")
        else:
            minutos1=int(input("Ingrese valores para los minutos: "))
            if minutos1<0:
                print("Error. Ingrese minutos válidos")
                minutos1=int(input("Ingrese valores para los minutos: "))
            else:
                segundos1=int(input("Ingrese valores para los segundos: "))
                if segundos1<0:
                    print("Error. Ingrese valores válidos")
                    segundos1=int(input("Ingrese valores para los segundos: "))
    except ValueError:
        print("Error. Usted no está ingresando números.")
while horas2<0 and minutos2<0 and segundos2<0: #validaciones
    try:
        horas2=int(input("Ingrese horas para el nuevo tiempo: ")) # Ingreso de dato
        if horas2<0:
            print("Error. Ingrese una hora válida.")
        else:
            minutos2=int(input("Ingrese minutos para el nuevo tiempo: "))
            if minutos2<0:
                print("Error. Ingrese minutos válidos")
                minutos2=int(input("Ingrese minutos para el nuevo tiempo: "))
            else:
                segundos2=int(input("Ingrese segundos para el nuevo tiempo: "))
                if segundos2<0:
                    print("Error. Ingrese valores válidos")
                    segundos2=int(input("Ingrese segundos para el nuevo tiempo: "))
    except ValueError:
        print("Error. Usted no está ingresando números.")
tiempohoras(horas1,minutos1,segundos1,horas2,minutos2,segundos2) # Llamo a la función