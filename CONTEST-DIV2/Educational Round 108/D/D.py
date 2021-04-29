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

import numpy as np

def solve():
    n = inputi()
    number1 = np.array(inputli())
    number2 = np.array(inputli())

    suma_total = np.sum(number1*number2)
    products =[0]
    prod = 0
    for i in range(n):
        prod += number1[i]*number2[i]
        products.append(prod)
    suma_total = products[-1]
    #print(products)
    suma = 0
    for i in range(1,n+1):
        for j in range(i-1,n):
            aux = products[i-1] + suma_total-products[j+1] + np.sum(number1[i-1:j+1][::-1]*number2[i-1:j+1])
            suma =max(aux,suma)
            #print(aux,number1[:i],number1[i:j+1][::-1],number1[j+1:],products[i-1],np.sum(number1[i-1:j+1][::-1]*number2[i-1:j+1]),suma_total-products[j+1])
    return suma


ans = solve()

print(ans,end='')
