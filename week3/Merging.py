'''Merge two dictionaries and sum common keys'''
def merge_and_sum(dict1, dict2):
    merged = dict1.copy()  # Start with first dictionary
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum values for common keys
        else:
            merged[key] = value   # Add new key
    return merged


dict_a = {'a': 10, 'b': 20, 'c': 30}
dict_b = {'b': 5, 'c': 15, 'd': 25}

result = merge_and_sum(dict_a, dict_b)
print("Merged Dictionary:", result)
