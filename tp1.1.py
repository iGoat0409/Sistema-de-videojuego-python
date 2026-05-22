
import os
import random

#Variables globales para el reporte
jugador_A = ""
veces_jugado_A = 0
mayor_racha_A = 0
jugador_B = ""
veces_jugado_B = 0
victoria_B = 0
derrota_B = 0
jugador_D = ""
victoria_D = 0
derrota_D = 0
veces_jugado_D = 0

# Cartel de inicio
print("\n**************************************************************")
print("*                                                            *")
print("* ¡ADVERTENCIA!                                              *")
print("*                                                            *")
print("* LOS JUEGOS DE APUESTA ESTAN PROHIBIDOS PARA MENORES        *")
print("* Y SON PERJUDICIALES PARA LA SALUD.                         *")
print("*                                                            *")
print("**************************************************************")

input("\n[ Presione ENTER para continuar ]") # Se puede escribir y no pasa nada, corregir eso
os.system('cls') 

# modulos del menu y los juegos
def MENU():
    print("\n==============================")
    print("       MENU PRINCIPAL")
    print("==============================")
    print("A. Juego del menor-mayor")
    print("B. Adivinar el numero secreto")
    print("C. Blackjack")
    print("D. Par o impar")
    print("E. Reporte")
    print("S. Salir del programa")
    print("------------------------------")
    print("Juegue con moderacion. Solo para mayores de 18 años.")
    print("Asistencia al jugador: 0800-444-58346")
    print("------------------------------")

def juego_1(): # Mayor o menor.
    print("\n*********************************")
    print("¡Bienvenido al juego del mayor o menor!")
    print("Adivina si el siguiente numero es mayor o menor al mio")
    print("*********************************")
    global jugador_A, veces_jugado_A, mayor_racha_A
    nombre = input("\nIngresa tu nombre: ")
    jugador_A = nombre
    racha = 0
    numActual = random.randint(1, 1000)
    numNuevo = random.randint(1, 1000)
    print(f"El numero actual es: {numActual}")
    print("¿El siguiente numero es mayor o menor?")
    respuesta = input("Ingresa si es mayor o menor: ").upper()
    while respuesta != "MAYOR" and respuesta != "MENOR":
        respuesta = input("Respuesta incorrecta. Ingresa 'mayor' o 'menor': ").upper()
    while (respuesta == "MAYOR" and numNuevo > numActual) or (respuesta == "MENOR" and numNuevo < numActual):
        os.system('cls')
        print(f"¡Correcto! El numero nuevo es: {numNuevo}")
        racha += 1
        numActual = numNuevo
        numNuevo = random.randint(1, 1000)
        print(f"Racha actual: {racha}")
        print(f"El numero actual es: {numActual}")
        print("¿El siguiente numero es mayor o menor?")
        respuesta = input("Ingresa si es mayor o menor: ").upper()
        while respuesta != "MAYOR" and respuesta != "MENOR":
            respuesta = input("Respuesta incorrecta. Ingresa 'mayor' o 'menor': ").upper()
    os.system('cls')
    print(f"¡Incorrecto! El número era: {numNuevo}")
    print("Fin del juego")
    print(f"Jugador: {nombre}")
    print(f"Racha final de aciertos: {racha}")
    if racha > mayor_racha_A:
        mayor_racha_A = racha
    input("\n[ Presione ENTER para retornar al menú principal ]")

def juego_2(): # Numero secreto.
    nombre = input("\nNombre de usuario: ")
    numSecreto = random.randint(1, 100)
    intentos = 6
    aciertos = 0
    acerto = "no"
    while intentos > 0 and acerto == "no":
        print(f"\nIntentos restantes: {intentos}")
        numJugador = int(input("Ingrese un número entre 1 y 100: ")).isdigit()

    
        # da igual que el numero que se ingresa no este entre 1 y 100, el juego continua como si nada.
        if numJugador == numSecreto:
            acerto = "si"
            aciertos = aciertos + 1
            cantIntentos = 7 - intentos
            print(f"\n¡Felicidades {nombre}! Has adivinado el número secreto en {cantIntentos} intentos.")
            input("\n[ Presione ENTER para continuar ]")
        else:
            intentos = intentos - 1
            if intentos == 0:
                print(f"\n¡Perdiste {nombre}! El número secreto era {numSecreto}.")
            else:
                if int(numJugador) < numSecreto:
                        print("\nEl número secreto es mayor.")
                else:
                        print("\nEl número secreto es menor.")

def juego_3(): # Blackjack.
    print("\n*********************************")
    print("* JUEGO EN CONSTRUCCION          *")
    print("*********************************")
    input("\n[ Presione ENTER para retornar al menú principal ]")

def juego_4(): # Dedos: Par o impar.
    print("------------------------------------------------------------")
    print("Adivina si el resultado de tirar dos dados es par o impar")
    print("------------------------------------------------------------")
    global victoria_D, derrota_D, veces_jugado_D, jugador_D
    Continuar = "S"
    nombre = input("\nNombre de usuario: ")
    creditos = 100
    jugador_D = nombre
    os.system('cls')
    while Continuar == "S" and creditos > 0:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        print(f"\n{nombre}, tienes {creditos} créditos disponibles.")
        apuesta = input("\n¿Cuántos créditos desea apostar? ")
        while not apuesta.isdigit():
            apuesta = input("\nEntrada inválida. Ingrese un número válido: ")
        apuesta = int(apuesta)
        
        # --- FILTRO DE RANGO ---
        while apuesta > creditos or apuesta <= 0:
            # Pedimos el dato siempre como texto en la variable base
            apuesta = input("\nIngrese una cantidad de créditos válida: ")
            
            # barremos las letras si es que puso alguna
            while not apuesta.isdigit():
                apuesta = input("\nEntrada inválida. Ingrese un número válido: ")
            
            # 👇 LA CLAVE: El casteo se hace ACÁ, afuera del while de letras,
            # asegurando que 'apuesta' SIEMPRE suba al inicio del bucle como un INT.
            apuesta = int(apuesta)
        eleccion = input("\nLos dados fueron lanzados. ¿Es la suma par o impar? (P/I): ").upper()
        while (eleccion != "P" and eleccion != "I"):
            eleccion = input("\nEntrada inválida. Ingrese 'P' para par o 'I' para impar: ").upper()
        if (suma % 2 == 0 and eleccion == "P") or (suma % 2 != 0 and eleccion == "I"):
            os.system('cls')
            creditos += apuesta
            victoria_D += 1
            print(f"¡Correcto! La suma de los dados es {suma}.")
        else:
            os.system('cls')
            print(f"¡Incorrecto! La suma de los dados es {suma}.")
            creditos -= apuesta
            derrota_D += 1
        print(f"Créditos restantes: {creditos}")
        print(f"Victorias: {victoria_D} | Derrotas: {derrota_D}")
        print("\n¿Desea jugar otra ronda de Par o Impar?")
        Continuar = input("\n(S/N): ").upper()
        while Continuar != "S" and Continuar != "N":
            Continuar = input("Entrada inválida. Ingrese 'S' para sí o 'N' para no: ").upper()
    if creditos <= 0:
        print("\n¡Has perdido todos tus créditos! Fin del juego.")
        input("\n[ Presione ENTER para retornar al menú principal ]")
    else:
        print("\nGracias por jugar Par o Impar.")
        input("\n[ Presione ENTER para retornar al menú principal ]")
    os.system('cls')

def stats(): # Victorias, derrotas, rachas, etc.
    print("\n*****************************************************************")
    print("                      ESTADISTICAS GENERALES                      ")
    print("*****************************************************************")
    # juego A:
    print("\n[ JUEGO A: MAYOR O MENOR ]")
    print(f"  > Ultimo jugador en la mesa   : {jugador_A}")
    print(f"  > Cantidad de veces jugado    : {veces_jugado_A}")
    print(f"  > Mayor racha alcanzada       : {mayor_racha_A} aciertos")
    print("-----------------------------------------------------------------")
    # juego B:
    print("\n[ JUEGO B: Numero Secreto ]")
    print(f"  > Ultimo jugador en la mesa   : {jugador_B}")
    print(f"  > Cantidad de veces jugado    : {veces_jugado_B}")
    print(f"  > Rondas ganadas totales      : {victoria_B}")
    print(f"  > Rondas perdidas totales     : {derrota_B}")
    print("-----------------------------------------------------------------")
    # juego D:
    print("\n[ JUEGO D: PAR O IMPAR ]")
    print(f"  > Ultimo jugador en la mesa   : {jugador_D}")
    print(f"  > Cantidad de veces jugado    : {veces_jugado_D}")
    print(f"  > Rondas ganadas totales      : {victoria_D}")
    print(f"  > Rondas perdidas totales     : {derrota_D}")
    print("-----------------------------------------------------------------")
    input("\n[ Presione ENTER para regresar al menú principal ]")
    os.system('cls')

# menu principal
opcion = ""
while opcion != "S":
    MENU()
    opcion = input("Ingrese una opcion: ")
    while opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E" and opcion != "S":
        opcion = input("Opcion Incorrecta: ")
    
    match opcion:
        case "A":
            os.system('cls')
            veces_jugado_A += 1
            juego_1()
        case "B":
            os.system('cls')
            veces_jugado_B += 1
            juego_2()
        case "C":
            os.system('cls')
            juego_3()   
        case "D":
            os.system('cls')
            veces_jugado_D += 1
            juego_4()
        case "E":
            os.system('cls')
            stats()
        case "S":
            print("\n=======================================================")
            print("Gracias por jugar, no apueste, juegue por diversion.")
            print("=======================================================")
            input("\n[ Presione Enter para cerrar el programa ]")