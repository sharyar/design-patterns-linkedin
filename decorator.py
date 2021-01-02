from functools import wraps

def make_blink(function):
    '''Defines the decorator'''
    
    #This makes the decorator transparent in terms of its name and docstring. 
    @wraps(function)
    
    # Define the inner function
    def decorator():
        # grab the return value of the function being decorated
        ret = function()
        
        # Add new functionality to the function being decorated. 
        return "<blink>" + ret + "</blink>"
    return decorator

# Apply the decorator
@make_blink
def hello_world():
    '''Original Function'''
    return 'Hello World!'

# Check result of original function
print(hello_world())

# Check if function name is still the name of the function being decorated
print(hello_world.__name__)


# check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)