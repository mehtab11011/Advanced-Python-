# Write a function order_food that takes a required restaurant_name argument,
# any number of dishes as *args, and additional details like delivery time as **kwargs.
# Print the details of the order.

def order_food(restaurant_name,*dishes,**additional_inform):
    print("restrunet name:",restaurant_name)
    print("dishes")
    for dish in dishes:
        print(f"{dish}")
        
    print("additional inform")
    for keys,values in additional_inform.items():
        print(f"{keys},{values}")

dishes=("mango","kabab","food_only")
add_inform={"payment_method":"online","discount":"50%"}
order_food("mk restrunent",*dishes,**add_inform)



# Write a function filter_even_numbers that accepts any 
# number of arguments, filters the even numbers, and returns them as a list.

def filter_even_numbers(*args):
    even_numbers = [num for num in args if isinstance(num,int)  and num % 2 == 0]
    return even_numbers
print(filter_even_numbers(1, 2, 3, 4, 5, 6))
# Output: [2, 4, 6]  # This is the expected output.