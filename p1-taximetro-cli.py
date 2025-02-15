import time  
from colorama import init, Fore  

# Inicializar colorama
init(autoreset=True)

# Tarifas en céntimos por segundo
TARIFA_MOVIMIENTO = 5
TARIFA_PARADO = 2

def bienvenida():
    print(Fore.CYAN + "🚖 ¡Bienvenido al Taxímetro Digital! 😁")
    nombre = input(Fore.YELLOW + "Ingresa tu nombre: " + Fore.RESET).strip()
    print(Fore.GREEN + f"\nHola, {nombre}, en este taxímetro podremos calcular tu tarifa. 😊")
    return nombre

def mostrar_menu():
    print(Fore.MAGENTA + "\nOpciones:")
    print(Fore.BLUE + "  [c]" + Fore.MAGENTA + " Comenzar un trayecto.")
    print(Fore.RED + "  [f]" + Fore.MAGENTA + " Finalizar el programa.")

def calcular_tarifa():
    print(Fore.GREEN + "\n🚕 Trayecto iniciado. Presiona " + Fore.RED + "[f]" + Fore.GREEN + " para finalizar.")
    
    estado_actual = None
    while estado_actual not in ["m", "p"]:
        estado_actual = input(Fore.YELLOW + "¿El taxi está en movimiento (m) o parado (p)? " + Fore.RESET).strip().lower()
        if estado_actual not in ["m", "p"]:
            print(Fore.RED + "⚠️ Estado no válido. Usa 'm' (movimiento) o 'p' (parado).")

    tiempo_inicio = time.time()
    total_centimos = 0

    while True:
        accion = input(Fore.YELLOW + "Cambia el estado (m/p) o finaliza (f): " + Fore.RESET).strip().lower()

        if accion == "f":
            break
        elif accion not in ["m", "p"]:
            print(Fore.RED + "⚠️ Comando no reconocido. Usa 'm', 'p' o 'f'.")
            continue
        elif accion == estado_actual:
            print(Fore.RED + f"⚠️ El taxi ya está {'en movimiento' if accion == 'm' else 'parado'}.")
            continue

        # Calcular tarifa acumulada desde el último cambio de estado
        duracion = time.time() - tiempo_inicio
        tarifa = duracion * (TARIFA_MOVIMIENTO if estado_actual == "m" else TARIFA_PARADO)
        total_centimos += tarifa

        # Actualizar estado y tiempo
        estado_actual = accion
        tiempo_inicio = time.time()

    # Calcular tarifa final antes de salir
    duracion_final = time.time() - tiempo_inicio
    tarifa_final = duracion_final * (TARIFA_MOVIMIENTO if estado_actual == "m" else TARIFA_PARADO)
    total_centimos += tarifa_final

    # Convertir a euros y mostrar total
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
        print(Fore.RED + "\n⚠️ Programa interrumpido por el usuario. ¡Hasta luego!")

if __name__ == "__main__":
    main()
