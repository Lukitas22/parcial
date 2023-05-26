import re 
import json


def leer_archivo(nombre_archivo: str):
    lista_jugadores = []
    with open(nombre_archivo, "r", encoding = "utf-8") as file:
        dict = json.load(file)
        lista_jugadores = dict["jugadores"]

    return lista_jugadores

lista_de_jugadores = leer_archivo("Primer Parcial\pp_lab1_casas_lucas\dt.json")

#PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1

def listar_jugadores(lista_jugadores: list):
    """
    -Lista los jugadores con el siguiente formato. ejemplo:
        'Nombre: Michael Jordan - Posicion: Escolta'

    -Recibe la lista con diccionarios de jugadores de basquet.

    -Devuelve el listado impreso por consola.
    """
    for jugador in lista_jugadores:
        datos_jugadores = "Nombre: {0} - Posicion: {1}".format(jugador["nombre"], jugador["posicion"])
        print(datos_jugadores)


#listar_jugadores(lista_de_jugadores)

#PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 

def mostrar_estadisticas_jugadores(lista_jugadores: list, indice: str) -> str:
    lista_estadisticas = []

    if (indice < len(lista_jugadores)):
        estadisticas = lista_jugadores[indice]["estadisticas"]
        nombre_jugador = lista_jugadores[indice]["nombre"]
        print("Nombre Jugador: {0}".format(nombre_jugador))

        for key, value in estadisticas.items():
            key = key.replace("_", " ")
            estadisticas_individuales = "{0}: {1}".format(key, value)
            print(estadisticas_individuales)
            lista_estadisticas.append(estadisticas_individuales)
    else:
        print("ERROR. EL indice elegido no existe.")


    for estadistica in lista_estadisticas:
        separador = ", "
        estadistica = separador.join(lista_estadisticas)

    return estadistica



# print("0. Michael Jordan")
# print("1. Magic Johnson")
# print("2. Larry Bird")
# print("3. Charles Barkley")
# print("4. Scottie Pippen")
# print("5. David Robinson")
# print("6. Patrick Ewing")
# print("7. Karl Malone")
# print("8. John Stockton")
# print("9. Clyde Drexler")
# print("10. Chris Mullin")
# print("11. Christian Laettner")


# indice_txt = input("Ingrese el indice del jugador a ver sus estadisticas: ")
# indice_int = int(indice_txt)

# estadisticas = mostrar_estadisticas_jugadores(lista_de_jugadores, indice_int)

#PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3

def crear_archivo_csv_estadisticas(estadisticas_jugadores: str):
    pass


#PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4


def mostrar_logros_jugador(lista_jugadores: list, nombre_jugador: str):
    patron = rf"{nombre_jugador.capitalize()}"

    if (nombre_jugador == " "):
        mensaje = "ERROR. Ingrese algun nombre."
        return mensaje

    for jugador in lista_jugadores:
        resultado = re.search(patron, jugador["nombre"])
        if (resultado):
            print(jugador["nombre"])
            logros = jugador["logros"]
            separador = "\n"
            logros = separador.join(logros)
            return logros


nombre_jugador = input("Ingrese el nombre del jugador: ")

logros = mostrar_logros_jugador(lista_de_jugadores, nombre_jugador)
print(logros)


































