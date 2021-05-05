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
    texto = input()
    texto = list(texto)
    dic = {}
    cnt = 1
    for idx,i in enumerate(texto):
        #print(i)
        if not i in dic:
            dic[i]= 1
        else:
            #print(i,idx-1,texto[idx-1])
            if i!=texto[idx-1]:
                return 'NO'
            dic[i]+=1
    return 'YES'        

t = inputi()


for i in range(t):

    ans = solve()
    
    #print(print_list(ans),end='')
    print(ans,end='')
    print('') if i!=(t-1) else None
