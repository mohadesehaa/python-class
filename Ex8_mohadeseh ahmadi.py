m=[31,28,31,30,31,30,31,31,30,31,30,31]
def tar(year,month,day):
    t=0
    if year%4==0 and year%100==0:
        
        
        m[1]=29
        
    if year%4==0 and year%100!=0:
        
        
        m[1]=29
    for i in range(0,month-1):
        t+=m[i]
    return t+day
