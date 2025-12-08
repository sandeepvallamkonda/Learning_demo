'''Perform CRUD on lists'''
# Initialize an empty list
my_list = []

# CREATE: Add elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("After CREATE:", my_list)

# READ: Access elements
print("READ first element:", my_list[0])
print("READ entire list:", my_list)

# UPDATE: Modify an element
my_list[1] = 25
print("After UPDATE:", my_list)

# DELETE: Remove an element
my_list.remove(30)  # Removes value 30
print("After DELETE:", my_list)

# DELETE by index
del my_list[0]
print("After DELETE by index:", my_list)
