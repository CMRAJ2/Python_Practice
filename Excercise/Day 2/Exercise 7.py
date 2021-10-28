patt_num = int(input("Enter the number of row : "))

for i in range(0, patt_num + 1):
    for j in range(patt_num-i, 0, -1):
        print(j, end=' ')
    print("")
