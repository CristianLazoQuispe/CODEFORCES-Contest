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
    numbers = inputli()
    print(n//2)
    for i in range(1,n,2):
        x = numbers[i-1]
        y = numbers[i]
        numbers[i]= 10**9+7
        numbers[i-1] = min(x,y)
        print(i,i+1,min(x,y),10**9+7)
    #print(numbers)
t = inputi()


for i in range(t):
    solve()
