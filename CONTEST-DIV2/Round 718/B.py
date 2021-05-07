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

def get_pesi(a,b,y):

    for i in range(2,a*b*2):
        if math.gcd(i,a)==1 and math.gcd(i,b)==1 and i>y:
            return i
    return -1
def solve():
    n = inputi()
    numbers = inputli()

    back = numbers[0]


    if n ==1:
        return 0


    ans = []
    idx = 1 

    for i in range(n-1):
        if numbers[i] ==1 and numbers[i+1]==1:
            j = i+1
            x = i+1
            y = 1
            numbers[i]=x
            numbers[j]=y
            ans.append([i,j,x,y])        

    while(idx<n-1):
        number = numbers[idx]
        #print('analiza id ',idx,'num',number)
        #print(math.gcd(back,number),math.gcd(number,numbers[idx+1]))
        if math.gcd(back,number)!=1 or math.gcd(number,numbers[idx+1])!=1 or (back ==1 and number ==1) or (numbers[idx+1] ==1 and number==1):
            #print('old ',numbers)
            
            ai = number
            aj = numbers[n-1]#max(numbers)
            i = idx
            j = n-1#numbers.index(aj)
            aux = get_pesi(back,numbers[idx+1],min(ai,aj))
            x = aux
            y = min(ai,aj)
            numbers[i] = x
            numbers[j] = y
            ans.append([i+1,j+1,x,y])
            #print('r',ai,aj,x,y)
            #print('minis',min(ai,aj),min(x,y))
            #print('new ',numbers,ai,x)
        back = numbers[idx]
        idx+=1

    #print('new ',numbers)
    if len(ans) == 0 :
        print(0)
    else:
        print(len(ans))
        for idx,i in enumerate(ans):
            if idx == len(ans)-1:
                print(print_list(i))
            else:
                print(print_list(i))
t = inputi()


for i in range(t):

    solve()
    
    #print(print_list(ans),end='')
    #print(ans,end='')
    #print('') if i!=(t-1) else None
