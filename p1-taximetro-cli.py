import time  
from colorama import init, Fore  

# Colorama
init(autoreset=True)

# Función principal de bienvenida
def main():
    print(Fore.CYAN + "🚖 ¡Bienvenido al Taxímetro Digital! 🚖")
    nombre = input(Fore.YELLOW + "Ingresa tu nombre: " + Fore.RESET)
    print(Fore.GREEN + f"\nHola, {nombre}, en este taxímetro podremos calcular tu tarifa. 😊")

    while True:
        print(Fore.MAGENTA + "\nPresiona " + Fore.BLUE + "c" + Fore.MAGENTA + " para comenzar un trayecto.")
        print(Fore.MAGENTA + "Presiona " + Fore.RED + "f" + Fore.MAGENTA + " para finalizar el programa.")
        opcion = input(Fore.YELLOW + "\n> " + Fore.RESET).strip().lower()

        if opcion == "c":
            calcular_tarifa()
        elif opcion == "f":
            print(Fore.CYAN + f"\n¡Gracias por usar el Taxímetro Digital! {nombre} ¡Hasta luego! 👋")
            break
        else:
            print(Fore.RED + "⚠️ Opción no válida. Intenta de nuevo.")

# Función para calcular la tarifa
def calcular_tarifa():
    print(Fore.GREEN + "\n🚕 Trayecto iniciado. Presiona " + Fore.RED + "f" + Fore.GREEN + " para finalizar.")
    estado_actual = None
    tiempo_inicio = time.time()
    total_centimos = 0

    while estado_actual not in ["m", "p"]:
        estado_actual = input(Fore.YELLOW + "¿El taxi está en movimiento (m) o parado (p)? " + Fore.RESET).strip().lower()
        if estado_actual not in ["m", "p"]:
            print(Fore.RED + "⚠️ Estado no válido. Usa 'm' o 'p'.")

    while True:
        accion = input(Fore.YELLOW + "Cambia el estado (m/p) o finaliza (f): " + Fore.RESET).strip().lower()

        if accion == "f":
            break
        elif accion in ["m", "p"]:
            if accion == estado_actual:
                print(Fore.RED + f"⚠️ El taxi ya está {'en movimiento' if accion == 'm' else 'parado'}.")
                continue
            # Calcular tarifa acumulada
            tiempo_actual = time.time()
            duracion = tiempo_actual - tiempo_inicio
            tarifa = duracion * (5 if estado_actual == "m" else 2)
            total_centimos += tarifa
            # Actualizar estado y tiempo
            estado_actual = accion
            tiempo_inicio = tiempo_actual
        else:
            print(Fore.RED + "⚠️ Comando no reconocido.")

    # Calcular tarifa final
    tiempo_final = time.time()
    duracion_final = tiempo_final - tiempo_inicio
    tarifa_final = duracion_final * (5 if estado_actual == "m" else 2)
    total_centimos += tarifa_final

    # Mostrar total en euros
    total_euros = total_centimos / 100
    print(Fore.GREEN + f"\n✅ Trayecto finalizado. Total a pagar: €{total_euros:.2f}")

# Ejecutar el taximetro
if __name__ == "__main__":
    main()