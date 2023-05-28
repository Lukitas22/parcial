import re 
import json


def leer_archivo(nombre_archivo: str):
    lista_jugadores = []
    with open(nombre_archivo, "r", encoding = "utf-8") as file:
        dict = json.load(file)
        lista_jugadores = dict["jugadores"]

    return lista_jugadores

lista_de_jugadores = leer_archivo("Primer Parcial\pp_lab1_casas_lucas\dt.json")

def quick_sort(lista_original: list, key: str, flag_orden: bool) -> list:
    lista_de = []
    lista_iz = []

    if (len(lista_original) <= 1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if (elemento[key] > pivot[key] and flag_orden == True or elemento[key] < pivot[key] and flag_orden == False):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    
    lista_iz = quick_sort(lista_iz, key, flag_orden)
    lista_iz.append(pivot) 
    lista_de = quick_sort(lista_de, key, flag_orden)
    lista_iz.extend(lista_de) 

    return lista_iz

#PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1 PUNTO 1

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

#PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 PUNTO 2 

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

#PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3

def crear_archivo_csv_estadisticas(estadisticas_jugadores: str):
    pass


#PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4


def mostrar_logros_jugador(lista_jugadores: list, nombre_jugador: str) -> str:
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


# nombre_jugador = input("Ingrese el nombre del jugador: ")

# logros = mostrar_logros_jugador(lista_de_jugadores, nombre_jugador)
# print(logros)



#PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 PUNTO 5 

def calcular_promedio_puntos_partido(lista_jugadores: list) -> float:
    acumulador_puntos = 0
    contador_puntos = 0

    lista_ordenada = quick_sort(lista_jugadores, "nombre", True)
    for jugador in lista_ordenada:
        print("nombre jugador: {0} || Promedio de puntos por partido: {1}".format(jugador["nombre"],
                                                                                  jugador["estadisticas"]["promedio_puntos_por_partido"]))

    for jugador in lista_jugadores:
        acumulador_puntos += jugador["estadisticas"]["promedio_puntos_por_partido"]
        contador_puntos += 1
    
    promedio = acumulador_puntos / contador_puntos
    promedio = round(promedio, 2)

    return promedio


#promedio = calcular_promedio_puntos_partido(lista_de_jugadores)

#PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 PUNTO 6 


def mostrar_miembro_salon_fama(lista_jugadores: list, nombre_jugador: str) -> str:
    patron_nombre = rf"{nombre_jugador.capitalize()}"
    patron = r"Fama"
    
    for jugador in lista_jugadores:
        resultado = re.search(patron_nombre, jugador["nombre"])
        if (resultado):
            logros = jugador["logros"]
            separador = ","
            logros = separador.join(logros)
            miembro = re.search(patron, logros)
            if (miembro):
                return "El jugador: {0} es miembro del salon de la fama.".format(jugador["nombre"])
            else:
                return "El jugador: {0} NO es miembro del salon de la fama.".format(jugador["nombre"])
                

# nombre_jugador = input("Ingrese el nombre de un jugador: ")

# miembro = mostrar_miembro_salon_fama(lista_de_jugadores, nombre_jugador)
# print(miembro)


#PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7 PUNTO 7

def calcular_y_mostrar_mayor_segun_key(lista_jugadores: list, key: str) -> str:
    mayor_segun_key = 0
    mayor_logros = 0

    if (key != "logros"):
        for jugador in lista_jugadores:
            if (jugador["estadisticas"][key] > mayor_segun_key):
                mayor_segun_key = jugador["estadisticas"][key] 
                jugador_mayor_segun_key = jugador

        mensaje = "El jugador con mayor cantidad de {0} es: {1}, con un total de: {2}".format(key.replace("_", " "), jugador_mayor_segun_key["nombre"],
                                                                              jugador_mayor_segun_key["estadisticas"][key])

    else:
        for jugador in lista_jugadores:
            if (len(jugador["logros"]) > mayor_logros):
                mayor_logros = len(jugador["logros"])
                jugador_mayor_logros = jugador

        mensaje = "El jugador con mayor cantidad de logros es: {0}, con un total de: {1}".format(jugador_mayor_logros["nombre"],
                                                                              len(jugador_mayor_logros["logros"]))

    return mensaje


# jugador_mayor_rebotes = calcular_y_mostrar_mayor_segun_key(lista_de_jugadores, "rebotes_totales")
# print(jugador_mayor_rebotes)


#PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 PUNTO 8 

# jugador_mayor_tiros_campo = calcular_y_mostrar_mayor_segun_key(lista_de_jugadores, "porcentaje_tiros_de_campo")
# print(jugador_mayor_tiros_campo)


#PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9 PUNTO 9

# jugador_mayor_asistencias = calcular_y_mostrar_mayor_segun_key(lista_de_jugadores, "asistencias_totales")
# print(jugador_mayor_asistencias)


#PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10 PUNTO 10

def calcular_mayor_segun_key(lista_jugadores: list, numero_ingresado: float, key: str) -> str:
    lista_jugadores_mayores = []
    lista_textos = []
    jugadores_mayores = "No hay ningun jugador mayor al numero ingresado, ingrese un numero mas bajo."

    if (type(numero_ingresado) != float):
        return "ERROR. No se ingreso un numero."

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

    for jugador in lista_jugadores:
        if (jugador["estadisticas"][key] > numero_ingresado):
            lista_jugadores_mayores.append(jugador)
    
    for jugador in lista_jugadores_mayores:
        texto = "El jugador: {0} tiene un total de {1} de {2}\n".format(jugador["nombre"],
                                                                       jugador["estadisticas"][key], key.replace("_"," "))
        lista_textos.append(texto)
        separador = ""
        jugadores_mayores = separador.join(lista_textos)
    
    print("El/Los jugadores que tienen mayor cantidad de {0} que el numero ingresado son: ".format(key.replace("_"," ")))
    return jugadores_mayores


# numero_txt = input("Ingrese un numero: ")
# numero_float = float(numero_txt)

# mayor_promedio_puntos_partido = calcular_mayor_segun_key(lista_de_jugadores, numero_float, "promedio_puntos_por_partido")
# print(mayor_promedio_puntos_partido)


#PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 PUNTO 11 

# numero_txt = input("Ingrese un numero: ")
# numero_float = float(numero_txt)

# mayor_promedio_rebotes_partido = calcular_mayor_segun_key(lista_de_jugadores, numero_float, "promedio_rebotes_por_partido")
# print(mayor_promedio_rebotes_partido)


#PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12 PUNTO 12

# numero_txt = input("Ingrese un numero: ")
# numero_float = float(numero_txt)

# mayor_promedio_asistencias_partido = calcular_mayor_segun_key(lista_de_jugadores, numero_float, "promedio_asistencias_por_partido")
# print(mayor_promedio_asistencias_partido)


#PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13 PUNTO 13

# jugador_mayor_robos = calcular_y_mostrar_mayor_segun_key(lista_de_jugadores, "robos_totales")
# print(jugador_mayor_robos)

#PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 PUNTO 14 

# jugador_mayor_bloqueos = calcular_y_mostrar_mayor_segun_key(lista_de_jugadores, "bloqueos_totales")
# print(jugador_mayor_bloqueos)


#PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 PUNTO 15 

# numero_txt = input("Ingrese un numero: ")
# numero_float = float(numero_txt)

# mayor_promedio_tiros_libres = calcular_mayor_segun_key(lista_de_jugadores, numero_float, "porcentaje_tiros_libres")
# print(mayor_promedio_tiros_libres)


#PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 PUNTO 16 

def calcular_promedio_puntos_partidos_sin_menor(lista_jugadores: list) -> float:
    menor = 999999
    acumulador = 0
    contador = 0

    for jugador in lista_jugadores:
        if (jugador["estadisticas"]["promedio_puntos_por_partido"] < menor):
            menor = jugador["estadisticas"]["promedio_puntos_por_partido"]
            jugador_menor_promedio = jugador
    
    for jugador in lista_jugadores:
        if (jugador == jugador_menor_promedio):
            pass
        else:
            acumulador += jugador["estadisticas"]["promedio_puntos_por_partido"]
            contador +=1
    
    promedio = acumulador / contador

    return promedio


# promedio_sin_menor = calcular_promedio_puntos_partidos_sin_menor(lista_de_jugadores)
# print("El promedio sin el jugador con la menor cantidad es:", promedio_sin_menor)


#PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 PUNTO 17 

# jugador_mayor_logros = calcular_y_mostrar_mayor_segun_key(lista_de_jugadores, "logros")
# print(jugador_mayor_logros)


#PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18 PUNTO 18

# numero_txt = input("Ingrese un numero: ")
# numero_float = float(numero_txt)

# mayor_promedio_tiros_triples = calcular_mayor_segun_key(lista_de_jugadores, numero_float, "porcentaje_tiros_triples")
# print(mayor_promedio_tiros_triples)


#PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19 PUNTO 19


# jugador_mayor_temporadas = calcular_y_mostrar_mayor_segun_key(lista_de_jugadores, "temporadas")
# print(jugador_mayor_temporadas)



#PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 PUNTO 20 



























