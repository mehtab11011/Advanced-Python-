# List comprehension ek chhota aur asaan tareeqa hai list banane ka. Isme hum ek purani list ke har element par koi operation apply kar ke nayi list bana sakte hain.

# Example:
# Agar hume ek list ke sirf woh numbers chahiye jo 3 se divide ho sakte hain:


numbers = [1, 33, 44, 55, 3, 6, 8, 9, 90, 999, 77]
divide_by_three = [i for i in numbers if i % 3 == 0]
print(divide_by_three)  # Output: [33, 3, 6, 9, 90, 999]


# Dictionary Comprehension 
# Dictionary comprehension ek aasaan aur chhota tareeqa hai nayi dictionary banane ka. Isme hum ek purani dictionary ke har key-value pair par koi operation apply karke nayi dictionary bana sakte hain.

# Example 1: Values ko Double Karna
# Agar hume ek dictionary ki har value ko 2 se multiply karna ho:
original = {'apple': 10, 'banana': 20, 'cherry': 30}
reverse = {k: v * 2 for k, v in original.items()}
print(reverse)  
# Output: {'apple': 20, 'banana': 40, 'cherry': 60}

# Given two dictionaries, merge them into one. If a key appears in both dictionaries, add the values together.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
mer={k: dict1.get(k,0) + dict2.get(k,0) for k in set(dict1)|set(dict2)} 
print(mer)
