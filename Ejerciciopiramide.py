def generar_piramide(n):
    for i in range(1, n + 1, 2):
        espacios = (n - i) // 2
        print(" " * espacios + "*" * i + " " * espacios)

def main():
    try:
        n = int(input("Ingrese un número entero mayor o igual a 1: "))
        if n < 1:
            raise ValueError("El número debe ser mayor o igual a 1.")
        
        generar_piramide(n)

    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
