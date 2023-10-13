#task 1
r = int(input("enter the radius:"))
pi = 3.14
print(pi*(r**2))

m = int(input("enter the 1st value :"))
n = int(input("enter the 2nd value:"))

if(m<n):
    print(m,"is less than",n)
elif(m==n):
    print(m, "is equal to", n)
else:
    print(m, "is greater than", n)

#task 2

a = int(input("enter the 1st value :"))
b = int(input("enter the 2nd value:"))
c = int(input("enter the 3rd value:"))

max = (a if a > b and a > c else b if b > a and b > c else c)
print("Maximum of ", a, b, c, "is :", max)

print(a**2)
print(a**3)