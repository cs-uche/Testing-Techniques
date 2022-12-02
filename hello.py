def add_number(x,y):
    '''This is a basic function that sums 2 digits'''
    # debuggins with print
    print(f"This is x:{x} of type {type(x)} and this is y:{y} of type {type(y)}")

    try:
        result = x+y
    except TypeError as exception:
        print(f"The wrong type was passed in {exception}")
        result = int(x)+int(y)

    print(f"This is the reuslt:{result}")
    return result

print(add_number("1",2))



# def add_number(x,y):
#     '''This is a basic function that sums 2 digits'''
#     # debuggins with print
#     print(f"This is x:{x} and this is y:{y}")
#     result = x+y
#     print(f"This is the reuslt:{result}")
#     return result

# print(add_number(1,2))