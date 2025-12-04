def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)


num = int(input("Enter a number: "))
print(recursive_sum(num))
