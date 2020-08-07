numbers=[2,3,5,7]
for i in numbers:
    print(i)
n= int(input('enter a three_digit number'))
if n in numbers:
    print(numbers.index(n))
else:
    print('That is not in the list')
