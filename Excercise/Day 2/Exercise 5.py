list_val = []

list_total_ele = int(input("Enter size in list : "))

for i in range(0, list_total_ele):
    list_ele = input("Enter list elements value : ")
    list_val.append(list_ele)
print("")
print("List elements :", list_val)

new_list_val = []
for ele in list_val:
    if int(ele) % 5 == 0:
        new_list_val.append(ele)
    elif int(ele) <= 150:
        new_list_val.append(ele)
    elif int(ele) <= 500:
        new_list_val.append(ele)
print("Result :", new_list_val)
