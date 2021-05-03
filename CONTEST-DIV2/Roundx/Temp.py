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
    [n,k] = inputli()

    numbers = inputli()
    #numbers2 = numbers.copy()
    for idx,a in enumerate(numbers):

        while(k>0 and numbers[idx]>0):
            numbers[idx]-=1
            k-=1
            numbers[-1]+=1
       

    return numbers


t = inputi()


for i in range(t):

    ans = solve()
    
    #print("Case #"+str(i+1)+':',print_list(ans),end='')
    print("Case #"+str(i+1)+':',ans,end='')
    print('') if i!=(t-1) else None
