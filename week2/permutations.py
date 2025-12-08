def generate_permutations(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i in range(len(s)):
        # Take each character as the first character
        char = s[i]
        # Remaining string after removing the chosen character
        remaining = s[:i] + s[i+1:]
        # Recursively get permutations of the remaining string
        for perm in generate_permutations(remaining):
            perms.append(char + perm)
    return perms

text = input("Enter a string: ")
result = generate_permutations(text)
print("All permutations:")
print(result)
