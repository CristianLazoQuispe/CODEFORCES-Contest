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

moves = [[0,1],[1,0]]


def solve2(x,y,n,m,k,cost):
    if x==n and y ==m:
        return [cost ==k]

    ans = []
    for [dx,dy] in moves:
        x_new = x+dx
        y_new = y+dy
        if x_new<=n and y_new<=m:
            if dy==1:
                ans += solve2(x_new,y_new,n,m,k,cost+x_new+1)
            else:
                ans += solve2(x_new,y_new,n,m,k,cost+y_new+1)
    return ans



def solve():
    [n,m,k] = inputli()
    result = solve2(0,0,n-1,m-1,k,0)
    ans = False
    for i in result:
        if i==True:
            ans=True
            break
    if ans:
        return 'YES'
    else:
        return 'NO'


t = inputi()


for i in range(t):

    ans = solve()
    
    print(ans,end='')
    print('') if i!=(t-1) else None
