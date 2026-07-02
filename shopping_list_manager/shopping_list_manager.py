shopping_list = []

count = int(input("How many items do you want to add? "))

for i in range(count):
    item = input("Enter an item: ")
    shopping_list.append(item)

for i in range(len(shopping_list)):
    print(f"Item {i + 1}: {shopping_list[i]}")

number = int(input("Enter the number of the item you want to remove: "))
index = number - 1
shopping_list.remove(shopping_list[index])

print("Updated list:")
for i in range(len(shopping_list)):
    print(f"Item {i + 1}: {shopping_list[i]}")