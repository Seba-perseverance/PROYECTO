from Movie import Movie

class Menu:

    def __init__():

        print("Seleccione una opcion ...")
        print("1 para listar las peliculas.. ")
        print("2 para agregar pelicula")
        print("0 para salir del sistema")

        valor = int(input("...\n"))

        if valor == 0:
            print("Adios ...")
        elif valor == 1:
            print("Listando peliculas")
            Movie.list_all()
        elif valor == 2:
            print("Solicitando datos de pelicula ...\n")
            title = input("Ingrese titulo de la pelicula ")
            movie = Movie(title)
            movie.save()
            print("Pelicula guardada exitosamente! \n")
        else:
            print("No se reconoce el comando ... :s")
            Menu.__init()

Menu.__init__()

