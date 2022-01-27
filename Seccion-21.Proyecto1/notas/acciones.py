import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print (f"\nOK {usuario[1]} vamos a crear una nota ..... ")

        titulo = input ("Ingresa el titulo de la nota: ")
        descripcion = input ("Agrega el contenido de la nota: ")

        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        
        if guardar [0] >= 1:
            print (f"\nPerfecto has guardado la nota: {nota.titulo}")

        else:
            print (f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print (f"\nClaro {usuario[1]} estas son tus notas: ")

        nota = modelo.Nota(usuario[0])
        nota = nota.listar()

        for n in nota:
            print ("---------------------------------------")
            print (f"Titulo:", n[2])
            print (f"Contenido:",n[3])
            print ("---------------------------------------")

        
    def borrar(self, usuario):
        print (f"\nOkey {usuario[1]} vamos a eliminar notas...")

        titulo = input("\nIngresa el titulo de la nota que quieres borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print (f"\nListo ha sido eliminada la nota: {nota.titulo}")
        
        else:
            print ("No se ha borrado la nota")

    def edit(self, usuario):
        print (f"\nOK vamos a editar una nota!!!")

        titulo = input("Ingresa el titulo de la nota: ")
        descripcion = ("Ingresa o cambia el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        editar = nota.editar()
    

        if editar [0] >= 1:
            print (f"\nPerfecto has editado la nota: {nota.titulo}")

        else:
            print (f"\nNo se ha guardado la nota, lo siento {usuario[1]}")


    
