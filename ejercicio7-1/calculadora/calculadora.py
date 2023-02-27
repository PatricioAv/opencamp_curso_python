class Calculadora:
    """
    Clase calculadora con metodos Suma, Resta, Multiplicación y División.
    Validación de entradas pendiente
    """

    def sumar(self, *args):
        """
        Retorna el resultado de la suma de los argumentos
        """
        sumatoria: int = 0
        for arg in args:
            sumatoria += arg
        return sumatoria


    def restar(self, *args):
        """
        Retorna el resultado de la sustracción al primer número pasado como
        argumento, del segúndo nro. argumento. Retorna el resultado de la sustracción
        para el resultado anterior respecto del proximo argumento.
        """
        sustraccion: int = 0
        for ind, arg in enumerate(args):
            if ind == 0:
                sustraccion = arg
            else:
                sustraccion -= arg
        return sustraccion


    def multiplicar(self, *args):
        """
        Retorna el resultado de la Multiplicación de los argumentos
        """
        multiplicacion: int = 1
        for arg in args:
            multiplicacion *= arg
        return multiplicacion


    def dividir(self, *args):
        """
        Retorna el resultado del la división del primer número por el segundo.
        Para cada argumento siguente, calcula la división del resultado 
        anterior por el próximo argumento.
        """
        division: float = 0.0
        try:
            for ind, arg in enumerate(args):
                if ind == 0:
                    division = arg
                else:
                    division /= arg
            return division
        except Exception as Ex:
            return 'Error: ' + str(Ex)
