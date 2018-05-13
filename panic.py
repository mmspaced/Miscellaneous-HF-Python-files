phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# My version of how to manipulate "Don't panic!" to "on tap"

plist.remove('D')
plist.remove("'")
plist.remove(' ')
plist.insert(2, ' ')
plist.insert(4, 'a')

for i in range(5):
    plist.pop()

# The join() method returns a string concatenated with the elements of an
# iterable. If the iterable contains any non-string values, it raises a
# TypeError exception.
# The syntax of the join method is: string.join(iterable). Note that '' is
# the separator string.
# In this case, plist is the iterable, a list of single-character strings as
# elements. new_phrase is the concatenation of the single-character string
# elements in the list into a single string.  So, it essentially converts
# a list of strings into a single string.

print()
print("Result of manipulation of Don't panic! -- ", plist)
new_phrase = ''.join(plist)
print('Result of join() method to convert list of characters to string -- ', new_phrase)

print()

# The book's version of how to manipulate "Don't panic!" to "on tap"

plist = list(phrase)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

print(plist)
new_phrase = ''.join(plist)
print(new_phrase)

print()

# Accessing lists like arrays via bracket notation and individual elements

plist = list(phrase)

print("plist = ", plist)
print("plist[0] = ", plist[0])
print("plist[1] = ", plist[1])
print("plist[-1] = ", plist[-1])
print("plist[-2] = ", plist[-2])

# Using start, stop, and step with lists
# Note that the stop value is the index to stop at but not include

print()

print("plist[0:10:3] = ", plist[0:10:3])
print("plist[3:] = ", plist[3:])
print("plist[:10] = ", plist[:10])
print("plist[:12] = ", plist[:12])
print("plist[::2] = ", plist[::2])

print()

title = "The Hitchhiker's Guide to the Galaxy"

title_list = list(title)

print(title_list)
print(title_list[4:16])

# A slice is a fragment of a list

# List methods change the state of a list, whereas using square brackets and slices (typically) does not.

# This is the slice for the first word
first_word = ''.join(title_list[4:16])
print(first_word)


# This is the slice for the last word
last_word = ''.join(title_list[-6:])
print(last_word)

# This works for assertions used for debugging.  Assertions are removed via the -O command line flag

try:
    assert last_word == "Galaxy"
except AssertionError:
    print("Last word is not Galaxy!")



backwards = ''.join(title_list[::-1])
print(backwards)

everyother = ''.join(title_list[::2])
print(everyother)

print()

plist = list(phrase)
new_phrase_list = list(plist[1:3])

new_phrase_list.extend([plist[-7:-9:-1], plist[-5:-7:-1]])

print(new_phrase_list)

print()

# The following code generates an error, because the 2nd and 3rd indexed elements in new_phrase_list are actually
# lists themselves [' ', 't'] and ['a', 'p'], respectively.  The join method only works on a list that consists
# of strings, not lists

# new_phrase = ''.join(new_phrase_list)


# This code works, because it traverses the list one element at at time and appends to the string using the
# String join method, which - for an empty string - converts an iterable of characters into a string

new_phrase = ''

for character in range(len(new_phrase_list)):
    new_phrase = new_phrase + ''.join(new_phrase_list[character])

print(new_phrase)

print()

# This code also works, because it extracts the two list objects in elements 2 and 3 of the new_phrase_list
# and appends them as individual characters to the new_phrase_char_list by using the extend list method

new_phrase_char_list = new_phrase_list[:2]

list_in_list = new_phrase_list[2]
new_phrase_char_list.extend(list_in_list)

list_in_list = new_phrase_list[3]
new_phrase_char_list.extend(list_in_list)

new_phrase = ''.join(new_phrase_char_list)

print(new_phrase)

# for loop examples using slices

print()

paranoid_android = "Marvin, the Paranoid Android"

letters = list(paranoid_android)

for char in letters[:6]:
    print('\t', char)

for char in letters[-7:]:
    print('\t'*2, char)

for char in letters[12:20]:
    print ('\t'*3, char)









