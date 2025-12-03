def recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*recursive(n-1) #formula for factorial of a number
n=int(input("Enter the number: "))
print("Factorial is: ",recursive(n))