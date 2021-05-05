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
    n = inputi()
    if n<10:
        return n
    size = len(str(n))
    ref = int(str(n)[0])
    if int(n)<int(size*str(n)[0]):
        ref-=1
    
    return ref+(size-1)*9
    

t = inputi()


for i in range(t):

    ans = solve()
    
    #print(print_list(ans),end='')
    print(ans,end='')
    print('') if i!=(t-1) else None
