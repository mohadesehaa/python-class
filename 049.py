compnum=50
number=int(input('enter a number'))
count=1
if number==compnum:
    print('well done , you took ',1,'attempts')
else:
    while True:
        number=int(input('enter a number'))
        count+=1
        if number==compnum:
            print('well done, you took','',count,'attempts')
            break
        
