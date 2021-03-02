from domain.movieClass import Movie
from service.catalogClass import Catalog
op = None
while op != "4":
    print("1. Agregar pelicula \n")
    print("2. Listar peliculas \n")
    print("3. Eliminar archivo \n")
    op = input("Elija una opcion con su teclado:")
    if op == "1":
        nombre_pelicula = input("Agregue el titulo de la pelicula: ")
        pelicula = (nombre_pelicula)
        Catalog.agregar_pelicula(pelicula)
    elif op == "2":
        Catalog.listar_peliculas()
    elif op == "3":
        Catalog.borrar_archivo()
else:
    print("Salimos del programa.")