def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))


def print_list(lista):
    s=""
    for i in lista[:-1]:
        s+=str(i)+" "
    s+=str(lista[-1])
    return s


def solve():
    [n,m,x] = inputli()
    heights = inputli()
    
    suma = sum(heights)
    heights = sorted(heights)
    mean = int(suma/m)
    aux = 0
    idx = 1
    ans = []
    band = True
    back = None
    for i,h in enumerate(heights):
        aux+=h
        ans.append(idx)
        if not back is None:
            if abs(back-aux)>x:
                return False,[]
        if aux>= mean and h!=heights[-1] or (m-i-1)>(x-idx):
            idx+=1
            back = aux
            aux=0
    #print(idx,ans)
    if idx!=m:
        return False,None
    return band,ans


t = inputi()


for i in range(t):

    band,ans = solve()
    if band:
        print("YES")
        print(print_list(ans),end='')
        print('') if i!=(t-1) else None
    else:
        print("NO")