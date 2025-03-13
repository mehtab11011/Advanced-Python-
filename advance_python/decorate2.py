# Counts how many times a function is called
# Logs the function name, arguments (*args, **kwargs), and return value
# Prints the execution time of the function
# # Expected Behavior:
import time  # Import time module to measure execution time

# Decorator function
def advanced_logger(fun):
    fun.count = 0  # Initialize function call count

    def wrapper(*args, **kwargs):
        fun.count += 1  # Increase count each time the function is called

        print(f"\nFunction: {fun.__name__} | Call count: {fun.count}")  # Print function name and count
        print(f"Arguments: {args}, {kwargs}")  # Print passed arguments

        start_time = time.time()  # Record start time before execution
        result = fun(*args, **kwargs)  # Execute the original function
        end_time = time.time()  # Record end time after execution

        execution_time = end_time - start_time  # Calculate execution time
        print(f"Return Value: {result}")  # Print function return value
        print(f"Execution Time: {execution_time:.6f} seconds")  # Print execution time

        return result  # Return the result to maintain original function behavior

    return wrapper  # Return the decorated function

# Example function to demonstrate the decorator
@advanced_logger
def add_numbers(a, b):
    return a + b  # Simple addition function

# Calling the function multiple times
add_numbers(3, 5)
add_numbers(10, 20)
add_numbers(100, 200)
