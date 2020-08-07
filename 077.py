
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
print(m)
name=input('type one of the names on the list')
t=m.index(name)
print(t)
answer=input('are you want that person to come to the party')
if answer=='no':
    del(m[t])
    print(m)
