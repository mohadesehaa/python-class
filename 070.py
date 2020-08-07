country=('China','Japan','Iran','Iraq','Russia')
print(country)
name=input('enter a name of  a country')
m=country.index(name)

n=int(input('enter a number:'))
if n==0:
    
    print((name,)+country[1:])
elif n==1:
    
    print(country[0]+(name,)+country[2:])
elif n==2:
    
    print(country[0:2]+(name,)+country[3:])
elif n==3:
    
    print(country[0:3]+(name,)+(country[4],))
elif n==4:
    
    print(country[0:4]+(name,))
