
def complejo(a):
    a = a.split()
    imaginario = a[2]
    real = int(a[0])
    if a[1] == "-":
        imaginario = int(imaginario[0])*-1
    else:
        imaginario = int(imaginario[0])
    return real, imaginario


def resta (a, b):

    r, i = complejo(a)
    r1, i1 = complejo(b)
    r1 = r1 * -1
    i1 = i1 * -1

    real = r + r1
    imaginario = i + i1

    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + " - " + str(b) + "i"

    return str(a) + " + " + str(b) + "i"