class Vehiculo:

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
