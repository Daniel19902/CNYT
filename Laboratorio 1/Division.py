

def divicion(a, b):
    a = [int(x) for x in a.split(",")]
    b = [int(x) for x in b.split(",")]

    f = a[1]**2 + b[1]**2
    s = a[0] * a[1] + b[0] * b[1]
    t = a[1] * b[0] - a[0] * b[1]

    real = (s / f)
    imaginario = (t / f)
    print(real)
    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + " - " + str(b) + "i"

    return str(a) + " + " + str(b) + "i"