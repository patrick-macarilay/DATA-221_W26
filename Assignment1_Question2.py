# Nested Dictionary from Strings

def stringInfo(listOfStrings):
    result = {}

    for string in listOfStrings:
        length = len(string)

        if length % 2 == 0:
            parity = 'even'
        else:
            parity = 'odd'

        result[string] = {
            'length': length,
            'parity': parity
        }

    return result

print(stringInfo(['data','science']))
