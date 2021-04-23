def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))


def print_list(lista):
    s=""
    for i in lista[:-1]:
        if i!= None:
            s+=str(i)+" "
    if lista[-1]!= None:
        s+=str(lista[-1])

    return s


def llenar(ans,row,column,cnt,value):
    if cnt==1:
        return 0
    #print(ans,row,column)

    if (ans[row][max(column-1,0)]== None):
        ans[row][max(column-1,0)]=value
        return llenar(ans,row,max(column-1,0),cnt-1,value)
    elif(ans[min(row+1,len(ans)-1)][column]== None):
        ans[min(row+1,len(ans)-1)][column]=value
        return llenar(ans,min(row+1,len(ans)-1),column,cnt-1,value)
    else:
        return -1


def solve():

    n =  inputi()

    diagonal = inputli()

    ans = [[None]*n for i in range(n)]

    for i in range(n):
        ans[i][i] = diagonal[i]

    #print(ans)

    for idx,x in enumerate(diagonal):
        auxiliar = llenar(ans,idx,idx,x,x)
        if auxiliar==-1:
            break
    
    if ans==-1:
        print(-1)  
    else:
        for i in range(n):
            print(print_list(ans[i]))
    
    return 0



solve()
