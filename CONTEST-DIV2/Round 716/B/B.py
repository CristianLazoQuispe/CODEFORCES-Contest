import math
t = int(input())
m = 1000000007

p = (int)(1e9+7)
  
# Using direct fast method to compute 
# (a ^ b) % p.


def solve(numbers):
    n = numbers[0]
    k = numbers[1]

    #nf = math.factorial(n) 
    ans = d = pow(n, k, m) #int(nf/(math.factorial(k)*math.factorial(n-k)) % m)
    return ans 

for i in range(t):
    numbers = list(map(int,input().split(' ')))
    ans = solve(numbers)
    print(ans)