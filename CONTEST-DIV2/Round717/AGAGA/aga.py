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

    n = inputi()

    numbers = inputli()

    ref = numbers[0]^numbers[1]

    aux = ref
    
    for a in numbers[2:]:
        aux= aux^a

    if (aux==ref or aux==numbers[0] or aux==numbers[1]):
        return 'YES'
    else:
        return 'NO'


t = inputi()


for i in range(t):

    ans = solve()
    print(ans,end="")
    #print("Case #"+str(i+1)+':',print_list(ans),end='')
    #print("Case #"+str(i+1)+':',ans,end='')
    print('') if i!=(t-1) else None
