def search_for_characters(phrase:str, characters:str) -> set:

    """ Function to search for the characters in a phrase, both passed as function arguments.
        Return the characters found in the phrase.
        This is considered a docstring, which can span muliple lines

        Note the use of annotations, which are documentation standards, not enforcement mechanisms.
        The type of data being passed back and forth is not considered by the interpreter.  """

    return set(characters).intersection(set(phrase))

# word = input('Provide a word to search for vowels: ')

# search_for_vowels(word)