day=int(input())
month=int(input())
year=int(input())
t=0
m=[31,28,31,30,31,30,31,31,30,31,30,31]
if year%4==0 and year%100==0:
        
        
        m[1]=29
if year%4==0 and year%100!=0:
    m[1]=29
for i in range(0,month-1):
    t+=m[i]
t+=day
print(t)
