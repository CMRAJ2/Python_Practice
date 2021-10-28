string_1 = str(input("Enter string 1 : "))
string_2 = str(input("Enter string 2 : "))

n = len(string_1)//2

print(string_1[0:n] + string_2 + string_1[n:])
