from functools import reduce

def suma_impares(lista):
    """
    Función recibe una lista de números, filtra los impares
    y retorna el resultado de la suma de estos.
    """
    lista_impares = list(filter(lambda x: x % 2, lista))
    sumatoria = reduce(lambda a,b: a + b, lista_impares)
    return sumatoria


def main():
    lista_nums = [x for x in range(1, 101)]
    resultado = suma_impares(lista_nums)
    print(resultado)


if __name__ == "__main__":
    main()
