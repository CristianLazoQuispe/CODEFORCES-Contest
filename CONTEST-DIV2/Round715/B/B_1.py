t = int(input())
def check(texto):

    bandera = False
    cnt_t1 = 0
    cnt_m =0
    aux = 0
    for j in texto:
        if j == 'T':
            aux+=1
            cnt_t1+=1
            if cnt_m>0:
                cnt_t1-=2
                cnt_m-=1
        else:
            if cnt_t1>0:
                cnt_m+=1
            else:
                bandera = True
                break

    print(texto,cnt_t1,cnt_m,aux,bandera)
    if (3*(aux)/2 )!= n or bandera:
        return False
    else:
        return True

for i in range(t):
    n  = int(input())
    texto = input()

    if check(texto) and check(texto[::-1]):
        print('YES')
    else:
        print('NO')