list_1 = [1, 2, 3]
list_2 = list_1
list_2.append(4)

print("List 1:", list_1) # Both lists refer to the same object or id
print("List 2:", list_2)
print(id(list_1))
print(id(list_2))

# Output:
# Both lists refer to the same object or id
# List 1: [1, 2, 3, 4]
# List 2: [1, 2, 3, 4]
# 1992913721600
# 1992913721600