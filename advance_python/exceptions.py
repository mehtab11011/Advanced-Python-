# 1. Question: What happens when you divide a number by zero?

try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    
# How can you handle a file not found error?

try:
    open("mk.txt","r")
except FileNotFoundError as e:
    print(f"{e}")
    
# How can you handle multiple exceptions in a single block?

try:
    num=int("abc")
    x=8/num
except ValueError as v:
    print(v)
    
except ZeroDivisionError as z:
    print(z)
finally:
    print("we don this ")