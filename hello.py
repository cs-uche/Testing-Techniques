def add_number(x,y):
    import pdb; pdb.set_trace()
    '''This is a basic function that sums 2 digits'''
    # debugging with pdb(python debugger)
    '''
    We use pdb as a normal debugger we
    n - takes us to the next line of code
    x - shows us what is in the variable x
    y - likewise displays content of variable y
    result - displays contents of var result
    exit() - exits the debugger

    We can also perform expressions in the debugger as we would in any python terminal
    '''
    print(f"This is x:{x} of type {type(x)} and this is y:{y} of type {type(y)}")

    try:
        result = x+y
    except TypeError as exception:
        print(f"The wrong type was passed in {exception}")
        result = int(x)+int(y)

    print(f"This is the reuslt:{result}")
    return result

print(add_number("one",2))


# def add_number(x,y):
#     '''This is a basic function that sums 2 digits'''
#     # debugging with print
#     print(f"This is x:{x} of type {type(x)} and this is y:{y} of type {type(y)}")

#     try:
#         result = x+y
#     except TypeError as exception:
#         print(f"The wrong type was passed in {exception}")
#         result = int(x)+int(y)

#     print(f"This is the reuslt:{result}")
#     return result

# print(add_number("1",2))

