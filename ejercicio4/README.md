Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

Ejercicio:

[./ejercicio4.py](./ejercicio4.py)

```py
lista_num = [num for num in range(1,101)]
lista_num.reverse()

for numero in lista_num:
    print(numero)
```
