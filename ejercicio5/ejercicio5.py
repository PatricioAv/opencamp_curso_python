def es_bisiesto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'El año {ano} es bisiesto')
    else:
        print(f'El año {ano} no es bisiesto')


for ano in range(1900, 2100):
    es_bisiesto(ano)
