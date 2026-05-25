"""
VAR Globales:
jugador_A, jugador_B, jugador_D:string
veces_jugado_A, veces_jugado_B, veces_jugado_D:int
mayor_racha_A, victoria_A, derrota_A, victoria_D, derrota_D:int
VAR Juego B:
numSecreto, numJugador, intentos, cantIntentos:int
acerto, filtro_entero:string
VAR juego D:
continuar, apuesta, filtro_entero:string
creditos, dado1, dado2, suma:int

"""
import os
import random

#Variables globales para el reporte
jugador_A = "Sin registro"
veces_jugado_A = 0
mayor_racha_A = 0
jugador_B = "Sin registro"
veces_jugado_B = 0
victoria_B = 0
derrota_B = 0
jugador_D = "Sin registro"
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
    print("==============================")
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
    global jugador_A, veces_jugado_A, mayor_racha_A
    print("========================================")
    print("juego mayor o menor")
    print("========================================")
    jugador_A = input("\nNombre de usuario: ")
    numero_actual= random.randint(1, 1000)
    nuevo_numero = random.randint (1, 1000)
    puntaje=0
    seguir_jugando="si"

    while seguir_jugando == "si": 
    # Este while hace que mientras no pierda, el juego se repite.
        print(f"\nEl numero actual es: {numero_actual}")
        opcion = input("\nEl proximo numero sera MAYOR o MENOR?: ").upper()
        while opcion != "MAYOR" and opcion != "MENOR":
        # Este while valida que eligio una opcion correcta.
            opcion = input("Respuesta incorrecta. Ingresa 'mayor' o 'menor': ").upper()
    
        if (opcion=="MAYOR" and nuevo_numero > numero_actual) or (opcion=="MENOR" and nuevo_numero < numero_actual):
        # Con un solo if y un conector, verificamos si el jugador acerto o no.
            print ("¡correcto!")
            puntaje += 1
            numero_actual = nuevo_numero
            nuevo_numero = random.randint (1, 1000)
        else:
            seguir_jugando= "no"
            print ("\n===========================================")
            print("¡incorecto!")
            print(f"El numero nuevo era: {nuevo_numero}")
            print("fin del juego")
            print("racha de aciertos:", puntaje)
            print("===========================================")
            input("\n[ Presione ENTER para continuar ]")
    os.system('cls')
    
def juego_2(): # Numero secreto.
    global jugador_B, veces_jugado_B, victoria_B, derrota_B
    print("------------------------------------------")
    print("Adivina el numero secreto entre 1 y 100")
    print("------------------------------------------")
    jugador_B = input("\nNombre de usuario: ")
    numSecreto = random.randint(1, 100)
    intentos = 6
    acerto = "no"
    while intentos > 0 and acerto == "no":
        print(f"\nIntentos restantes: {intentos}")
        numJugador = (input("Ingrese un número entre 1 y 100: "))
        filtro_entero = 'no'
        while filtro_entero == 'no':
            if numJugador.isdigit():
                numJugador = int(numJugador)
                if numJugador >= 1 and numJugador <= 100:
                    filtro_entero = 'si'
                else:
                    numJugador = input("\nEntrada inválida. Ingrese un número entre 1 y 100: ")
            else:
                numJugador = input("\nEntrada inválida. Ingrese un número entre 1 y 100: ")
        if numJugador == numSecreto:
            acerto = "si"
            victoria_B = victoria_B + 1
            cantIntentos = 7 - intentos
            print(f"\n¡Felicidades {jugador_B}! Has adivinado el número secreto en {cantIntentos} intentos.")
            input("\n[ Presione ENTER para continuar ]")
        else:
            intentos = intentos - 1
            if intentos == 0:
                derrota_B = derrota_B + 1
                print(f"\n¡Perdiste {jugador_B}! El número secreto era {numSecreto}.")
                input("\n[ Presione ENTER para continuar ]")
            else:
                if (numJugador) < numSecreto:
                    print("\nEl número secreto es mayor.")
                else:
                    print("\nEl número secreto es menor.")
    os.system('cls')

def juego_3(): # Blackjack.
    print("\n*********************************")
    print("* JUEGO EN CONSTRUCCION         *")
    print("*********************************")
    input("\n[ Presione ENTER para retornar al menú principal ]")
    os.system('cls')

def juego_4(): # Dedos: Par o impar.
    print("------------------------------------------------------------")
    print("Adivina si el resultado de tirar dos dados es par o impar")
    print("------------------------------------------------------------")
    global victoria_D, derrota_D, veces_jugado_D, jugador_D
    continuar = "S"
    jugador_D = input("\nNombre de usuario: ")
    creditos = 100
    os.system('cls')
    while continuar == "S" and creditos > 0:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        print(f"\n{jugador_D}, tienes {creditos} créditos disponibles.")
        apuesta = input("\n¿Cuántos créditos desea apostar? ")
        # Diego llora cada vez que ve este bloque de codigo, pero no puedo usar booleanos xd
        filtro_entero = 'no'
        while filtro_entero == 'no':
            # Segun entendi, el isdigit verifica que el input sea un numero entero, si ya es un numero entero convierte el string a int y sale del bucle.
            if apuesta.isdigit(): 
                apuesta = int(apuesta)
                filtro_entero = 'si'
            else:
                apuesta = input("\nEntrada inválida. Ingrese un número válido: ")
        while apuesta > creditos or apuesta <= 0:
            apuesta = input("\nIngrese una cantidad de créditos válida: ")
            filtro_entero = 'no'
            while filtro_entero == 'no':
                if apuesta.isdigit():
                    apuesta = int(apuesta)
                    filtro_entero = 'si'
                else:
                    apuesta = input("\nEntrada inválida. Ingrese un número válido: ")
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
        continuar = input("\n(S/N): ").upper()
        while continuar != "S" and continuar != "N":
            continuar = input("Entrada inválida. Ingrese 'S' para sí o 'N' para no: ").upper()
    if continuar == "N":
        print(f"\nGracias por jugar, {jugador_D}. Volviendo al menú principal.")
        input("\n[ Presione ENTER para continuar ]")
    else:
        print(f"\n¡Has perdido todos tus créditos, {jugador_D}! Volviendo al menú principal.")
        input("\n[ Presione ENTER para continuar ]")
    os.system('cls')

def reporte(): # Victorias, derrotas, rachas, etc.
    print("\n*****************************************************************")
    print("                      ESTADISTICAS GENERALES                      ")
    print("*****************************************************************")
    # juego A:
    print("\n[ JUEGO A: MAYOR O MENOR ]")
    print(f"  > Ultimo jugador en la mesa   : {jugador_A}")
    print(f"  > Cantidad de veces jugado    : {veces_jugado_A}")
    print(f"  > Mayor racha alcanzada       : {mayor_racha_A}")
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
    opcion = input("Ingrese una opcion: ").upper()
    while opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E" and opcion != "S":
        opcion = input("Opcion Incorrecta: ").upper()
    # upper() convierte en mayuscula el input.
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
            reporte()
        case "S":
            print("\n=======================================================")
            print("Gracias por jugar, no apueste, juegue por diversion.")
            print("=======================================================")
            input("\n[ Presione Enter para cerrar el programa ]")