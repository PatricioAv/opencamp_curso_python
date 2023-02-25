peso_kg = input("Ingresa tu peso en kilogramos: ")
estatura = input("Ingresa tu estatura en metros: ")

peso_kg = int(peso_kg)
estatura = float(estatura)

imc = peso_kg / (estatura ** 2)
imc = '{:.2f}'.format(imc)

print(f'Tu índice de masa corporal es: {imc}')
