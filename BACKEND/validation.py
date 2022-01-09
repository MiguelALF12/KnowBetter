def isSaved(excercise, saved_excercises):

    flag = False
    excercise_index = None

    for item in saved_excercises:
        if item[0] == excercise:
            flag = True
            excercise_index = saved_excercises.index(item)
            return [flag,excercise_index]
    return [flag, excercise_index]


