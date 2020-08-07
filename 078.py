programmes=['asre jadid','kadak','news','movie']
for i in programmes:
    print(i)
n=input('enter another show')
m=int(input('enter aposition show'))


if m<4:
    q=[]
    for i in range(0,m):
        q.append(programmes[i])
    t=[]
    for j in range(m,4):
        t.append(programmes[j])
    print(q+[n]+t)
elif m==4:
    programmes.append(n)
    print(programmes)
    
