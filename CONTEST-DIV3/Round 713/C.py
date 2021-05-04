def reduce_text(a,b,texto):
    n = len(texto)
    new_texto = list('?'*n)
    middle = n//2
    cnt = 0
    for i in range(middle):
        if texto[i] == texto [n-1-i]:
            if texto[i]!='?':
                new_texto[i]=texto[i]
                new_texto[n-1-i]=texto[i]
                if texto[i]=='1':
                    b-=2
                else:
                    a-=2
            else:
                cnt+=2
        else:
            e =texto[i]+texto [n-1-i] 
            if e in ['01','10']:
                return -1,-1,-1,''
            elif e in ['?1','1?']:
                b-=2
                new_texto[i]='1'
                new_texto[n-1-i]='1'
            else:
                a-=2
                new_texto[i]='0'
                new_texto[n-1-i]='0'


    if n%2 ==1:
        pos = n//2
        middle = texto[pos]
        if middle =='?':            
            new_char = None
            if a%2 ==1:
                new_char = '0'
                a-=1
            if b%2 ==1 :
                new_char = '1'
                b-=1
            new_texto[pos]=new_char

        elif middle =='1':
            b-=1
            new_texto[pos]='1'
        else:
            a-=1
            new_texto[pos]='0'
    return a,b,cnt,new_texto


t = int(input())


for i in range(t):

    [a,b] = list(map(int,input().split(' ')))
    texto = input()

    a,b,cnt,texto = reduce_text(a,b,texto)
    #print(a,b,texto)
    if texto=='':
        print(-1)
    else:
        n = len(texto)
        middle = n//2

        for i in range(middle):
            if texto[i] == '?':
                if a>0:
                    texto[i] = '0'
                    texto [n-1-i] = '0'
                    a-=2
                else:
                    texto[i] = '1'
                    texto [n-1-i] = '1'
                    b-=2
        #print(a,b,texto)
        if a==0 and b==0:
            print(''.join(texto))
        else:
            print(-1)
