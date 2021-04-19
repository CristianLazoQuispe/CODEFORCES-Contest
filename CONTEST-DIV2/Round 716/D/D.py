import math

lista = list(map(int,input().split(' ')))

n = lista[0]
q = lista[1]

numbers = list(map(int,input().split(' ')))

freq = {}
maxi = 0
maxi_number = None

for number in numbers:
    if not number in freq.keys():
        freq[number]=1
    else:
        freq[number]+=1 

def get_dic(freq,lista):
    maxi = 0
    maxi_number = None

    for number in list(set(lista)):
        if freq[number]>maxi:
            maxi = freq[number]
            maxi_number = number    
    return maxi_number,maxi

for query in range(q):
    lista_aux = list(map(int,input().split(' ')))
    l = lista_aux[0]
    r = lista_aux[1]

    sub_sequence = numbers[l-1:r]
    ans = 0
    mode,freq_mode = get_dic(freq,sub_sequence)
    print(sub_sequence,mode,freq_mode)
    for i in range(1,r-l+2):
        aux1 = math.ceil(freq_mode/i)
        aux2 = math.ceil((r-l+1)/(i*2))

        print(i,aux1,aux2)
        if aux1 <= aux2:
            ans = i
            break
    print(ans)
