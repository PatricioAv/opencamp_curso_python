En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes
atributos:

- Color
- Ruedas
- Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá
los siguientes atributos:

- Velocidad
- Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

Ejercicio:

[./ejercicio6-1.py](./ejercicio6-1.py)

```py
class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __repr__(self) -> str:
        repres = f'Color: {self.color}, '
        repres += f'Ruedas: {self.ruedas}, '
        repres += f'Puertas: {self.puertas}'
        return repres


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0.0
    
    def __init__(self, color, velocidad, cilindrada, ruedas=4, puertas=5):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __repr__(self) -> str:
        repres = f'Coche -> {super().__repr__()}, '
        repres += f'velocidad: {self.velocidad}, '
        repres += f'cilindrada {self.cilindrada} '
        return repres


coche1 = Coche('verde', '180', '1.5')
print(coche1)
```

```py
Coche -> Color: verde, Ruedas: 4, Puertas: 5, velocidad: 180, cilindrada 1.5
```
