# Class Definition
class TestClass:
    def __init__(self):
        """Class definition."""

        # Class definitions, like function definitions (def statements) must be executed before they
        # have any effect. (You could conceivably place a class definition in a branch of an if
        # statement, or inside a function.)

        class GreetingClass:
            """Example of the class definition
            This class contains two public methods and doesn't contain a constructor.
            """
            name = 'Billy'

            def say_hello(self):
                """Class method."""
                # The self parameter is a reference to the class itself and is used to access variables
                # that belong to the class. It does not have to be named self; you can call it
                # whatever you like, but it has to be the first parameter of any function in the class.
                return 'Hello ' + self.name

            def say_goodbye(self):
                """Class method."""
                return 'Goodbye ' + self.name

        # Class instantiation uses function notation. Just pretend that the class object is a
        # parameterless function that returns a new instance of the class. For example, the following
        # code will create a new instance of the class and assign this object to the local variable.
        greeter = GreetingClass()

        assert greeter.say_hello() == 'Hello Billy'
        assert greeter.say_goodbye() == 'Goodbye Billy'

# Define a variable named 'content' with a value
content = "Some content"

# Now you can print its type
print(type(content))

# Standalone class definition
class GreetingClass:
    """Example of the class definition
    This class contains two public methods and doesn't contain a constructor.
    """
    name = 'Bisrat'

    def say_hello(self):
        """Class method."""
        # The self parameter is a reference to the class itself, and is used to access variables
        # that belong to the class. It does not have to be named self; you can call it
        # whatever you like, but it has to be the first parameter of any function in the class.
        return 'Hello ' + self.name

    def say_goodbye(self):
        """Class method."""
        return 'Goodbye ' + self.name

# Class instantiation for the standalone class
greeter = GreetingClass()

assert greeter.say_hello() == 'Hello Bisrat'
assert greeter.say_goodbye() == 'Goodbye Bisrat'

# Print the type of 'content'
print(type(content))

#!===============================================================================
# ===
    #!Instance Object
def test_instance_objects():
    # DATA ATTRIBUTES need not be declared; like local variables, they spring into existence when
    # they are first assigned to. For example, if x is the instance of MyCounter created above,
    # the following piece of code will print the value 16, without leaving a trace.

    # pylint: disable=too-few-public-methods
    class DummyClass:
        pass

    dummy_instance = DummyClass()

    # pylint: disable=attribute-defined-outside-init
    dummy_instance.temporary_attribute = 1
    assert dummy_instance.temporary_attribute == 1
    del dummy_instance.temporary_attribute
    #!============================================================
 


    #!===============================================================
from functools import wraps

def spam(repeats):
    # This is the outer decorator function. It takes the number of repeats as a parameter.
    def decorator(func):
        # This is the inner decorator function. It takes the function to be decorated as a parameter.
        @wraps(func)
        # The wraps decorator is used to update the wrapper function to look more like the original function.
        def wrapper(*args, **kwargs):
            # This is the wrapper function. It will be called instead of the original function.
            # It repeats the original function call according to the specified number of repeats.
            for i in range(repeats):
                func(*args, **kwargs)
        # The inner decorator returns the wrapper function.
        return wrapper
    # The outer decorator returns the inner decorator.
    return decorator

# The @spam(11) syntax is a shorthand for calling spam(11) and then using the result as a decorator for the function.
@spam(11)
def talk(word):
    """talk docstring"""
    # This is the original function. It prints the specified word.
    print(word)

# Calling the decorated function.
talk("Hello")

