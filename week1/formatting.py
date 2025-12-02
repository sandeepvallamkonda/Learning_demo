def format_sentence(name, age, city):
    return f"My name is {name}, I am {age} years old, and I live in {city}."


name = input("\nEnter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print("Formatted Sentence:", format_sentence(name, age, city))
