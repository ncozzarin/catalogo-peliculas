from domain.movieClass import Movie
import os 
class Catalog(Movie):
    ruta_archivo = "peliculas.txt"
    def __init__(self,nombre):
        super().__init__(nombre)

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(Catalog.ruta_archivo, "a")
            archivo.write(pelicula.__str__() + "\n")       
        except Exception as e:
            print("Oops ocurrio un error:", e)
        finally:
            archivo.close()
        
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(Catalog.ruta_archivo, "r")
            print("Catalogo de peliculas")
            print(archivo.read())
        except Exception as e:
            print("Error",e)
        finally:
            archivo.close()

    @staticmethod
    def borrar_archivo():
        os.remove(Catalog.ruta_archivo)
        print("Archivo eliminado")