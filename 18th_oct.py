#task 1 fact
n = int(input("Enter the value for factorial:"))
sum = 1
if n == 0:
    print(n,"factorial is",1)
else:
    for i in range(1,n+1):
        sum = sum * i
    print(n,"factorial is",sum)

#task 2 fact
n = int(input("Enter the value for fibonacci series:"))
f0 = 0
f1 = 1
fib = 0
for i in range(0,n):
    f0 = f1
    f1 = fib
    fib = f0 + f1
print(fib)

#break statement
n = 100
for i in range(1,n+1):
    if i ==51:
        break
    print(i)