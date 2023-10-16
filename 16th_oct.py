#task1
score = int(input("Enter the student score:"))
if (90<=score<=100):
    print("A")
elif(80<=score<=89):
    print("B")
elif(79<=score<=70):
    print("C")
elif (69<=score<=60):
    print("D")
elif(0<=score<=50):
    print("E")
else:
    print("please enter the correct score")

#task2
year = int(input("Enter the year:"))
if(year%400 ==0 and year % 100 ==0):
    print(year, "is leap year")
elif(year%4 ==0 and year % 100 != 0):
          print(year,"is leap year")
else:
    print(year,"is not leap year")

#task3

side1 = int(input("Enter the 1st side:"))
side2 = int(input("Enter the 2nd side:"))
side3 = int(input("Enter the 3rd side:"))

if(side1==side2==side3):
    print("Equilateral")
elif(side1==side2!=side3 or side3==side2!=side1 or side1==side3!=side2):
    print("Isoceles")
else:
    print("scalene")