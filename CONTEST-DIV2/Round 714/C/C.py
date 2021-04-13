import functools,operator

T = int(input())

maximo = 2*100000+1
dp = [[i,[0]*(maximo)] for i in range(0,10)]
sumas = [0 for i in range(0,10)]

def get_suma(number):
    suma = ''
    for i in str(number):
        suma += str(i+1)
        
for i in range(1,maximo):
    for number in range(0,10):
        suma = get_suma(sumas[number])
        dp[number,i] = 
def calculate(digit,k):


def solve(n,k):
    suma = 0
    for i in str(n):
        digit = int(i)
        suma+= calculate(digit,k)
    return suma

m = 1000000007


for i in range(T):
    lista = list(map(int,input().split()))
    n = lista[0]
    k = lista[1]    
    ans = solve(n,k)%m
    print(ans)
