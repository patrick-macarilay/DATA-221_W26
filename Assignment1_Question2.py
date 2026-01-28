# Nested Dictionary from Strings

def dict_from_strings(listOfStrings):
    dictionary = {}
    for string in listOfStrings:
        dictionary[string]
        
        letters = len(string)
        dictionary['length'] = letters
        if letters % 2 == 0:
            dictionary['parity'] = 'even'
        else:
            dictionary['parity'] = 'odd'
            return dictionary

print(dict_from_strings(['data', 'science']))