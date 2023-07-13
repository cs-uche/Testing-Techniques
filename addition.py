#!/usr/bin/env python3
# import pdb; pdb.set_trace()


def add_number(x, y):
    """This is a basic function that sums 2 digits
    debugging with pdb(python debugger)

    h - displays some helpful commands, some of which are
    n - takes us to the next line of code
    x - shows us what is in the variable x
    y - likewise displays content of variable y
    result - displays contents of var result
    exit() - exits the debugger

    The debugger can also perform expressions the same way any python terminal would
    """

    print(f"This is x: {x} of type {type(x)} and this is y: {y} of type {type(y)}\n")

    # breakpoint()
    try:
        result = x + y
    except TypeError as exception:
        print("The wrong type was passed")
        print("Exception:", exception)
    try:
        result = int(x) + int(y)
    except ValueError as e:
        print("\nOne of the variables is not a number")
        print("Exception:", e)
        result = "error"

    print(f"\nThis is the result:{result}")
    return result


add_number("one", 2)
