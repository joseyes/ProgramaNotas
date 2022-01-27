import usuarios.usuario as modelo
import notas.acciones 

class Acciones:

    def registro(self):

        print("\nOk!! vamos a registrate en el sistema")
        nombre = input("Ingresa tu nombre: ")
        apellidos = input ("Ingresa tus apellidos: ")
        email = input ("Ingresa tu email: ")
        password = input ("Ingresa una contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print (f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}\n")
        else:
            print ("\nNo te has podido registrar correctamente")
    
    
    def login(self):

        print("\nIndentificate en el sistema...")

        try:
            email = input ("Ingresa tu email: ")
            password = input ("Ingresa tu contraseña: ")

            usuario = modelo.Usuario('', '',email,password)
            login = usuario.indentificar()

            if email == login[3]:
                print (f"\nBienvenido {login[1]}, te has registrado en el sistema {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print (f"Login incorrecto!!! Intente de nuevo")

    
    def proximasAcciones(self, usuario):
        print ("""

        Acciones disponible :

        -Crear nota (crear)
        -Mostrar nota (mostrar)
        -Editar nota (editar)
        -Eliminar nota (eliminar)
        
        -Salir (salir)        

        """)
        
        accion = input ("¿Que quieres hacer?: ")

        realiza = notas.acciones.Acciones()

        if accion == "crear":
            realiza.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mostrar":
            realiza.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            realiza.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "editar":
            realiza.edit(usuario)
            self.proximasAcciones(usuario)
    
       
        elif accion == "salir":
            print (f"\nOk {usuario[1]}, hasta pronto")
            exit()

        


