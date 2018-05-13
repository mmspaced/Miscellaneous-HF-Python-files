from vsearch import search_for_characters

phrase = input('Provide a phrase: ')
characters = input('Provide characters for which to search in the phrase: ')

found = search_for_characters(phrase, characters)

if bool(found) :
    print('Characters were found!')
    for character in found :
        print(character)
else :
    print('Sorry - no characters were found :(')

