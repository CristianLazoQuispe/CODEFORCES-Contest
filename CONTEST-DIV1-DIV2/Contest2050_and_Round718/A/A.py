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
import math


def n_digit(number):
    return int(math.log10(number))+1

ref = 2050
def n_number(n):
    if n==4:
        return ref
    else:
        return ref*pow(10,n-4)


def solve():
    
    n = inputi()

    digits = n_digit(n)

    #print('number ',n," -> ",digits)
    if digits<4:
        return -1
    cnt = 0    
    while(n>0):
        n2 = n
        cnt+=math.floor(1.0*n/n_number(digits))
        n= n%n_number(digits)
        #print(n2,n_number(digits),cnt)
        digits-=1
        if n<2050:
            break
    if n==0:
        return cnt
    else:
        return -1
    


t = inputi()


for i in range(t):

    ans = solve()

    print(ans,end="")
    print('') if i!=(t-1) else None
