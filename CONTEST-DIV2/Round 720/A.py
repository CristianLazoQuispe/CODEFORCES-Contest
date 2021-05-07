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

    [a,b] = inputli()

    if b==1:
        print('NO',end='')
        return 
    
    maxi = b*2
    for p in range(maxi-1,2,-1):
        r = maxi-p
        if r%b !=0 and p!=r:
            print('YES')
            print(a*p,a*r,a*maxi,end='')
            return
    print('NO',end='')
    return 
    
t = inputi()


for i in range(t):

    ans = solve()
    
    #print(print_list(ans),end='')
    #print(ans,end='')
    print('') if i!=(t-1) else None
