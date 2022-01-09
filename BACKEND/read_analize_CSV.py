import csv

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

def standardized_csv(saved_excercises):
    #to_lower and analyze  all above
    for hint in saved_excercises[1:]:
        hint_index = saved_excercises.index(hint)
        for item in hint:
            item_index = hint.index(item)
            saved_excercises[hint_index][item_index] = toLowerString(saved_excercises[hint_index][item_index])
            saved_excercises[hint_index][item_index] = removeTildesaAndPunctuation(saved_excercises[hint_index][item_index])
        for hint in saved_excercises:
            if len(hint) == 0:
                saved_excercises.remove(hint)
    return saved_excercises

def searchInExcercises(itemToSearch, PlaceToSearch):
    for item in PlaceToSearch:
        if itemToSearch in item:
            return True
    return False

def indexItemAppended(itemToSearch, PlaceToSearch):
    index = 0
    for item in PlaceToSearch:
        if itemToSearch in item:
            index = PlaceToSearch.index(item)
            return index

def unifyContentByProblem(saved_excercises):
    unified_saved_excercises = []
    for item in saved_excercises[1:]:
        if '-' not in item:
            if searchInExcercises(item[0], unified_saved_excercises):
                itemAppendedIndex = indexItemAppended(item[0], unified_saved_excercises)
                unified_saved_excercises[itemAppendedIndex][1].append(item[1:])
            else:
                unified_saved_excercises.append([item[0],[]])
                itemAppendedIndex = indexItemAppended(item[0], unified_saved_excercises)
                unified_saved_excercises[itemAppendedIndex][1].append(item[1:])
    return unified_saved_excercises

#leyendo CSV para obtener información
def open_csv():
    saved_excercises = []
    with open("BACKEND/excercises.csv", encoding=("utf-8-sig")) as File:
        reader = csv.reader(File, delimiter=";")
        for row in reader:
            saved_excercises.append([item for item in row if item != ''])
    saved_excercises = standardized_csv(saved_excercises)
    std_saved_excercises = unifyContentByProblem(saved_excercises)

    # print("\n\n")
    print(std_saved_excercises)
    return std_saved_excercises

# open_csv()