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
    texto = list(input())+['/']

    numbers = []

    cnt = 0
    back = '.'
    for e in texto:
        if e == back:
            cnt+=1
        else:            
            numbers.append(cnt)
            cnt=1
        back = e
    print(numbers)
    return 1
t = inputi()


for i in range(t):

    ans = solve()
    
    #print(print_list(ans),end='')
    print(ans,end='')
    print('') if i!=(t-1) else None
