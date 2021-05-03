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
    [r,b,d] = inputli()

    mini = min(r,b)
    maxi = max(r,b)

    if (1+d)*mini>=maxi :
        return 'YES'
    else:
        return 'NO'


t = inputi()


for i in range(t):

    ans = solve()
    
    print(ans,end='')
    print('') if i!=(t-1) else None
