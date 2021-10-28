string = str(input("Enter odd string (greater than 7) : "))

if (len(string) % 2 == 1 and len(string)) >= 7:
    n = ((len(string) - 1) // 2) - 1
    b = n + 3
    print(string[n:b])
else:
    print("Entered odd string length is less than 7.")
