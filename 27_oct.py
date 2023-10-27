#math task
n = int(input("enter the number of values to put in list:"))
list1 = []
for i in range(n):
    a = int(input("enter the value:"))
    list1.append(a)
print(list1)
print(max(list1))
print(min(list1))
print(sum(list1))
prod = 1
for i in range(len(list1)):
    prod = prod * list1[i]
print(prod)

#string task
n = int(input("enter the number of values to put in list:"))
list2 = []
count = 0
for i in range(n):
    a = (input("enter the value:"))
    list2.append(a)
for i in range(len(list2)):
    if len(list2[i])>=2:
        if list2[i][0]==list2[i][-1]:
            count +=1
print(count)