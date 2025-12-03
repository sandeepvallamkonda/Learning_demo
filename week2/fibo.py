def fibo(n):
    if n==0:
        return "Invalid"
    elif n==1:
        return 0
    elif n==2:
        return 1
    return fibo(n-1)+fibo(n-2) #returning the fibonacci number

def fibo_series(n):
    if n<=0:
        return "Invalid"
    a=0
    b=1
    series=[]
    for i in range(n):
        series.append(a)
        temp=a+b
        a=b
        b=temp
    return series


n=int(input("Enter the number: "))
print(f"The {n} th fibonacci number is {fibo(n)}")
print(f"The fibonacci series is :{fibo_series(n)}")