# Task 5: make_shirt() with default size 'large' and default message 'I love Python'

def make_shirt(size="large", message="I love Python"):
    """Print a sentence summarizing the shirt size and the message on it.
    Defaults to a large shirt with the message 'I love Python' if not specified.
    """
    print(f"The shirt is size {size} and has the message: '{message}'")

# Make a large shirt using the default size and default message
make_shirt()

# Make a medium shirt using the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="Code is life")
