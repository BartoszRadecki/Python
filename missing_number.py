def missing_number(items: list[int]) -> int:
    items = sorted(items)
    dlugosc = len(items)
    min = items[0]
    max = items[-1]
    krok = (max - min)/dlugosc
    print(sorted(items))
    print(len(items))

    for n in range(len(items)-1):
        if sorted(items)[n+1] - sorted(items)[n] != krok:
            return sorted(items)[n] + krok

