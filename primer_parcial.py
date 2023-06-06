import re 
import json


def leer_archivo_json(nombre_archivo: str) -> list:
    """
    -Esta funcion lee un archivo JSON.

    -Recibe un string, el cual sera la ubicacion del archivo a leer.

    -Devuelve la lista que contenga ese archivo JSON.
    """
    lista_jugadores = []
    with open(nombre_archivo, "r", encoding = "utf-8") as file:
        dict = json.load(file)
        lista_jugadores = dict["jugadores"]

    return lista_jugadores

lista_de_jugadores = leer_archivo_json("Primer Parcial\pp_lab1_casas_lucas\dt.json")


def quick_sort(lista_original: list, key: str, flag_orden: bool) -> list:
    """
    -Esta funcion ordena una lista segun la key ingresada.

    -Recibe la lista a ordenar, la key por la que se desea ordernar
        y un flag que indica si se desea ordenar de manera ascendente(False) o descendente(True).
        
    -Devuelve la lista ingresada ordenada.
    """
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

def quick_sort_estadisticas(lista_original: list, key: str, flag_orden: bool) -> list:
    """
    -Esta funcion ordena una lista segun la key ingresada.

    -Recibe la lista a ordenar, la key por la que se desea ordernar
        y un flag que indica si se desea ordenar de manera ascendente(False) o descendente(True).
        
    -Devuelve la lista ingresada ordenada.
    """
    lista_de = []
    lista_iz = []

    if (len(lista_original) <= 1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if (elemento["estadisticas"][key] > pivot["estadisticas"][key] and flag_orden == True or elemento["estadisticas"][key] < pivot["estadisticas"][key] and flag_orden == False):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    
    lista_iz = quick_sort_estadisticas(lista_iz, key, flag_orden)
    lista_iz.append(pivot) 
    lista_de = quick_sort_estadisticas(lista_de, key, flag_orden)
    lista_iz.extend(lista_de) 

    return lista_iz


def listar_jugadores(lista_jugadores: list):
    """
    -Lista los jugadores con el siguiente formato. ejemplo:
        'Nombre: Michael Jordan - Posicion: Escolta'

    -Recibe la lista con diccionarios de jugadores de basquet.

    -Devuelve el listado impreso por consola.
    """
    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."
    
    for jugador in lista_jugadores:
        datos_jugadores = "Nombre: {0} - Posicion: {1}".format(jugador["nombre"], jugador["posicion"])
        print(datos_jugadores)


def mostrar_estadisticas_jugadores(lista_jugadores: list, indice: str) -> dict:
    """
    -Muestra las estadisticas del jugador ingresado.

    -Recibe una lista de diccionarios con jugadores de basquet,
        y el indice del jugador que se desea ver las estadisticas.

    -Devuelve el diccionario del jugador ingresado por indice.
    """
    flag_indice_correcto = False

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

    if (indice < len(lista_jugadores)):
        flag_indice_correcto = True
        estadisticas = lista_jugadores[indice]["estadisticas"]
        nombre = lista_jugadores[indice]["nombre"]
        print("Nombre: {0}".format(nombre))
        
        for key, value in estadisticas.items():
            key = key.replace("_", " ")
            estadisticas_individuales = "{0}: {1}".format(key, value)
            print(estadisticas_individuales)
           
    else:
        print("ERROR. EL indice elegido no existe.")
    
    if (flag_indice_correcto == True):
        dict_jugador = lista_jugadores[indice]

        return dict_jugador


def crear_archivo_csv_estadisticas(dict_jugador: dict) -> bool:
    """
    -Crea el archivo CSV del jugador ingresado en la opcion 2.

    -Recibe un diccionario de un jugador.

    -Devuelve True en caso de que se haya podido crear el archivo y False en caso contrario.
    """
    lista_keys = ["nombre", "posicion"]
    lista_values = []

    nombre = dict_jugador["nombre"]
    posicion = dict_jugador["posicion"]
    jugador_estadisticas = dict_jugador["estadisticas"]
    
    for key, value in jugador_estadisticas.items():
        lista_keys.append(key)
        lista_values.append(str(value))

    separador = ","
    keys = separador.join(lista_keys)
    values = separador.join(lista_values)

    datos_a_guardar = "{0}\n{1},{2},{3}".format(keys.replace("_", " "), nombre, posicion, values)

    with open("Estadisticas.csv", "w") as file:
        creado = file.write(datos_a_guardar)

    if (creado):
        print("Se creó el archivo: {0}".format("Estadisticas.csv"))
        return True
    
    else:
        print("Error al crear el archivo: {0}".format("Estadisticas.csv"))
        return False

def mostrar_logros_jugador(lista_jugadores: list, nombre_jugador: str) -> str:
    """
    -Muestra los logros del jugador ingresado.

    -Recibe una lista de diccionarios con jugadores de basquet,
        y el nombre del jugador a mostrar sus logros.

    -Devuelve un string con todos los logros del jugador.
    """
    patron = rf"{nombre_jugador.capitalize()}"

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

    if (nombre_jugador == " " or nombre_jugador == ""):
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
        else:
            mensaje = "El nombre del jugador no se ingreso correctamente."
            return mensaje


def calcular_promedio_puntos_partido(lista_jugadores: list) -> float:
    """
    -Calcula el promedio de puntos por partido del equipo, y los ordena
        alfabeticamente, mostrando el nombre y el promedio de puntos de cada jugador.
    
    -Recibe una lista de diccionarios con jugadores de basquet.

    -Devuelve un float con el promedio calculado, y los jugadores ordenados impresos por consola.
    """
    acumulador_puntos = 0
    contador_puntos = 0

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

    lista_ordenada = quick_sort(lista_jugadores, "nombre", True)

    for jugador in lista_ordenada:
        print("Nombre jugador: {0} || Promedio de puntos por partido: {1}".format(jugador["nombre"],
                                                                                  jugador["estadisticas"]["promedio_puntos_por_partido"]))

    for jugador in lista_jugadores:
        acumulador_puntos += jugador["estadisticas"]["promedio_puntos_por_partido"]
        contador_puntos += 1
    
    promedio = acumulador_puntos / contador_puntos
    promedio = round(promedio, 2)

    return promedio


def mostrar_miembro_salon_fama(lista_jugadores: list, nombre_jugador: str) -> str:
    """
    -Busca si el jugador ingresado es miembro del salon de la fama de basquet.

    -Recibe una lista de diccionarios con jugadores de basquet, y el nombre del jugador.

    -Devuelve un mensaje(string) de si el jugador es o no miembro del salon de la fama.
    """
    patron_nombre = rf"{nombre_jugador.capitalize()}"
    patron = r"Fama"
    
    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

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
        else:
            return "El nombre del jugador no se ingreso correctamente."

def calcular_y_mostrar_mayor_segun_key(lista_jugadores: list, key: str) -> str:
    """
    -Calcula el jugador mayor segun la key ingresada.

    -Recibe una lista de diccionarios con jugadores de basquet, y la
        key por la que se desea saber el mayor.

    -Devuelve un mensaje(string) del nombre y dato del jugador mayor. ejemplo:
        "El jugador con mayor cantidad de puntos por partido es Michael Jordan con un total de 30.1".
    """
    mayor_segun_key = 0
    mayor_logros = 0

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

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


def calcular_mayor_ingreso_segun_key(lista_jugadores: list, numero_ingresado: float, key: str) -> str:
    """
    -Busca los jugadores mayores (segun la key ingresada) que el numero ingresado.

    -Recibe una lista de diccionarios con jugadores de basquet, el numero por el que se desea
        buscar los jugadores mayores y la key por la que se busca.
    
    -Devuelve un string con TODOS los jugadores mayores a ese numero y con este formato, ejemplo:
        "El jugador: Michael Jordan tiene un total de 30.1 de promedio de puntos por partido".
    """
    lista_jugadores_mayores = []
    lista_textos = []
    jugadores_mayores = "No hay ningun jugador mayor al numero ingresado, ingrese un numero mas bajo."

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

    for jugador in lista_jugadores:
        if (jugador["estadisticas"][key] > numero_ingresado):
            lista_jugadores_mayores.append(jugador)
    
    for jugador in lista_jugadores_mayores:
        texto = "El jugador: {0} tiene un total de {1} de {2}.\n".format(jugador["nombre"],
                                                                       jugador["estadisticas"][key], key.replace("_"," "))
        lista_textos.append(texto)
        separador = ""
        jugadores_mayores = separador.join(lista_textos)
    
    print("El/Los jugadores que tienen mayor cantidad de {0} que el numero ingresado son: ".format(key.replace("_"," ")))
    return jugadores_mayores


def calcular_promedio_puntos_partidos_sin_menor(lista_jugadores: list) -> float:
    """
    -Calcula el promedio de puntos por partido del equipo, exceptuando al jugador con menos promedio.

    -Recibe una lista de diccionarios con jugadores de basquet.

    -Devuelve el promedio calculado sin el jugador con menor promedio.
    """
    menor = 999999
    acumulador = 0
    contador = 0

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

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


def calcular_y_ordenar_mayor_ingreso_tiros_campo(lista_jugadores: list, numero_ingresado: float) -> str:
    """
    -Busca los jugadores con mayor promedio de tiros de campo que el numero ingresado.

    -Recibe una lista de diccionarios con jugadores de basquet y el numero ingresado por consola
        con el que se desea buscar los mayores.

    -Devuelve un string con todos los jugadores mayores a ese numero y ordenados de manera ascendente.
    """
    lista_jugadores_mayores = []
    lista_textos = []
    jugadores_mayores = "No hay ningun jugador mayor al numero ingresado, ingrese un numero mas bajo."

    if (len(lista_jugadores) == 0):
        return "ERROR. Lista vacia."

    lista_ordenada = quick_sort_estadisticas(lista_jugadores, "porcentaje_tiros_de_campo", True)

    for jugador in lista_ordenada:
        if (jugador["estadisticas"]["porcentaje_tiros_de_campo"] > numero_ingresado):
            lista_jugadores_mayores.append(jugador)
    
    for jugador in lista_jugadores_mayores:
        texto = "El jugador: {0} tiene un total de {1} de Porcentaje de tiros de campo.\n".format(jugador["nombre"],
                                                                       jugador["estadisticas"]["porcentaje_tiros_de_campo"])
        lista_textos.append(texto)
        separador = ""
        jugadores_mayores = separador.join(lista_textos)
    
    print("El/Los jugadores que tienen mayor cantidad de Porcentaje de tiros de campo que el numero ingresado son: ")
    
    return jugadores_mayores


def calcular_ranking_jugadores(lista_jugadores: list) -> list:
    """
    -Calcula la posicion de cada jugador segun una estadistica.

    -Recibe una lista de diccionarios con jugadores de basquet.

    -Devuelve una lista modificada con los ranking de los jugadores segun las estadistcas.
    """
    lista_estadisticas = ["rebotes_totales", "asistencias_totales", "robos_totales", "puntos_totales"]

    for estadistica in lista_estadisticas:
        lista_ordenada = quick_sort_estadisticas(lista_jugadores, estadistica , False)
        lista_estadisticas_jugadores = []

        for indice in range(len(lista_ordenada)):
            nombre_jugador = lista_ordenada[indice]["nombre"]
            lista_ordenada[indice]["estadisticas"][estadistica] = indice + 1
            dict_nombre_estadisticas = {
                "nombre": nombre_jugador,
                "estadisticas": lista_ordenada[indice]["estadisticas"]
            }

            lista_estadisticas_jugadores.append(dict_nombre_estadisticas)


    return lista_estadisticas_jugadores


def crear_csv_ranking(lista_estadisticas_jugadores: list) -> bool:
    """
    -Crea el archivo CSV del ranking de los jugadores segun una estadistica.

    -Recibe una lista modificada con los rankings.

    -Devuelve True en caso de que se haya podido crear el archivo y False en caso contrario.
    """
    lista_keys = ["nombre", "puntos totales", "rebotes totales", "robos totales"]
    lista_filas = []

    for jugador in lista_estadisticas_jugadores:
            values = [jugador["nombre"],
                       str(jugador["estadisticas"]["puntos_totales"]),
                       str(jugador["estadisticas"]["rebotes_totales"]),
                       str(jugador["estadisticas"]["robos_totales"])]
            
            separador = ","
            fila = separador.join(values)
            lista_filas.append(fila)

    separador = ","
    keys = separador.join(lista_keys)
    datos_a_guardar = "{0}\n{1}".format(keys, "\n".join(lista_filas))

    with open("ranking.csv", 'w+') as file:
        creado = file.write(datos_a_guardar)

    if (creado):
        print("Se creó el archivo: {0}".format("ranking.csv"))
        return True

    print("Error al crear el archivo: {0}".format("ranking.csv"))
    return False


def imprimir_ranking_en_tabla(lista_jugadores: list):
    """
    -Imprime la tabla del ranking.

    -Recibe la lista modificada con los rankings.

    -Devuelve la tabla impresa por consola.
    """
    print("_____________________________________________________________________________________")
    print("        Jugador        |    Puntos    |    Rebotes    |   Asistencias   |   Robos   |")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    for jugador in lista_jugadores:
        print("  {:^19s}  |  {:^10d}  |  {:^11d}  |  {:^13d}  |  {:^7d}  |".format(
            jugador["nombre"], jugador["estadisticas"]["puntos_totales"],
            jugador["estadisticas"]["rebotes_totales"], jugador["estadisticas"]["asistencias_totales"],
            jugador["estadisticas"]["robos_totales"]
        ))
        print("-------------------------------------------------------------------------------------")


#EXTRA 1 EXTRA 1 EXTRA 1 EXTRA 1 EXTRA 1 EXTRA 1 EXTRA 1 EXTRA 1 EXTRA 1 EXTRA 1

def calcular_jugadores_posicion(lista_jugadores: list):
    dict_contador = {}

    for jugador in lista_jugadores:
        if (jugador["posicion"] in dict_contador):
            dict_contador[jugador["posicion"]].append(jugador["nombre"])
        else:
            dict_contador[jugador["posicion"]] = [jugador['nombre']]
    
    for key in dict_contador:
        print(key + ":")
        for value in dict_contador[key]:
            print("\t- " + value)


#calcular_jugadores_posicion(lista_de_jugadores)


#EXTRA 2 EXTRA 2 EXTRA 2 EXTRA 2 EXTRA 2 EXTRA 2 EXTRA 2 EXTRA 2 EXTRA 2 EXTRA 2

def ordenar_cantidad_all_stars(lista_jugadores: list):
    patron = r"All-Star"
    for jugador in lista_jugadores:
        print(jugador["nombre"])
        for logro in jugador["logros"]:
            all_stars = re.search(patron, logro)
            if (all_stars):
                print(logro)


#ordenar_cantidad_all_stars(lista_de_jugadores)


def menu_principal(lista_jugadores):
    flag = False
    while True:
        print("Menu de opciones:")
        print("1. Listar los jugadores con su nombre y posición.")
        print("2. Mostrar estadisticas del indice de jugador ingresado por consola.")
        print("3. Guardar archivo del punto anterior en CSV.")
        print("4. Mostrar logros del jugador ingresado por consola.")
        print("5. Calcular promedio de puntos por partido del equipo y mostrar los jugadores de manera ascendente.")
        print("6. Mostrar si el jugador ingresado por consola es miembro del salon de la fama.")
        print("7. Mostrar el jugador con la mayor cantidad de rebotes totales.")
        print("8. Mostrar el jugador con el mayor porcentaje de tiros de campo.")
        print("9. Mostrar el jugador con la mayor cantidad de asistencias totales.")
        print("10. Mostrar los jugadores que han promediado más puntos por partido que el valor ingresado por consola.")
        print("11. Mostrar los jugadores que han promediado más rebotes por partido que el valor ingresado por consola.")
        print("12. Mostrar los jugadores que han promediado más asistencias por partido que el valor ingresado por consola.")
        print("13. Mostrar el jugador con la mayor cantidad de robos totales.")
        print("14. Mostrar el jugador con la mayor cantidad de bloqueos totales.")
        print("15. Mostrar los jugadores que han promediado más porcentaje de tiros libres que el valor ingresado por consola.")
        print("16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
        print("17. Mostrar el jugador con la mayor cantidad de logros obtenidos.")
        print("18. Mostrar los jugadores que han promediado más porcentaje de tiros triples que el valor ingresado por consola.")
        print("19. Mostrar el jugador con la mayor cantidad de temporadas jugadas.")
        print("20. Mostrar los jugadores ordenados por posición en la cancha, que han promediado más porcentaje de tiros de campo que el valor ingresado por consola.")
        print("23. Exportar a CSV un ranking de cada jugador, segun los puntos, rebotes, asistencias y robos.")
        print("0. Salir del menu.")
        opcion = input("\nIngrese la opción deseada: ")

        match opcion:
            case "1":
                listar_jugadores(lista_jugadores)
            case "2":
                print("0. Michael Jordan")
                print("1. Magic Johnson")
                print("2. Larry Bird")
                print("3. Charles Barkley")
                print("4. Scottie Pippen")
                print("5. David Robinson")
                print("6. Patrick Ewing")
                print("7. Karl Malone")
                print("8. John Stockton")
                print("9. Clyde Drexler")
                print("10. Chris Mullin")
                print("11. Christian Laettner")


                indice_txt = input("Ingrese el indice del jugador a ver sus estadisticas: ")
                indice_int = int(indice_txt)

                estadisticas = mostrar_estadisticas_jugadores(lista_jugadores, indice_int)
                flag = True
            case "3":
                pass
                if (flag):
                    crear_archivo_csv_estadisticas(estadisticas)
                else:
                    print("ERROR. primero ingrese la opcion 2")
            case "4":
                nombre_jugador = input("Ingrese el nombre del jugador: ")

                logros = mostrar_logros_jugador(lista_jugadores, nombre_jugador)
                print(logros)
            case "5":
                promedio = calcular_promedio_puntos_partido(lista_jugadores)
                print("El promedio total del equipo es: {0}".format(promedio))
            case "6":
                nombre_jugador = input("Ingrese el nombre de un jugador: ")

                miembro = mostrar_miembro_salon_fama(lista_jugadores, nombre_jugador)
                print(miembro)
            case "7":
                jugador_mayor_rebotes = calcular_y_mostrar_mayor_segun_key(lista_jugadores, "rebotes_totales")
                print(jugador_mayor_rebotes)
            case "8":
                jugador_mayor_tiros_campo = calcular_y_mostrar_mayor_segun_key(lista_jugadores, "porcentaje_tiros_de_campo")
                print(jugador_mayor_tiros_campo)
            case "9":
                jugador_mayor_asistencias = calcular_y_mostrar_mayor_segun_key(lista_jugadores, "asistencias_totales")
                print(jugador_mayor_asistencias)
            case "10":
                numero_txt = input("Ingrese un numero: ")
                patron = r"[0-9.0-9]"
                resultado = re.search(patron, numero_txt)
                if (resultado):
                    numero_float = float(numero_txt)
                    mayor_promedio_puntos_partido = calcular_mayor_ingreso_segun_key(lista_jugadores, numero_float, "promedio_puntos_por_partido")
                    print(mayor_promedio_puntos_partido)
                else:
                    print("Ingrese un numero.")
            case "11":
                numero_txt = input("Ingrese un numero: ")
                patron = r"[0-9.0-9]"
                resultado = re.search(patron, numero_txt)
                if (resultado):
                    numero_float = float(numero_txt)
                    mayor_tiros_campo = calcular_mayor_ingreso_segun_key(lista_jugadores, numero_float, "promedio_rebotes_por_partido")
                    print(mayor_tiros_campo)
                else:
                    print("Ingrese un numero.")
            case "12":
                numero_txt = input("Ingrese un numero: ")
                patron = r"[0-9.0-9]"
                resultado = re.search(patron, numero_txt)
                if (resultado):
                    numero_float = float(numero_txt)
                    mayor_promedio_asistencias_partido = calcular_mayor_ingreso_segun_key(lista_jugadores, numero_float, "promedio_asistencias_por_partido")
                    print(mayor_promedio_asistencias_partido)
                else:
                    print("Ingrese un numero.")
            case "13":
                jugador_mayor_robos = calcular_y_mostrar_mayor_segun_key(lista_jugadores, "robos_totales")
                print(jugador_mayor_robos)
            case "14":
                jugador_mayor_bloqueos = calcular_y_mostrar_mayor_segun_key(lista_jugadores, "bloqueos_totales")
                print(jugador_mayor_bloqueos)
            case "15":
                numero_txt = input("Ingrese un numero: ")
                patron = r"[0-9.0-9]"
                resultado = re.search(patron, numero_txt)
                if (resultado):
                    numero_float = float(numero_txt)
                    mayor_promedio_tiros_libres = calcular_mayor_ingreso_segun_key(lista_jugadores, numero_float, "porcentaje_tiros_libres")
                    print(mayor_promedio_tiros_libres)
                else: 
                    print("Ingrese un numero.")
            case "16":
                promedio_sin_menor = calcular_promedio_puntos_partidos_sin_menor(lista_jugadores)
                print("El promedio de puntos por partido sin el jugador con la menor cantidad es:", promedio_sin_menor)
            case "17":
                jugador_mayor_logros = calcular_y_mostrar_mayor_segun_key(lista_jugadores, "logros")
                print(jugador_mayor_logros)
            case "18":
                numero_txt = input("Ingrese un numero: ")
                patron = r"[0-9.0-9]"
                resultado = re.search(patron, numero_txt)
                if (resultado):
                    numero_float = float(numero_txt)
                    mayor_promedio_tiros_triples = calcular_mayor_ingreso_segun_key(lista_jugadores, numero_float, "porcentaje_tiros_triples")
                    print(mayor_promedio_tiros_triples)
                else: 
                    print("Ingrese un numero.")
            case "19":
                jugador_mayor_temporadas = calcular_y_mostrar_mayor_segun_key(lista_jugadores, "temporadas")
                print(jugador_mayor_temporadas)
            case "20":
                numero_txt = input("Ingrese un numero: ")
                patron = r"[0-9.0-9]"
                resultado = re.search(patron, numero_txt)
                if (resultado):
                    numero_float = float(numero_txt)
                    mayor_numero_tiros_campo = calcular_y_ordenar_mayor_ingreso_tiros_campo(lista_jugadores, numero_float)
                    print(mayor_numero_tiros_campo)
                else:
                    print("Ingrese un numero.")
            case "23":
                lista_ranking = calcular_ranking_jugadores(lista_de_jugadores)
                crear_csv_ranking(lista_ranking)
                imprimir_ranking_en_tabla(lista_ranking)
            case "0":   
                break
            case _:
                print("No se ingreso una opcion correcta (del 0 al 20).")
        
        input("\nPulse enter para continuar\n")
    

menu_principal(lista_de_jugadores)



