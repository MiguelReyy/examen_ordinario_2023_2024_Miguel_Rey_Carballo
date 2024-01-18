# Crear un archivo llamado tiempo_partidas.py

# Definir las variables tiempo_carlsen y tiempo_nakamura
tiempo_carlsen = 180  # 3 minutos en segundos
tiempo_nakamura = 180  # 3 minutos en segundos

# Definir el número total de turnos
num_turnos = 10

# Bucle para simular los turnos
for turno in range(1, num_turnos + 1):
    # Es el turno de Carlsen
    jugador_actual = input(f"Turno {turno}: Ingresa 'carlsen' para el turno de Carlsen (o 'Salir' para terminar): ").lower()

    while jugador_actual != 'carlsen' and jugador_actual != 'salir':
        print("Nombre incorrecto. Debes ingresar 'carlsen' para el turno de Carlsen (o 'Salir' para terminar).")
        jugador_actual = input(f"Turno {turno}: Ingresa 'carlsen' para el turno de Carlsen (o 'Salir' para terminar): ").lower()

    if jugador_actual == 'salir':
        print("Partida terminada. ¡Hasta luego!")
        break

    print("Es el turno de Carlsen.")
    
    # Verificar si el tiempo de Carlsen es menor o igual a 100 segundos
    if tiempo_carlsen <= 100:
        print("¡Cambio a 5 segundos por movimiento para Carlsen!")
        tiempo_carlsen -= 5
    else:
        tiempo_carlsen -= 10  # Restar 10 segundos al tiempo de Carlsen

    print(f"Tiempo restante de Carlsen: {tiempo_carlsen} segundos")

    if tiempo_carlsen <= 0:
        print("¡Carlsen se ha quedado sin tiempo! Nakamura gana.")
        break

    # Es el turno de Nakamura
    jugador_actual = input(f"Turno {turno}: Ingresa 'nakamura' para el turno de Nakamura (o 'Salir' para terminar): ").lower()

    while jugador_actual != 'nakamura' and jugador_actual != 'salir':
        print("Nombre incorrecto. Debes ingresar 'nakamura' para el turno de Nakamura (o 'Salir' para terminar).")
        jugador_actual = input(f"Turno {turno}: Ingresa 'nakamura' para el turno de Nakamura (o 'Salir' para terminar): ").lower()

    if jugador_actual == 'salir':
        print("Partida terminada. ¡Hasta luego!")
        break

    print("Es el turno de Nakamura.")

    # Verificar si el tiempo de Nakamura es menor o igual a 100 segundos
    if tiempo_nakamura <= 100:
        print("¡Cambio a 5 segundos por movimiento para Nakamura!")
        tiempo_nakamura -= 5
    else:
        tiempo_nakamura -= 10  # Restar 10 segundos al tiempo de Nakamura

    print(f"Tiempo restante de Nakamura: {tiempo_nakamura} segundos")

    if tiempo_nakamura <= 0:
        print("¡Nakamura se ha quedado sin tiempo! Carlsen gana.")
        break

# Imprimir los tiempos finales
print("Tiempo final de Carlsen:", tiempo_carlsen, "segundos")
print("Tiempo final de Nakamura:", tiempo_nakamura, "segundos")
