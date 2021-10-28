list_val = []

list_total_ele = int(input("Enter size in list : "))

for i in range(0, list_total_ele):
    list_ele = input("Enter list elements value : ")
    list_val.append(list_ele)
print("")
print("List elements :", list_val)

for j in list_val[1::2]:
    print(j, end=' ')