# Write a function named add_numbers that takes 
# any number of arguments and returns their sum. 
# If no arguments are provided, return 0.
def add_number(*args):
    if args:
        sum=0
        for i in args:
            sum=sum+i
        return (sum)
    else:
        print(0)

nuber=(1,2,3)
print(add_number(*nuber))

#eassy 
def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(10, 20))   # Output: 30
print(add_numbers())         # Output: 0


# Write a function named greet_user that accepts a user's first and last name as keyword arguments and prints a greeting in the format: "Hello, <first_name> <last_name>!". If a name is missing, use "Guest" as the default.

def greet_user(**kwargs):
    first_name = kwargs.get('first_name', 'Guest')
    last_name = kwargs.get('last_name', 'Guest')
    print(f"Hello, {first_name} {last_name}!")

name={"first_name":"mehtab","last_name":"khan"}
print(greet_user(**name))
    
    
# Write a function describe_person that accepts any number of positional arguments as hobbies and any number of keyword arguments for personal details (like name, age, etc.). Print the details and hobbies in a readable format.

def describe_person(*hobbies, **kwargs):
       print("/details")
       for keys,values in kwargs.items():
           print(f"{keys}:{values}")
           
       print("/hobbies")
       if hobbies:
           for i in hobbies:
               print(i)
hobby=(1,2,3)
detail={"mehtab":"khan","pocket_money":50}
describe_person(*hobby,**detail)

    