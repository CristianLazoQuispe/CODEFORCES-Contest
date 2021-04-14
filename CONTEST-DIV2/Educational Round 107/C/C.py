
import math

def make_query(colors,query):
    idx = colors.index(query)
    colors[1:idx+1] = colors[0:idx]
    colors[0] =query
    return colors,idx+1

def solve():
    #n = int(input()) # number of reviewers
    types = list(map(int,input().split()))
    n = types[0]
    q = types[1]
    colors = list(map(int,input().split()))
    queries = list(map(int,input().split()))
    
    ans = []
    for query in queries:
        colors,value = make_query(colors,query)
        ans.append(value)
    return ans

ans = solve()
texto = ''
for number in ans:
    texto+=str(number)+' '
print(texto[:-1])  
#print(ans)