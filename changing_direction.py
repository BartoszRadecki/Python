def changing_direction(elements: list) -> int:

    lista = list()

    for n in range(len(elements)-1):
        print(n)
        if elements[n+1] < elements[n]:
            if not lista or lista[-1] == "up":
                lista.append("down")
        elif elements[n+1] > elements[n]:
            if not lista or lista[-1] == "down":
                lista.append("up")


    return len(lista)-1