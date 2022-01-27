"""
Crear una aplicacion de consola que realice lo siguente:

-   1) Abrir un asistente
    2) Login o registro 
    3) Si elegimos registro creara un usuario en la base de datos
    4) Si elegimos login, identificara al usuario y nos preguntura lo siguiente:
    5) - Crear Notas, Mostrar Notas, Eliminar Notas

"""
from usuarios import acciones

print ("""

Acciones disponibles:
    -registro
    -login

""")

realizar = acciones.Acciones()  #Instanciamos la clase que tenemos dentro del modulo acciones

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    realizar.registro()
    
elif accion == "login":
    realizar.login()




