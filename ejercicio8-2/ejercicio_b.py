import pickle

class Vehiculo:

    def __init__(self, marca, color, puertas):
        self.marca = marca
        self.color = color
        self.puertas = puertas

    def __str__(self) -> str:
        repres = f'Marca: {self.marca}, '
        repres += f'Color: {self.color}, '
        repres += f'Puertas: {self.puertas}'
        return repres


def main():

    def guardar_vehiculo(vehiculo):
        "Guarda objeto 'vehiculo' como archivo binario"
        with open('./vehiculo.dat', 'wb') as file:
            pickle.dump(vehiculo, file)

    def cargar_vehiculo(archivo):
        "Retorna objeto cargado de 'archivo' binario"
        with open(archivo, 'rb') as file:
            vehiculo_guardado = pickle.load(file)
        return vehiculo_guardado

    # Creación de instancia de objeto Vehiculo()
    vehiculo_a = Vehiculo('PepeCar', 'Verde', 3)
    guardar_vehiculo(vehiculo_a)
    
    # Eliminación de objeto vehiculo_a
    del vehiculo_a

    # Nuevo objeto vehiculo_a cargado desde archivo
    vehiculo_a = cargar_vehiculo('./vehiculo.dat')
    print(vehiculo_a)

if __name__ == '__main__':
    main()
