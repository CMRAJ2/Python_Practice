string = input("Enter string with lower and upper characters : ")
small = ""
caps = ""

for c in string:
    if c.islower():
        small = small+c
    else:
        caps = caps+c

print(small + caps)
