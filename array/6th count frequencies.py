fruits=["apple","banana","cherry","apple","banana","apple"]
for i in range(len(fruits)):
    count=0
    for j in range(len(fruits)):
        if fruits[i]==fruits[j]:
            count+=1
    print(fruits[i],count)