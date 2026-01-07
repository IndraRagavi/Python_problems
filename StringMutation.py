# Mutate a string by replacing a specific index. One way to do is through slicing
def mutate_string(string, position, character):
    #lis = list(string)
    lis = string[:position]+character+string[position+1:]
    p = ''.join(lis)
    return p

s = 'abracadabra'
position = 5
character = 'k'
n = mutate_string(s,position,character)
print(n)
