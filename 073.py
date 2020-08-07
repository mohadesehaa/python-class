d={}
for i in range(1,5):
    n=input('enter your favourite foods')
    d.setdefault(i,n)
print(d)
m=int(input('which one you want to get rid of and remove it '))
d.pop(m)
print(d)
    
