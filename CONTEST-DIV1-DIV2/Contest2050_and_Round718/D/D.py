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


moves = [[-1,0],[1,0],[0,-1],[0,1]]

def min_path1(matriz,weights,i,j,k):
    paths = min_path2(matriz,weights,i,j,k)
    
    #print('paths')
    total_cost = []
    
    for path in paths:
        #print(path)
        if path[-1] == [i,j]:
            x_back = i
            y_back = j 
            suma = 0
            for [x,y] in path:
                #print(str(x_back)+str(y_back)+str(x)+str(y))
                suma+= weights[str(x_back)+str(y_back)+str(x)+str(y)]
                x_back = x
                y_back = y
            total_cost.append(suma)

    if len(total_cost)>0:
        return min(total_cost)    
    else:
        return -1
def min_path2(matriz,weights,i,j,k):
    ans = []
    if k==0:
        return []
    for move in moves:
        x_new = i+move[0]
        y_new = j+move[1]
        #print(x_new,y_new,len(matriz),len(matriz[0]))
        if x_new>=0 and y_new>=0 and x_new < len(matriz) and y_new < len(matriz[0]):      
            #cost = weights[str(i)+str(j)+str(x_new)+str(y_new)]
            paths = min_path2(matriz,weights,x_new,y_new,k-1)
            if len(paths)==0:
                ans.append([[x_new,y_new]])
            else:
                for path in paths:
                    ans.append([[x_new,y_new]]+path)
                    #print('ga',[[x_new,y_new]]+path)
    #print(i,j,k,ans)

    return ans

def solve():
    [n,m,k] = inputli()
    
    matriz = [[None]*m for i in range(n)]
    ans = [[None]*m for i in range(n)]
    
    weights = {}

    for i in range(n):
        weight = inputli()
        for idx,w in enumerate(weight):
            weights[str(i)+str(idx)+str(i)+str(idx+1)] = w
            weights[str(i)+str(idx+1)+str(i)+str(idx)] = w
            

    for i in range(n-1):
        weight = inputli()
        for idx,w in enumerate(weight):
            weights[str(i)+str(idx)+str(i+1)+str(idx)] = w 
            weights[str(i+1)+str(idx)+str(i)+str(idx)] = w 
    
    #print(k,weights)

    for i in range(n):
        for j in range(m):
            #print(i,j,'start ')
            if k%2 == 1:
                aux = -1
            else:
                aux = min_path1(matriz,weights,i,j,k)
            ans[i][j] = aux
    
    
    for i in range(n):
        print(print_list(ans[i]))
    return 0

respuesta = solve()

if respuesta==-1:
    print(-1)
