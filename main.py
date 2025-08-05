from sumar import suma
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada


while True:
    print("\n☆ •「Calculadora」• ☆")
    print('      ── ☆  ──')
    print("Seleccione una opción:")
    print("[S]  ▷  Sumar")
    print("[R]  ▷  Restar")
    print("[M]  ▷  Multiplicar")
    print("[D]  ▷  Dividir")
    print("[A]  ▷  Suma Avanzada")
    print("[Q]  ▷  Salir")
    opcion = input("\n¿Qué operación deseas realizar? ").upper()
    if opcion == "Q":
        print("¡Hasta luego!")
        break
    elif opcion == "A":
        suma_avanzada()
    else: 
        operaciones = {
            "S": suma,
            "R": resta,
            "M": multiplicar,
            "D": dividir
        }
        if opcion in operaciones:

            titulo = f"\n☆ •「{operaciones[opcion].__name__.capitalize()}」• ☆"
            print(titulo)
            ancho = len(titulo.strip())
            linea = '── ☆  ──'
            print(linea.center(ancho))

            try:
                a, b = input("Ingrese dos números separados por un espacio: ").split()
                a, b = float(a), float(b)
                resultado = operaciones[opcion](a, b)
                print(f"Resultado: {resultado}")

            except ValueError:
                print("Por favor, ingrese dos números válidos separados por un espacio.")