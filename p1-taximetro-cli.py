import os
import time
import threading
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Tarifas en céntimos por segundo
TARIFA_MOVIMIENTO = 5
TARIFA_PARADO = 2

# Variables globales para el hilo de conteo
total_centimos = 0
estado_actual = "p"  # Empieza detenido
ejecutando = False   # Control del hilo

def bienvenida():
    """Muestra un saludo y obtiene el nombre del usuario."""
    print(Fore.CYAN + "🚖 ¡Bienvenido al Taxímetro Digital! 😁")
    nombre = input(Fore.YELLOW + "Ingresa tu nombre: " + Fore.RESET).strip()
    print(Fore.GREEN + f"\nHola, {nombre}, en este taxímetro calcularemos tu tarifa en tiempo real. 😊")
    return nombre

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print(Fore.MAGENTA + "\nOpciones:")
    print(Fore.BLUE + "  [c]" + Fore.MAGENTA + " Comenzar un trayecto.")
    print(Fore.RED + "  [f]" + Fore.MAGENTA + " Finalizar el programa.")

def actualizar_tarifa():
    """
    Hilo que se encarga de:
    - Limpiar la pantalla en cada iteración.
    - Mostrar la tarifa en tiempo real y el estado actual.
    - Repetir cada segundo mientras 'ejecutando' sea True.
    """
    global total_centimos, estado_actual, ejecutando
    
    while ejecutando:
        time.sleep(1)
        # Aumentar tarifa en función del estado
        tarifa = TARIFA_MOVIMIENTO if estado_actual == "m" else TARIFA_PARADO
        total_centimos += tarifa

        # Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

        # Mostrar información en una sola línea
        total_euros = total_centimos / 100
        estado_texto = "🚗 Moviendo" if estado_actual == "m" else "⏳ Parado"
        print(
            Fore.YELLOW
            + "Pulsa 'm' para mover, 'p' para parar o 'f' para finalizar.\n"
            + f"💰 Tarifa actual: €{total_euros:.2f}  |  Estado: {estado_texto}"
        )

def calcular_tarifa():
    """
    Inicia el conteo en segundo plano (hilo),
    espera a que el usuario cambie de estado o finalice,
    y al finalizar limpia la pantalla y muestra el total.
    """
    global total_centimos, estado_actual, ejecutando

    # Resetear valores
    total_centimos = 0
    estado_actual = "p"
    ejecutando = True

    # Iniciar hilo
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

    # Esperar a que el hilo termine
    hilo.join()

    # Limpiar la pantalla para no dejar restos
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
        print(Fore.RED + "\n⚠️ Programa interrumpido. ¡Hasta luego!")

if __name__ == "__main__":
    main()
