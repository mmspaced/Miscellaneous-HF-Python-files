vowels=['a','e','i','o','u']
word=input("Provide a word to search for vowels: ")

print()

# List implementation that indicates vowels found

found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
if len(found) != 0:
    for vowel in found:
        print(vowel)
else:
    print("No vowels in that word.")

print()

# Set implementation.  Note that sets don't allow duplicates.
# Convert vowels from a list to a set
vowels = set(vowels)

# Recognize how powerful the following line of code is...
found = vowels.intersection(set(word))

if len(found) != 0:
    for vowel in found:
        print(vowel)
else:
    print("No vowels in that word.")

print()

# Convert vowels from a set back to a list
vowels = list(vowels)

# Dictionary implementation that indicates vowels found and frequency count

found = {}

# The following code is no longer needed due to use of the setdefault method on the found dictionary
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0

for letter in word:
    if letter in vowels:

        # This eliminates the need to initialize the dictionary
        # Note that the setdefault method initializes a non existing key (letter) and optionally
        # initializes the value of that key to a default (0).  If the key already exists, setdefault
        # will do nothing.
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

# Create a tuple of vowels.  This is appropriate, as vowels comprise a finite set of 5 letters
vowels2 = ('a','e','i','o','u')

# Every tuple needs to include a least one comma to differentiate it from a string

# This is a string
last_name = ('Bon Jovi')
print()
print(type(last_name))

# But this is a tuple
last_name_of_rock_star_Jon = ('Bon Jovi',)
print()
print(type(last_name_of_rock_star_Jon))


