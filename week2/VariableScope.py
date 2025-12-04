x = 10  # Global variable

def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        z = 30  # Local variable
        print("Local:", z)
        print("Enclosing:", y)
        print("Global:", x)

    inner_function()

outer_function()
