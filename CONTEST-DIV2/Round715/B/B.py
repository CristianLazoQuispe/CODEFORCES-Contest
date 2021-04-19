t = int(input())

for i in range(t):
    n  = int(input())
    texto = input()
    cnt_t2 = 0
    cnt_t1 = 0
    cnt_m =0
    last_m = 0
    bandera = False
    for idx,j in enumerate(texto):
        if texto[n-idx-1] =='T':
            cnt_t2+=1
        if texto[n-idx-1] =='M':
            last_m = n-idx-1
            break

    aux = 0
    for j in texto[:last_m]:
        if j == 'T':
            cnt_t1+=1
        else:
            if 
            aux+=1


    if 3*(cnt_t2+cnt_t1)/2 != n:
        print('NO')
    else:
        print(cnt,bandera)
        if cnt!=0 or bandera :
            print('NO')
        else:
            print('YES')
