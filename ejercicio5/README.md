Escribe una función que pueda decirte si un año (número entero) es bisiesto o no

Ejercicio:

[./ejercicio5.py](./ejercicio5.py)

```py
def es_bisiesto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'El año {ano} es bisiesto')
    else:
        print(f'El año {ano} no es bisiesto')
```
