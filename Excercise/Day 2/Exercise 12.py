num = int(input("Enter the number : "))
num1 = 0
num2 = 1

for i in range(num):
    print(num1, end="  ")
    res = num1 + num2

    num1 = num2
    num2 = res
