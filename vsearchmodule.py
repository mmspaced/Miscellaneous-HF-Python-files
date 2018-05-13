def search_for_chars(phrase: str, characters: str) -> set:

    """ Function to search for the characters in a phrase, both passed as
        function arguments.  Return the characters found in the phrase.
        This is considered a docstring, which can span multiple lines

        Note the use of annotations, which are documentation standards,
        not enforcement mechanisms.  The type of data being passed back
        and forth is not considered by the interpreter. """

    return set(characters).intersection(set(phrase))

# word = input('Provide a word to search for vowels: ')
# search_for_vowels(word)


def double(arg):

    """ Call-by-Value function argument example.  If the function argument
        variable is mutable, then call-by-reference applies.  If the function
        argument is immutable (e.g., int, string, tuple), then call-by-value
        applies.  However, in the case of an assignment, the code to the
        right of the = symbol is executed first, and then whatever value is
        created has its object reference assigned to the variable on the left
        of the = symbol.  Executing the code arg * 2 creates a new value,
        which is assigned a new object reference, which is the assigned to the
        arg variable, overwriting the previous object reference stored in the
        arg in teh function's suite.  However, the old object reference still
        exists in the calling code and its value hasn't changed, so the shell
        still sees the original value that was passed into the function. """

    arg = arg * 2

    return arg


def change(initial, append_data):
    """ Call-by-Reference function argument example.  Note that there is no
        assignment here, so the behavior described above (int the case of a
        list) does not apply. Therefore, no new object reference is created,
        because no assignment is performed. """

    return initial.append(append_data)
