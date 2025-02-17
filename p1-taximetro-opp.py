import os
import time
import threading
from colorama import init, Fore
import logging

# Configuración del logger
logging.basicConfig(
    filename='p1-taximetro.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

init(autoreset=True)

class Taximetro:
    TARIFA_MOVIMIENTO = 5
    TARIFA_PARADO = 2

    def __init__(self):
        self.total_centimos = 0
        self.estado_actual = "p"  # "m" = moviendo, "p" = parado
        self.ejecutando = False
        self.hilo = None
        logging.info("🚖 Taxímetro iniciado.")

    def iniciar_trayecto(self):
        self.total_centimos = 0
        self.estado_actual = "p"
        self.ejecutando = True
        self.hilo = threading.Thread(target=self.actualizar_tarifa, daemon=True)
        self.hilo.start()
        print(Fore.GREEN + "\n🚕 Trayecto iniciado. Presiona [f] para finalizar.\n")
        logging.info("🟢 Inicio de trayecto.")

    def actualizar_tarifa(self):
        while self.ejecutando:
            time.sleep(1)
            tarifa = self.TARIFA_MOVIMIENTO if self.estado_actual == "m" else self.TARIFA_PARADO
            self.total_centimos += tarifa

            os.system('cls' if os.name == 'nt' else 'clear')
            estado_texto = "🚗 Moviendo" if self.estado_actual == "m" else "⏳ Parado"
            print(Fore.YELLOW + "Pulsa 'm' para mover, 'p' para parar o 'f' para finalizar.")
            print(f"💰 Tarifa actual: €{self.total_centimos / 100:.2f}  |  Estado: {estado_texto}")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["m", "p"]:
            self.estado_actual = nuevo_estado
        else:
            print(Fore.RED + "⚠️ Comando no reconocido. Usa 'm', 'p' o 'f'.")
        logging.info(f"🔄 Cambio de estado: {nuevo_estado}")

    def finalizar_trayecto(self):
        self.ejecutando = False
        if self.hilo:
            self.hilo.join()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + f"\n✅ Trayecto finalizado. Total a pagar: €{self.total_centimos / 100:.2f}")
        logging.info(f"✅ Trayecto finalizado. Total: {self.total_centimos / 100:.2f}€")
        
class App:
    def __init__(self):
        self.taximetro = Taximetro()
        self.nombre = ""

    def bienvenida(self):
        print(Fore.CYAN + "🚖 ¡Bienvenido al Taxímetro Digital! 😁")
        self.nombre = input(Fore.YELLOW + "Ingresa tu nombre: " + Fore.RESET).strip()
        print(Fore.GREEN + f"\nHola, {self.nombre}, en este taxímetro calcularemos tu tarifa en tiempo real. 😊")

    def mostrar_menu(self):
        print(Fore.MAGENTA + "\nOpciones:")
        print(Fore.BLUE + "  [c]" + Fore.MAGENTA + " Comenzar un trayecto.")
        print(Fore.RED + "  [f]" + Fore.MAGENTA + " Finalizar el programa.")

    def ejecutar(self):
        try:
            self.bienvenida()
            while True:
                self.mostrar_menu()
                opcion = input(Fore.YELLOW + "\n> " + Fore.RESET).strip().lower()

                if opcion == "c":
                    self.taximetro.iniciar_trayecto()
                    while True:
                        accion = input().strip().lower()
                        if accion == "f":
                            self.taximetro.finalizar_trayecto()
                            break
                        else:
                            self.taximetro.cambiar_estado(accion)

                elif opcion == "f":
                    print(Fore.CYAN + f"\n¡Gracias por usar el Taxímetro Digital, {self.nombre}! 👋")
                    break
                else:
                    print(Fore.RED + "⚠️ Opción no válida. Intenta de nuevo.")

        except KeyboardInterrupt:
            print(Fore.RED + "\n⚠️ Programa interrumpido. ¡Bye bye!")

if __name__ == "__main__":
    app = App()
    app.ejecutar()
