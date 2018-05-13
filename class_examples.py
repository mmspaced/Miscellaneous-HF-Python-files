
class CountFromBy:

    # The Python convention for class vs. function naming is that a class
    # is named capitalized, CamelCase; whereas, a function is named using
    # all lowercase letters with underscores for emphasis

    # The use of self indicates that the code you're reading is a method,
    # as opposed to a function (when self is not used)
    # Whe you see self, think this object or an alias to the object

    # Prefix all attribute names with self

    # pass is Python's empty statement
    # pass

    # No matter where you use variables in Python, they must be initialized

    # The standard dunder methods, available to all classes, are known as
    # the magic methods.  You can override the standard behavior by providing
    # your own implementation of the dunder methods, as we are doing to
    # __init__ , which is essentially a constructor that initializes attributes
    # The argument defaults are initial value = 0 and increment = 1

    def __init__(self, v:int=0, i:int=1) -> None:
        self.value = v
        self.increment = i

    def __repr__(self) -> str:
        """ Convert the value attribute to a string and return it to caller"""
        return str(self.value)

    def increase(self) -> None:
        self.value += self.increment


number1 = CountFromBy(5, 4)

print('Object type =', type(number1))
print('Object id = ', id(number1))
print('Object id (hex) = ', hex(id(number1)))

# The print function BIF uses __repr__ to display specific contents of a
# specific object - in this case, the value attribute of the number1 object
# of the CountFromBy class
print('Object value =', number1)

print('value = ', number1.value)
number1.increase()
print('incremented number', number1.value)
number1.increase()
print('incremented number', number1.value)

print()

number2 = CountFromBy(12, 17)

print('Object type =', type(number2))
print('Object id = ', id(number2))
print('Object id (hex) = ', hex(id(number2)))

print('Object value =', number2)

print('value = ', number2.value)
number2.increase()
print('incremented number', number2.value)
number2.increase()
print('incremented number', number2.value)

print()

# Use the default arguments for initial value and increment
number3 = CountFromBy()

print('Object type =', type(number3))
print('Object id = ', id(number3))
print('Object id (hex) = ', hex(id(number3)))

print('Object value =', number3)

print('value = ', number3.value)
number3.increase()
print('incremented number', number3.value)
number3.increase()
print('incremented number', number3.value)