def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n>2:
        return fib(n-1)+fib (n-2)
n=int(input())
m=[]
for i in range(1,n+1):
    m.append(i)
print(list(map(fib,m)))
