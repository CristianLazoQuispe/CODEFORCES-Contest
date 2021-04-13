T = int(input())


def solve():
    n = int(input()) # number of reviewers
    types = list(map(int,input().split()))
    server_1 = 0 # type 1 and 3
    server_2 = 0 # type 2 
    for person in types:
        if person in[1,3]:
            server_1+=1
    return server_1

for i in range(T):
    ans = solve()
    print(ans)