t = int(input())

for i in range(t):
    n = int(input())
    lista = list(map(int,input().split(' ')))

    even = []
    for i in lista:
        if i%2==0:
            print(i,end=' ')
        else:
            even.append(i)
    for i in even:
        print(i,end=' ')
    print('')
