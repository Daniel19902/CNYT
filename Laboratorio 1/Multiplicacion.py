

def multiply(c, c1):

    c = [int(x) for x in c.split(",")]
    c1 = [int(x) for x in c1.split(",")]
    real = c[0] * c1[0] - c[1] * c1[1]
    imaginario = c[0] * c1[1] + c[1] * c1[0]

    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + " - " + str(b) + "i"

    return str(a) + " + " + str(b) + "i"
