def suma_avanzada():

    print("\n☆ •「Suma Avanzada」• ☆")
    print('          ── ☆  ──')
    print('Presione Enter para terminar')

    numeros = []
    while True:
        
        entrada = input("Ingrese un número: ")
        if entrada == "":
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
    resultado = sum(numeros)
    print(f"La suma es: {resultado}")