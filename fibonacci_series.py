# series : 0 1 1 2 3 5 8 13 21

def fib(n):
    a = 0 
    b = 1

    if n == 1:
        print(a)
    else:
        print(0)
        print(1)

        for i in range(2, n):
            c = a + b
            a, b = b, c
            print(c)

fib(1)