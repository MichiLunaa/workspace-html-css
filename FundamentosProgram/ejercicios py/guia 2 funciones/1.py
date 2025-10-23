def ganador(c1, c2, c3, meta):
    if c1 >= meta and c2 < meta and c3 < meta:
        return 1
    elif c2 >= meta and c1 < meta and c3 < meta:
        return 2
    elif c3 >= meta and c1 < meta and c2 < meta:
        return 3
    elif (c1 >= meta and c2 >= meta) or (c1 >= meta and c3 >= meta) or (c2 >= meta and c3 >= meta):
        return 0
    else:
        return 0

resultado1 = ganador(2, 5, 3, 5)
print("El ganador es la alianza:", resultado1)

resultado2 = ganador(1, 3, 3, 5)
print("El ganador es la alianza:", resultado2)

