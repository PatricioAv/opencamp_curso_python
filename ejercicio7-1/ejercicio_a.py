from calculadora.calculadora import Calculadora


def main():
    calc = Calculadora()

    # Suma
    resultado = calc.sumar(2, 3)
    print("\nResultado suma 2 + 3 =", resultado)

    resultado = calc.sumar(2, 3, 5, 8)
    print("Resultado suma 2 + 3 + 5 + 8 =", resultado)


    # Resta
    resultado = calc.restar(7, 4)
    print("\nResultado resta  7 - 4 =", resultado)

    resultado = calc.restar(7, 4, 8, 2)
    print("Resultado resta  7 - 4 - 8 - 2 =", resultado)


    # Multiplicación
    resultado = calc.multiplicar(6, 8)
    print("\nResultado multiplicacion 6 * 8 =", resultado)

    resultado = calc.multiplicar(6, 8, 5)
    print("Resultado multiplicacion 6 * 8 * 5 =", resultado)


    # División
    resultado = calc.dividir(10, 3)
    print("\nResultado division 10 / 3 =", resultado)

    resultado = calc.dividir(10, 3, 3)
    print("Resultado division (10 / 3) / 3 =", resultado)

    resultado = calc.dividir(3, 0)
    print("Resultado division 3 / 0 =", resultado)

if __name__ == "__main__":
    main()
