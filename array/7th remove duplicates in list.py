fruits=["apple","banana","cherry","apple","banana","apple"]
new_list=[]
for i in range(len(fruits)):
    if fruits[i] not in new_list:
        new_list.append(fruits[i])
print(new_list)