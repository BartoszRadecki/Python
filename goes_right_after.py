def checkio(values: list) -> list:
    i = word.find(first)
    j = word.find(second)

    return i >= 0 and j == i + 1






print("Example:")
print(goes_after("world", "w", "o"))

assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
