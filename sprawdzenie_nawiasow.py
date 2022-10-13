def checkio(expression: str) -> bool:
    brackets = {'(': ')', '[': ']', '{': '}'}
    new = ['']
    for i in expression:
        if i in brackets:
            new.append(brackets[i])
            print(new)
        elif i in brackets.values() and i != new.pop():
            return False
    return new == ['']


# These "asserts" using only for self-checking and not necessary for auto-testing

print("Example:")
print(checkio("((5+3)*2+1)"))

assert checkio("((5+3)*2+1)") == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("[(3)+(-1)]*{3}") == True
assert checkio("(((([[[{{{3}}}]]]]))))") == False
assert checkio("[1+202]*3*({4+3)}") == False
assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True
assert checkio("[[[1+[1+1]]])") == False
assert checkio("(((1+(1+1))))]") == False
assert checkio("2+3") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")