list_val = []

list_total_ele = int(input("Enter size in list : "))

for i in range(0, list_total_ele):
    list_ele = input("Enter list elements value : ")
    list_val.append(list_ele)
print("")
print("List elements :", list_val)
print("")
print("**Reverse order list**")
list_new = []
for item in reversed(list_val):
    list_new.append(item)
print(list_new)
