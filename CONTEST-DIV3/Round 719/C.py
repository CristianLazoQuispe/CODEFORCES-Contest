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
    if n==1:
        return False,1
    if n==2:
        return False,-1

    matriz = [[0]*(n+2) for i in range(n+2)]            

    if n==2:
        matriz[1][1] =1 
        matriz[1][2] =4 
        matriz[2][2] =6 
        matriz[2][1] =8 
        return True,matriz


    for i in range(1,n+1):
        matriz[i][i]= i
    
    numbers = [i for i in range(n+1,n**2+1)]
    for k in range(1,n+1):
        for j in range(1,k):
            matriz[k][j]=numbers.pop(0)
            matriz[j][k]=numbers.pop(0)
    return True,matriz

    
t = inputi()


for i in range(t):
    band,ans = solve()
    
    if band:
        for i in range(1,len(ans)-1):
            print(print_list(ans[i][1:-1]))
    elif ans ==1:
        print(1)
    else:
        print(-1)
    #print('') if i!=(t-1) else None
