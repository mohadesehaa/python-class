name=input('name of somebody you want to invite to a party')
print(name,'','has now been invited')
count=1

while True:
    n=input('are you want to invite somebody else if you want enter her name')
    if n!='no':
        count+=1
    elif n=='no':
        print(count)
        break
    
    
    
    
