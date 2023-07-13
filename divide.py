#!/usr/bin/env python3


def divide_number(x, y):
    """This is a basic function that mulitplies 2 digits"""
    # debugging with print

    try:
        try:
            x = int(x)
        except ValueError as e:
            print("x is not a number")
            print("Exception:", e)

        try:
            y = int(y)
        except ValueError as e:
            print("y is not a number")
            print("Exception:", e)

        result = int(x / y)

    except TypeError:
        print("\nThe wrong type was passed")
        result = "error"

    print(f"\nThis is the result: {result}")
    return result


divide_number("one", 2)
