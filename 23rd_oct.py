#task1 counting vowels and consonants
vow=0
cons=0
v=['a','e','i','o','u','A','E','I','O','U']
str1=input("Enter the string:")
for i in range(len(str1)):
    for j in range(len(v)):
        if str1[i]==v[j]:
            vow +=1
            break
    else:
        cons +=1
print("count of vowels:",vow)
print("count of consonants:",cons)

#task 2 right angle star pyramid

n = int(input("enter the number to form pyramid:"))
for i in range(n):
    for j in range(i+1):
          print("*",end=" ")
    print("")

# creating power function
def power(x,y):
    print(x**y)
x=int(input("Enter the number:"))
y=int(input("Enter the power for number:"))
power(x,y)

# creating power function using lamda
power = lambda x,y:x**y
x=int(input("Enter the number:"))
y=int(input("Enter the power for number:"))
print(power(5,6))