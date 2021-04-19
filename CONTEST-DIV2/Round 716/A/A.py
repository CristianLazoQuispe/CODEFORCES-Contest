import math
t = int(input())


def solve(n,numbers):
    ans = 'NO'
    for number in numbers:
        aux = int(math.sqrt(number))
        if number != (aux*aux):
            ans = 'YES'
            break
    return ans 

for i in range(t):
    n = int(input())
    numbers = list(map(int,input().split(' ')))

    ans = solve(n,numbers)
    print(ans)