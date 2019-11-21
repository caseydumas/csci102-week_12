def PrintOutput(string):
    output = print('OUTPUT '+str(string))
def LoadFile(file):
    f = open(file, 'r')
    lines = f.readlines()
PrintOutput()
LoadFile()
