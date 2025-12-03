num = int(input("Enter a number: "))
print(f"Multiplication Table for {num}:")
for i in range(1, 11):  #printing upto 10
    print(f"{num} x {i} = {num * i}")
