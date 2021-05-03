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

#import numpy as np

def solve():
    n = inputi()
    number1 = inputli()
    number2 = inputli()

    products =[0]
    prod = 0
    for i in range(n):
        prod += number1[i]*number2[i]
        products.append(prod)
    suma_total = products[-1]
    suma = suma_total
    for i in range(0,n,0.5):
        subarray = 0 if type(i)!= int else number1[i]
        for w in range(1,min(int(n-i),int(i+1))):
            for w in range(i-1,j+1):
                subarray += number1[j+i-1-w]*number2[w]
            #subarray = np.sum(number1[i-1:j+1][::-1]*number2[i-1:j+1])

            aux = products[i-1] + suma_total-products[j+1] + subarray
            suma =max(aux,suma)
            #print(aux,number1[:i],number1[i:j+1][::-1],number1[j+1:],products[i-1],subarray,suma_total-products[j+1])
    return suma


ans = solve()

print(ans,end='')
