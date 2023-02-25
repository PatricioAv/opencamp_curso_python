class Alumno:
    """
    Clase alumno requiere 'nombre' y 'nota' para inicializar
    """

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def aprobado(self):
        """
        Retorna mensaje indicando si alumno aprueba o no según 'nota'
        """
        if self.nota >=  6.0:
            print('Aprueba con nota:', self.nota)
        else:
            print('Reprueba con nota:', self.nota)

    def __repr__(self):
        return "\nAlumno: {} - Nota: {}".format(self.nombre, self.nota)


# Instancias de clase alumno
alumno1 = Alumno("Zerafin", 3.2)
alumno2 = Alumno("Alipio", 6.0)
alumno3 = Alumno("Roberta", 7.0)

# Representación de clase alumno y estado de aprobación
print(alumno1.__repr__())
alumno1.aprobado()

print(alumno2.__repr__())
alumno2.aprobado()

print(alumno3.__repr__())
alumno3.aprobado()
