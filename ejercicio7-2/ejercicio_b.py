from time import localtime

def diferencia_tiempo(hora_actual):
    """
    Retorna mensaje con cálculo de tiempo faltante para las 17 horas.
    """
    horas = 19 - hora_actual[0] - 1
    minutos = 59 - hora_actual[1]
    segundos = (59 - hora_actual[2]) + 1
    diferencia = "{:0>2d} horas, con {:0>2d} minutos".format(horas, minutos)
    diferencia += " y {:0>2d} segundos".format(segundos)
    return diferencia


def alerta_salida():
    """
    Imprime mensaje informando si es hora de irse a casa, o 
    el tiempo faltante para ello.
    """
    tiempo_actual = localtime()
    hora_actual = tiempo_actual[3], tiempo_actual[4], tiempo_actual[5]
    hora_pretty = "Siendo las {:0>2d}:{:0>2d}:{:0>2d}".format(hora_actual[0],
                                                       hora_actual[1],
                                                       hora_actual[2])
    mensaje = ''
    if hora_actual[0] < 19:
        faltan = diferencia_tiempo(hora_actual)
        mensaje = f"Faltan {faltan} aún para las 7 PM."
    else:
        mensaje = "Es hora de irte a casa."

    print(hora_pretty)
    print(mensaje)


if __name__ == "__main__":
    alerta_salida()
