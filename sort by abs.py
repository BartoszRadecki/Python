def checkio(values: list) -> list:

    print(sorted(values,key=abs))



    return sorted(values,key=abs)


print("Example:")
print(checkio([-20, -5, 10, 15]))

assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")
