colours=[]
for i in range(10):
    colour=input()
    colours.append(colour)

n1=int(input('enter start number'))
n2=int(input('enter end number'))
if 0<=n1 and n1<=4 and n2>=5 and n2<=9:
    print(colours[n1+1:n2])
