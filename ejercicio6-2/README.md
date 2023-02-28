En este segundo ejercicio, tendréis que crear un programa que tenga una clase
llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir
los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con
el resultado de la nota y si ha aprobado o no.

Ejercicio:

[./ejercicio6-2.py](./ejercicio6-2.py)

```py

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
print(alumno1)
alumno1.aprobado()

print(alumno2)
alumno2.aprobado()

print(alumno3)
alumno3.aprobado()
```

```txt
Alumno: Zerafin - Nota: 3.2
Reprueba con nota: 3.2

Alumno: Alipio - Nota: 6.0
Aprueba con nota: 6.0

Alumno: Roberta - Nota: 7.0
Aprueba con nota: 7.0
```
