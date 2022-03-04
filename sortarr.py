arr = [5, 7, 1, 8, 3]
temp = 0

print("Orginal Array: ")
for i in range(0, len(arr)):
    print(arr[i], end= " ")


for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print()
print("Elements accessing in assending order: ")
for i in range(0, len(arr)):
    print(arr[i], end="")
print()    