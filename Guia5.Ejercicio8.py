#***********************************************************
# Guia de ejercitación nº5
# Fecha: 06/10/21
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 8: Desarrollar una rutina tal que dada una fecha (AAAAMMDD)
#              y un número natural que representa una cantidad de días, calcule
#              y retorne la nueva fecha en tres parámetros  año (AAAA), mes (MM) y día (DD)
#              que resulte de incrementar al parámetro fecha con el parámetro cantidad de días. 
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numero=-1
f=-1

def sumafecha(f,numero): # Defino la función
    import datetime
    f=str(f)
    try: #validacion
        f=datetime.datetime.strptime(f, '%Y%m%d').date()
    except ValueError:
        print("Error. Ingrese una fecha válida")
    nuevafecha = f + datetime.timedelta(days=numero) # Sumo los diás
    nuevafecha= datetime.datetime.strftime(nuevafecha,'(%Y) (%m) (%d)') # Modifico el formato
    print("La nueva fecha es: {0}".format(nuevafecha)) # Salida por pantalla
    return(nuevafecha)


# Ingreso de datos
while f<0: #validacion
    try:
        f=int(input("Ingrese una fecha en formato (AAAAMMDDD): ")) # Ingreso de dato
        if f<0:
            print("Error. Ingrese números que representen una fecha.")
    except ValueError:
        print("Error. Tiene que ingresar una fecha.")
while numero<0: #validacion
    try:
        numero=int(input("Ingrese un número de días: ")) # Ingreso de dato
        if numero<0:
            print("Error. Ingrese un número natural.")
    except ValueError:
        print("Error. Tiene que ingresar un número")

sumafecha(f,numero) # Llamo a la función