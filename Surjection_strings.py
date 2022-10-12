def isometric_strings(a: str, b: str) -> bool:
    dic = {}
    for index,n in enumerate(a):
        dic[n] = dic.get(n,set()).union(set(b[index]))
        print(index,n)
        print(dic)
        if len(dic[n]) > 1:
            return False
    return True