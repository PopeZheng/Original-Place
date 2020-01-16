num = eval(input("Enter the num you want to reach:"))
sum = 0
for i in range(2,num+1):
    for j in range(1,i):
        if i%j ==0:
            sum += j
    if sum == i:
        print(i)
    sum = 0