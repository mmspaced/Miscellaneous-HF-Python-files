from vsearchmodule import search_for_chars, double, change

phrase = input('Provide a phrase: ')
characters = input('Provide characters for which to search in the phrase: ')

found = search_for_chars(phrase, characters)

if bool(found):
    print('Characters were found!')
    for character in found:
        print(character)
else:
    print('Sorry - no characters were found :(')

# Validation of pass by value for integer and float num passed as a function argument.  It is unchanged
# when checked after the function call.

num = 10
print('Before: num = ', num)
doubled_num = double(num)
print('After: num = ', num)

num = 10.7
print('Before: num = ', num)
doubled_num = double(num)
print('After: num = ', num)


# Validation of pass by reference for list numbers passed as a function argument.  It is unchanged
# when checked after the function call.

numbers = [42, 256, 16]
print('Before: numbers = ', numbers)
change(numbers, 'append data')
print('After: numbers = ', numbers)


