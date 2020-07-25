def fib(arg):
    if arg==1 :
        return 0
    if arg==2:
        return 1
    else:
        return fib(arg-2)+fib(arg-1)

