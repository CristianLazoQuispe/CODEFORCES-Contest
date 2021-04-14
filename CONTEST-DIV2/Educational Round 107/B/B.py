T = int(input())

import math

def solve():
    #n = int(input()) # number of reviewers
    types = list(map(int,input().split()))
    a =types[0]
    b =types[1]
    c =types[2]

    range_gcd = [10*(c-1),10*c-1]
    range_a   = [10*(a-1),10*a-1]
    range_b   = [10*(b-1),10*b-1]    
    for gcd in range((10**(c-1)),10**c):
        for q in range(int((10**(a-1))/gcd),int((10**a)/gcd)):
            x= gcd*q
            for r in range(int((10**(b-1))/gcd),int((10**b)/gcd)):
                #print('gcd',gcd,q,r,10**(b-1)/gcd)
                if math.gcd(q,r)==1:
                    y = gcd*r
                    #print('abs',gcd,q,r,x,y)
                    return [x,y]
    return [1,1]
for i in range(T):
    ans = solve()
    texto = ''
    for number in ans:
        texto+=str(number)+' '
    print(texto[:-1])