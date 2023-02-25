Escribe una función que pueda decirte si un año (número entero) es bisiesto o no

> Cuando comiences el ejercicio se te mostrarán las especificaciones para la
> realización y entrega del mismo.
> La entrega del ejercicio deberá realizarse a través de una carpeta .zip
> empaquetada o un enlace al repositorio del ejercicio en GitHub.

Ejercicio:

[./ejercicio5.py](./ejercicio5.py)

```py
def es_bisiesto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'El año {ano} es bisiesto')
    else:
        print(f'El año {ano} no es bisiesto')
```
