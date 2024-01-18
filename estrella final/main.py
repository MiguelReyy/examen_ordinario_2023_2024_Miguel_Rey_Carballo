
from EstrellaDeLaMuerte import EstrellaDeLaMuerte
from Naves import NavePequena, NaveGrande

class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

# Crear instancias de planeta
Concordia = Planeta("Concordia", 500, 1)
Ilum = Planeta("Ilum", 1200, 2)
Kamino = Planeta("Kamino", 800, 3)

# Crear instancias de EstrellaDeLaMuerte, NavePequena y NaveGrande
estrella_muerte = EstrellaDeLaMuerte(1000)
nave_pequena = NavePequena("X-Wing", 200)
nave_grande = NaveGrande("Star Destroyer", 800)

# Atacar planeta
estrella_muerte.destruir_planeta(Ilum)

# Agregar naves aliadas
estrella_muerte.agregar_nave_aliada(nave_pequena)
estrella_muerte.agregar_nave_aliada(nave_grande)

# Atacar naves aliadas
estrella_muerte.atacar_nave_aliada(nave_pequena)
estrella_muerte.atacar_nave_aliada(nave_grande)
