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


class node:
    def __init__(self,name):
        self.name  = name
        self.children = []
    def add(self,child):
        self.children.append(child)
def solve():
    n = inputi()
    nodes = {}
    for i in range(n-1):
        [a,b] = inputli()
        if a not in nodes:
            nodes[a] = node(a)
            nodes[a].add(b)
        else:
            nodes[a].add(b)

        if b not in nodes:
            nodes[b] = node(b)
            nodes[b].add(a)
        else:
            nodes[b].add(a)
    visited = {}
    for j in nodes:
        visited[i] = 0

    root = list(nodes.keys())[0]
    
    #print(root)

    
    cnt = 0  

t = inputi()


for i in range(t):

    solve()