
import Suma
import Multiplicacion
import Resta
import Division
import Modulo


def complejo(a):
    a = a.split()
    real = int(a[0])
    imaginario = a[2]

    if a[1] == "-":
        imaginario = int(imaginario[:-1])*-1
    else:
        imaginario = int(imaginario[:-1])

    return [real, imaginario, a[1]]


def conjugado(a):

    a = a.split()
    if a[1] == '-':
        return str(a[0])+" + "+str(a[2])
    return str(a[0]) + " - " + str(a[2])

def conjugadoSuma(a, b):

    resultado = Suma.sumaComplejo(a, b)
    return conjugado(resultado)

def conjugadoMultiplicacion(a, b):

    resultado = Multiplicacion.multiply(a, b)
    return conjugado(resultado)

def conjugadoModulo(a):

    resultado = Modulo.modulo(a)
    return conjugado(resultado)