t = int(input())


for i in range(t):
    n = int(input())
    points = []
    cnt = 0
    for j in range(n):
        lista = list(map(str,input()))
        if cnt!=2:
            for idx,c in enumerate(lista):
                if c=='*':
                    points.append([j,idx])
                    cnt+=1
                    if cnt==2:
                        break
    if points[0][0]!=points[1][0]:
        if points[0][1]!=points[1][1]:
            points.append([points[0][0],points[1][1]])
            points.append([points[1][0],points[0][1]])
        else:
            if points[1][1] == (n-1):
                aux=-1
            else:
                aux=1
            points.append([points[0][0],aux+points[1][1]])
            points.append([points[1][0],aux+points[0][1]])
    else:
        if points[0][1]!=points[1][1]:
            if points[0][0] == (n-1):
                aux=-1
            else:
                aux=1
            points.append([aux+points[0][0],points[1][1]])
            points.append([aux+points[1][0],points[0][1]])
        else:
            if points[0][0] == (n-1):
                aux1=-1
            else:
                aux1=1
            if points[1][1] == (n-1):
                aux2=-1
            else:
                aux2=1
            points.append([aux1+points[0][0],aux2+points[1][1]])
            points.append([aux1+points[1][0],aux2+points[0][1]])


    for w in range(n):
        for q in range(n):
            if [w,q] in points:
                print('*',end='')
            else:
                print('.',end='')
        print('')
    