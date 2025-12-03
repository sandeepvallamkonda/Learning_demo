def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (100 * n)) ** (n * time)  #formula of CI
    return round(amount, 2)


principal = float(input("\nEnter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = int(input("Enter time in years: "))
n = int(input("Enter number of times interest applied per year: "))
print("Compound Interest Amount:", calculate_compound_interest(principal, rate, time, n))
