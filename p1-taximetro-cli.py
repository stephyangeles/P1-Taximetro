import os
import time
import threading
from colorama import init, Fore

# colorama init
init(autoreset=True)

# Tarifas m y p 
TARIFA_MOVIMIENTO = 5
TARIFA_PARADO = 2

total_centimos = 0
estado_actual = "p"  
ejecutando = False   

def bienvenida():
    print(Fore.CYAN + "🚖 ¡Bienvenido al Taxímetro Digital! 😁")
    nombre = input(Fore.YELLOW + "Ingresa tu nombre: " + Fore.RESET).strip()
    print(Fore.GREEN + f"\nHola, {nombre}, en este taxímetro calcularemos tu tarifa en tiempo real. 😊")
    return nombre

def mostrar_menu():
    print(Fore.MAGENTA + "\nOpciones:")
    print(Fore.BLUE + "  [c]" + Fore.MAGENTA + " Comenzar un trayecto.")
    print(Fore.RED + "  [f]" + Fore.MAGENTA + " Finalizar el programa.")

def actualizar_tarifa():
    global total_centimos, estado_actual, ejecutando
    
    while ejecutando:
        time.sleep(1)
        # Aumentar tarifa por tipo estado
        tarifa = TARIFA_MOVIMIENTO if estado_actual == "m" else TARIFA_PARADO
        total_centimos += tarifa

        # Limpiar
        os.system('cls' if os.name == 'nt' else 'clear')

        # Mostrar tarifa
        total_euros = total_centimos / 100
        estado_texto = "🚗 Moviendo" if estado_actual == "m" else "⏳ Parado"
        print(
            Fore.YELLOW
            + "Pulsa 'm' para mover, 'p' para parar o 'f' para finalizar.\n"
            + f"💰 Tarifa actual: €{total_euros:.2f}  |  Estado: {estado_texto}"
        )

def calcular_tarifa():
    global total_centimos, estado_actual, ejecutando

    # Resetea
    total_centimos = 0
    estado_actual = "p"
    ejecutando = True

    hilo = threading.Thread(target=actualizar_tarifa, daemon=True)
    hilo.start()

    print(Fore.GREEN + "\n🚕 Trayecto iniciado. Presiona [f] para finalizar.\n")

    while True:
        accion = input().strip().lower()
        if accion == "f":
            ejecutando = False
            break
        elif accion in ["m", "p"]:
            estado_actual = accion
        else:
            print(Fore.RED + "⚠️ Comando no reconocido. Usa 'm', 'p' o 'f'.")

    # Esperar a hilo
    hilo.join()

    # Limpiar 
    os.system('cls' if os.name == 'nt' else 'clear')

    # Mostrar total final
    total_euros = total_centimos / 100
    print(Fore.GREEN + f"\n✅ Trayecto finalizado. Total a pagar: €{total_euros:.2f}")

def main():
    try:
        nombre = bienvenida()

        while True:
            mostrar_menu()
            opcion = input(Fore.YELLOW + "\n> " + Fore.RESET).strip().lower()

            if opcion == "c":
                calcular_tarifa()
            elif opcion == "f":
                print(Fore.CYAN + f"\n¡Gracias por usar el Taxímetro Digital, {nombre}! 👋")
                break
            else:
                print(Fore.RED + "⚠️ Opción no válida. Intenta de nuevo.")

    except KeyboardInterrupt:
        print(Fore.RED + "\n⚠️ Programa interrumpido. ¡Bye bye!")

if __name__ == "__main__":
    main()
