numbers=[1,2,3,4,5,6,7,8,9]
max=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
print(max)