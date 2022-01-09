
def toLowerString(hint):
    newHint = ""
    for char in hint:
        newHint += char.lower()
    return newHint

def removeTildesaAndPunctuation(hint):
    tildes = ['á','é', 'í', 'ó','ú']
    tildes_change = ['a','e', 'i', 'o','u']
    symbols_to_avoid = ['#', '$', '%', '^', '*', '@', '(', ')', '.', ',', '/', '[', ']', '{', '}', '<', '>', ':', ';']
    newHint = ""

    for char in hint:
        if char in tildes:
            tildes_index = tildes.index(char)
            newHint += tildes_change[tildes_index]
        elif char in symbols_to_avoid:
            newHint += ''
        else:
            newHint += char
    return newHint


def standardEntries(text):
    text = toLowerString(text)
    new_text = removeTildesaAndPunctuation(text)
    return new_text




