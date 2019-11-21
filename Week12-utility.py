def PrintOutput(string):
    output = print('OUTPUT '+str(string))

    
def LoadFile(file):
    f = open(file, 'r')
    lines = f.read().splitlines()
    print('Output'+str(lines))


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
            
PrintOutput('hi')
LoadFile("C:/Users/casey/csci102-week_12/README.md")
UpdateString('hello there', 'ye', 4)
