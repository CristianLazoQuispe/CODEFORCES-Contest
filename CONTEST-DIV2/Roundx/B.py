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

import math

def solve():
    n = inputi()
    if n==1 or n%2==1:
        return "NO"

    #loga = math.floor(math.log2(n)) 
    raiz1 = math.floor(math.sqrt(n/2))
    raiz2 = math.floor(math.sqrt(n/4))
    if raiz1*raiz1 == (n/2) or raiz2*raiz2 == (n/4):
        return "YES"

    return "NO"


t = inputi()


for i in range(t):

    ans = solve()
    
    #print("Case #"+str(i+1)+':',print_list(ans),end='')
    print(ans,end='')
    print('') if i!=(t-1) else None
