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

import math

def solve():
    [n,l1,r1] = inputli()
    colors = inputli()
    l = min(l1,r1)
    r = max(l1,r1)
    #left = sorted(colors[:l])
    #right= sorted(colors[l:])
    left = {}
    right= {}
    
    for i in colors[:l]:
        if not i in left:
            left[i]=1
        else:
            left[i]+=1

    for i in colors[l:]:
        if i in left:
            if left[i]>=1:
                left[i]-=1
            else:
                del left[i]
                if not i in right:
                    right[i]=1
                else:
                    right[i]+=1
        else:
            if not i in right:
                right[i]=1
            else:
                right[i]+=1
    print(left,right)
    cnt = 0
    s_left = sum(left.values())
    s_right = sum(right.values())
    aux = None
    if s_left == s_right:
        return s_right
    elif s_left <s_right:
        aux = right
    else:
        aux = left
    cnt = min(s_right,s_left)
    
    diff = abs(s_right-s_left)/2
    print('diff',cnt,diff)
    for i in aux:
        if diff <= 0:
            break
        if aux[i]>1:
            q = min(diff,aux[i]//2)
            cnt  += q
            diff -= q
            aux[i] = aux[i]-2*q
    print(aux)
    return cnt    
    #left  = dict(sorted(left.items(), key=lambda item: item[1]))
    #right = dict(sorted(right.items(), key=lambda item: item[1]))
    #print(cnt,left,right)

t = inputi()


for i in range(t):

    ans = solve()
    
    print(int(ans),end='')
    print('') if i!=(t-1) else None
