t = int(input())

for i in range(t):
    ga = input()
    [a,b] = list(map(int,ga.split(' ')))
    #print(a,b)
    s = list(map(str,input()))
    s_size = len(s)
    #if len(s)==0:
    #    print(-1)
    #    continue
    #print(s_size)

    if a==0 or b ==0:
        if (a+b)!=s_size:
            print(-1) 
            continue
    elif a%2!=0 and b%2!=0:
        print(-1)
        continue
    elif (a+b)!=s_size:
        print(-1) 
        continue
    cnt = {'0':0,'1':0,'?':0}

    for element in s:
        cnt[element]+=1
    #'''
    if cnt['0']>a:
        print(-1)
        continue
    if cnt['1']>b:
        print(-1)
        continue
    #'''
    if b==0:
        for idx in range(s_size):
            if s[idx]=='1':
                s='-1'
                break
            else:
                s[idx]='0'
    elif a==0:
        for idx in range(s_size):
            if s[idx]=='0':
                s='-1'
                break
            else:
                s[idx]='1'
    else:
        for idx in range(s_size//2):
            if s[idx]!=s[s_size-idx-1]:
                if s[idx] in ['0','1'] and s[s_size-idx-1] in ['0','1'] :
                    s='-1'
                    break
                elif s[idx]=='?':
                    s[idx]=s[s_size-idx-1]
                else:
                    s[s_size-idx-1] = s[idx]
                cnt[s[idx]]+=1
            else:
                if s[idx]=='?':
                    if (cnt['0']+2)<=a:
                        s[idx]='0'
                        s[s_size-idx-1]='0'
                        cnt['0']+=2
                    elif (cnt['1']+2)<=b:
                        s[idx]='1'
                        s[s_size-idx-1]='1'
                        cnt['1']+=2
                #else:
                #    cnt[s[idx]]+=2  
        #print('tmr',idx)
        if len(s)>2 and len(s)%2!=0:
            if s[idx+1] =='?':
                if cnt['0']<a:
                    s[idx+1]='0'
                else:
                    s[idx+1]='1'
    print(''.join(s))