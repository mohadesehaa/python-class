number=int(input('enter a number'))
if number<10:
    print('Too low')
    while True:
        number=int(input('enter another number'))
        if number>=10 and number<=20:
            print('Thank you')
            break
elif number>20:
    print('Too high')
    
    while True:
        number=int(input('enter another number'))
        if number>=10 and number<=20:
            print('Thank you')
            break
elif number>=10 and number<=20:
    print('Thank you')
            
    
