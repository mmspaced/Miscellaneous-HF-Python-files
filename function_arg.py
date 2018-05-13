
# A function that receives a function as an argument and returns
# the results of the function with the second argument passed to it.

def apply(func: object, value: object) -> object:
    return func(value)

length = apply(len,'123456')
print('String length is ', length)

obj_type = apply(type, '123456')
print('Argument type is', obj_type)

obj_type = apply(type, 12)
print('Argument type is', obj_type)

obj_type = apply(type, 12.3)
print('Argument type is', obj_type)

obj_type = apply(type, apply)
print('Argument type is', obj_type)

print()

# Inner functions

def outer() -> object:

    def inner():
        print('This is the inner function.')

    print('This is the outer function, invoking inner.')
    inner()

    print('This is the outer function, returning inner.')
    return inner

# Assign a reference to the inner function, which is returned by
# the outer function

inner_function_obj = outer()

print()

# Invoke the inner function through the reference
inner_function_obj()

print()

# Process a list (tuple) of arguments, without knowing how many
# exist in advance.  Think of * as meaning "expand to a list of values"

def multiargs(*args):
    for a in args:
        # Print all arguments on a single line by substituting a space for eol
        print(a, end=' ')
    # Now print eol
    if args:
        print()

multiargs()
multiargs(1)
multiargs(1, 1.2)
multiargs(1, 1.2, 'Mike')

# When  a lsit is prefixed with a '*', it expands to a list of individual
# arguments.

values = [23, 39, 43, 77, 122]
# This function invocation treats each element in the list as separate arguments
multiargs(*values)
# This function invocation treats the list as one argument
multiargs(values)

print()

# Use ** to accept arbitrary keyword arguments.
# Think of ** as "expand to a dictionary of keys and values"

def multikwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

multikwargs(a=10, b=20)
multikwargs()
multikwargs(a=10, b=20, c=30, d=40, e=50, f=60)

print()

# When a dictionary is prefixed by a '**', it tells the interpreter to treat
# dictionary as a collection of keys and their associated values

dict_values ={'first_name': 'Mike', 'last_name': 'Mitnick'}
multikwargs(**dict_values)

print()

# Accepting any number and type of regular function arguments and
# keyword function arguments

def multiargtypes(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()

multiargtypes(1.2, 1, 'Mike', name='George', occupation='appraiser', state='PA')








