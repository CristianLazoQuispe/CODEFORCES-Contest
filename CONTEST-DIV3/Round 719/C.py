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


def solve2(n,matriz,numbers,start_x,start_y,aea,cola):
    if n==1:
        return False,1
    if n==2:
        return False,-1

    moves = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    
    def rellenar(x,y):
        #cola = [[x,y]]
        while(len(cola)>0):
            [x,y] = cola.pop() if aea==-1 else cola.pop(aea)

            #if matriz[x][y] ==-1:
            #    return
            #if matriz[x][y] !=0:
            #    return   
            if matriz[x][y] ==0:
                rest = []
                for [a,b] in [[-1,0],[1,0],[0,1],[0,-1]] :
                    i_n = x+a
                    j_n = y+b
                    if matriz[i_n][j_n]!=0:
                        rest.append(matriz[i_n][j_n]-1)
                        rest.append(matriz[i_n][j_n]+1)
                for idx,e in enumerate(numbers[::-1]):
                    if not e in rest:
                        matriz[x][y] = e
                        numbers.remove(e)#idx]
                        break

            if matriz[x][y] == 0 :
                return 
            #for move in moves:
            #    x_n = x+move[0]
            #    y_n = y+move[1]
            #    if matriz[x_n][y_n]==0:
            #        cola.append([x_n,y_n])
            
    rellenar(start_x,start_y)
    #print(matriz)
    return len(numbers)==0, matriz

def solve():
    n = inputi()
    if n==1:
        return False,1
    if n==2:
        return False,-1

    matriz = [[-1]*(n+2) for i in range(n+2)]            
    matriz[1][1] =1 
    matriz[1][2] =4 
    matriz[2][2] =6 
    matriz[2][1] =8 

    numbers = [i+1 for i in range(3*3)]
    numbers.remove(1)
    numbers.remove(4)
    numbers.remove(6)
    numbers.remove(8)

    k = 3
    for i in range(1,k+1):
        matriz[k][i]=0
    for j in range(1,k+1):
        matriz[j][k]=0
    cola = []
    for i in range(1,k+1):
        if i==k:
            cola.append([k,i])
        else:
            cola.append([k,i])
            cola.append([i,k])
    #print("number ->",n)

    band,matriz = solve2(3,matriz,numbers,1,k,-1,cola)
    #print("k",k,"m",matriz)

    for k in range(4,n+1):
        #print('ga ',k)
        for i in range(1,k+1):
            matriz[k][i]=0
        for j in range(1,k+1):
            matriz[j][k]=0
        for i in range((k-1)**2+1,(k)**2+1):
            numbers.append(i)
        cola = []
        for i in range(1,k+1):
            if i==k:
                cola.append([k,i])
            else:
                cola.append([k,i])
                cola.append([i,k])
        #print("k",k,"previa m",matriz)
        band,matriz1 = solve2(k,matriz.copy(),numbers,1,k,-1,cola)
        #print("k",k,"m1",matriz1)
        if not band:
            band,matriz2 = solve2(k,matriz.copy(),numbers,1,k,0,cola)
            #matriz = matriz2
            #print("k",k,"m2",matriz2)
        else:
            matriz = matriz1
        
    return band,matriz
t = inputi()


for i in range(t):
    band,ans = solve()
    
    if band:
        #print(ans,len(ans))
        for i in range(1,len(ans)-1):
            #print(ans[i][:])
            print(print_list(ans[i][1:-1]))
    elif ans ==1:
        print(1)
    else:
        print(-1)
    #print('') if i!=(t-1) else None
