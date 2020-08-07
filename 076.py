m1=input('enter the names of person you want to invite to a party')
m2=input('enter the names of person you want to invite to a party')
m3=input('enter the names of person you want to invite to a party')
m=[]
m.append(m1)
m.append(m2)
m.append(m3)
while True:
    n=input('mehman')
    if n=='no':
        break
    m.append(n)
print(len(m))
