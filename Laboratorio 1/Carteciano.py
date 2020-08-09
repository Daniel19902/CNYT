import math



def carteacianoAPolar(a, b):

    p = round((a**2 + b**2)**(1/2))

    teta = round(math.atan(b/a))

    return "p = {} , angulo = {}".format(p,teta)

def polarACarteciano(a, b):

    x = round(a * math.cos(b))
    y = round(a * math.sin(b))

    return "{} + {}i".format(x, y)