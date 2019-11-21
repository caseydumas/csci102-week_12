def PrintOutput(string):
    output = print('OUTPUT '+str(string))

    
def LoadFile(file):
    f = open(file, 'r')
    lines = f.read().splitlines()
    print('OUTPUT'+str(lines))


def UpdateString(string_one, string_two, index):
    string_one_list = list(string_one)
    string_one_list[index] = string_two
    joined_string = ''.join(string_one_list)
    print(joined_string)

def FindWordCount(input_list, input_string):
    count = 0
    for i in input_list:
        if input_list[i] == input_string:
            count += 1
    return count
def ScoreFinder(list_one, list_two, input_string):
    for i in list_one:
        if list_one[i] == input_string:
            score = list_two[i]
            print('OUPUT '+input_string+' got a score of '+str(score))
    if input_string not in list_one:
        print('OUTPUT player not found')
    
def Union(list_one, list_two):
    union_list = []
    for i in list_one:
        if list_one[i] not in list_two:
            union_list.append(list_one[i])
    for i in list_two:
        if list_two[i] not in list_one:
            union_list.append(list_two[i])
    return union_list

def Intersections(list_one, list_two):
    intersection_list = []
    for i in list_one:
        if list_one[i] in list_two:
            intersection_list.append(list_one[i])
    return intersection_list


PrintOutput()
LoadFile()
UpdateString()
FindWordCount()
ScoreFinder()
Union()
Intersections()
