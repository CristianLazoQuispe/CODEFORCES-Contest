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
    [n,m] = inputli()
    aux = []
    ans = [[] for i in range(n)]   
    for i in range(n):
        b = inputli()
        b = sorted(b)
        aux.append(b)

    #indices = [i for i in range(n)]
    #minis,indices = zip(*sorted(zip(minis, indices)))

    for i in range(m):
        #print(aux)
        minis = [aux[j][0] for j in range(n)]
        mini = min(minis)
        idx = minis.index(mini)      
        ans[idx].append(mini)
        aux[idx].pop(0)
        for j in range(n):
            if idx!=j:
                ans[j].append(aux[j].pop())

    for i in range(n):
        print(print_list(ans[i]))
    return 0

t = inputi()


for i in range(t):
    
    solve()
