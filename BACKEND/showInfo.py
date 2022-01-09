from BACKEND.validation import isSaved
from BACKEND.standardizedEntries import standardEntries

def showExcerciseDescription(text):
    print("INDICACIÓN","INSTRUCCIONES")
    print("QUE DEBES HACER?", text['hacer'])
    print("QUE INFORMACIÓN TE BRINDA EL EJERCICIO?", text['info'])
    print("ENTRADAS", text['entrada'])
    print("SALIDAS", text['salida'])
    print("CONDICIONES", text['condiciones'])
    print("PSEUDOCÓDIGO", "Proximamente")
    print("\n\n")
    pass

def describe(text, saved_excercises):
    text = standardEntries(text)
    description = {
        'hacer': [],
        'info': [],
        'entrada': [],
        'salida': [],
        'condiciones': "descritas en la información que proporciona el texto del texto",
        'pseudocodigo': []
    }

    problemSaved = isSaved(text, saved_excercises)
    # #verificar si text esta almacenado en el CSV
    if problemSaved[0]: #The position [1] will store the index of the problem to analyze
        #asignación de descripción según campos
        excercise = problemSaved[1]
        print(saved_excercises[excercise][1])
        for hint in saved_excercises[excercise][1]:
            # print(hint)
            if hint[1] == 'hacer':
                description['hacer'].append(hint[0])
            elif hint[1] == 'condicion-info':
                description['info'].append(hint[0])
            elif hint[1] == 'entrada':
                description['entrada'].append(hint[0])
            elif hint[1] == 'salida':
                description['salida'].append(hint[0])
            elif hint[1] == 'pseudocodigo':
                description['pseudocodigo'].append(hint[0])
        # showExcerciseDescription(description)
        return description
    else:
        return None
        # raise ValueError("El ejercicio no se encuentra almaenado en el programa, por ende no puede ser analizado.\n\t"
        #                  "Te recomiendo que lo registres!!")
    pass



