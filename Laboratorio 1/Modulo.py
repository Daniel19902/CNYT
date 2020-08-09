

def complejo(a):
    a = a.split()
    real = int(a[0])
    imaginario = a[2]

    if a[1] == "-":
        imaginario = int(imaginario[:-1])*-1
    else:
        imaginario = int(imaginario[:-1])

    return [real, imaginario]


def modulo(a):
    a = complejo(a)
    print(a[0],a[1])
    modulo = round((a[0]**2 + a[1]**2)**(1/2), 2)

    return modulo