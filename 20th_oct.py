#task1 palindrome
def pal(n):
    pal1 = list(n)
    rpal = pal1[::-1]
    palret = ""
    for i in rpal:
        palret = palret+i
    if n == palret:
        print(palret,"is a palindrome")
    else:
        print(palret,"is not a palindrome")

n = input("Enter the palindrome value:")
pal(n)

# task2 sum of digits

def SOD(n):
    sum = 0
    while n>0:
        m=n%10
        sum = sum +m
        n = n//10
    print(sum)
n = int(input("Enter the SOD value:"))
SOD(n)



