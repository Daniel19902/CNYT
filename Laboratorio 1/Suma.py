
def complejo(a):
    a = a.split()
    real = int(a[0])
    imaginario = a[2]

    if a[1] == "-":
        imaginario = int(imaginario[:-1])*-1
    else:
        imaginario = int(imaginario[:-1])

    return [real, imaginario, a[1]]

def sumaComplejo(a , b):
    a = complejo(a)
    b = complejo(b)

    real = a[0] + b[0]
    imaginario = a[1] + b[1]

    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + " - " + str(b) + "i"

    return str(a) + " + " + str(b) + "i"



