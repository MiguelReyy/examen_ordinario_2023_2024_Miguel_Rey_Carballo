
class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

Concordia = Planeta("Concordia", 500, 1)
Ilum = Planeta("Ilum", 1200, 2)
Kamino = Planeta("Kamino", 800, 3)

class EstrellaDeLaMuerte:
    def __init__(self, vida):
        self.vida = vida

    def destruir_planeta(self, planeta):
        if planeta.volumen <= self.vida:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.vida -= planeta.volumen
            print(f"Puntos de vida restantes en la Estrella de la Muerte: {self.vida}")
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}. La clasificación es mayor que los puntos de vida de la Estrella de la Muerte.")

# Crear una instancia de EstrellaDeLaMuerte
estrella_muerte = EstrellaDeLaMuerte(1000)

# Pedir al usuario que elija un planeta
print("Elige un planeta para comprobar si puede ser destruido:")
print("1. Concordia")
print("2. Ilum")
print("3. Kamino")
opcion = int(input())

# Validar la opción del usuario y destruir el planeta correspondiente
if opcion == 1:
    estrella_muerte.destruir_planeta(Concordia)
elif opcion == 2:
    estrella_muerte.destruir_planeta(Ilum)
elif opcion == 3:
    estrella_muerte.destruir_planeta(Kamino)
else:
    print("Opción no válida. Inténtalo de nuevo con una opción válida.")
