def fib(n):
    a,b = 1,1
    for i in range(n-2):
        a,b = b,a+b
    print(a+b)

num = eval(input("Enter the num you want to reach:"))
fib(num)