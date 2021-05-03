
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


def solve():
    [n,k] = inputli()
    numbers = inputli()
    #print(k,numbers)
    band = "NO"
    ans = []
    maxi = max(numbers)
    suma = sum(numbers)
    if k==suma:
        return band,ans
    id = numbers.index(maxi)
    if k<maxi:
        ans = [maxi]+[e for i,e in enumerate(numbers) if i!=id]
        return "YES",ans
    
    numbers = sorted(numbers)
    #print(numbers)
    suma = 0
    for idx,a in enumerate(numbers):
        suma+= a
        if suma==k and idx!=n-1:
            #print("atraoada ",a,numbers[idx+1:])
            ans += numbers[idx+1:]+[a]
            return "YES",ans
        ans.append(a)
    return "YES",ans


t = inputi()


for i in range(t):

    band,ans = solve()
    if band=="NO":
        print(band)
    else:
        print(band)
        print(print_list(ans),end='')
        print('') if i!=(t-1) else None
