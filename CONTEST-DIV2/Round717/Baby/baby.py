def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))


import itertools
import numpy as np


def isSubsetSum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n-1] > sum:
        return isSubsetSum(arr, n-1, sum)

    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])

def findPartion(arr, n):
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    if sum % 2 != 0:
        return False
    return isSubsetSum(arr, n, sum // 2)
 


def print_list(lista):
    s=""
    for i in lista[:-1]:
        s+=str(i+1)+" "
    s+=str(lista[-1]+1)

    return s

def is_minimun(numbers,k):
    ids = [i for i in range(len(numbers))]
    for elements in list(itertools.combinations(ids,k)):
        #print(elements)
        group1 = numbers[list(elements)]
        group2 = numbers[list(set(list(ids))-set(elements))]
        if not findPartion(group2, len(group2)):
            return True,list(elements)

    return False,[]





def solve():

    n = inputi()

    numbers = inputli()
    numbers = np.array(numbers)

    for k in range(0,n):
        band,ans = is_minimun(numbers,k)
        if band:
            return band,ans


band,ans = solve()

if band == False or len(ans)==0:
    print(0)
else:
    print(len(ans))
    print(print_list(ans))
