# Task 4: Function that prints a shirt's size and the message printed on it

def make_shirt(size, message):
    """Print a sentence summarizing the shirt size and the message on it."""
    print(f"The shirt is size {size} and has the message: '{message}'")

# Call the function using positional arguments (size, message)
make_shirt("large", "Hello World")

# Call the function using keyword arguments
make_shirt(size="medium", message="Python is awesome")
