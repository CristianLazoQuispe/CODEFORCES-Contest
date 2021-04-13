import functools,operator

T = int(input())

def solve(lista):
    ida = []
    vuelta = []
    maxi = len(lista)

    back = None
    for i in range(len(lista)):
        if back is None:
            value = functools.reduce(operator.and_, [lista[i]])
            ida.append(value)
            back = value
        else:
            value = functools.reduce(operator.and_, [value,lista[i]])
            ida.append(value)
            back = value
    back = None
    for i in range(len(lista)):
        i = maxi-i-1
        if back is None:
            value = functools.reduce(operator.and_, [lista[i]])
            vuelta.append(value)
            back = value
        else:
            value = functools.reduce(operator.and_, [value,lista[i]])
            vuelta.append(value)
            back = value
    suma = 0
    for idx,ida_i in enumerate(ida):
        if vuelta[maxi-idx-1] == ida_i:
            suma+=1
            print(idx,ida_i)
    return suma


for i in range(T):
    n = int(input())
    lista = list(map(int,input().split()))
    ans = solve(lista)
    print(ans)
