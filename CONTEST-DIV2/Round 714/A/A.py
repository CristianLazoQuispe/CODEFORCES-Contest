T = int(input())

def make(k):
    maxi = 2*k+1
    ans = [0]*(maxi)
    
    for i in range(k):
        ans[i*2+1]=maxi-k+i+1 
    for i in range(maxi-k):
        ans[i*2]= i+1
    #print('ha',ans)
    return ans
def solve(n,k):
    mini_length = k*2+1
    if n<mini_length:
        return -1
    else:
        return make(k)+[i for i in range(mini_length+1,n+1)]

for i in range(T):
    lista = list(map(int,input().split()))
    n = lista[0]
    k = lista[1]
    ans = solve(n,k)
    if ans==-1:
        print(ans)
    else:
        texto = ''
        #print(ans)
        for i in ans:
            texto+=str(i)+' '
        print(texto[:-1])
    