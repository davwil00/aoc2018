def remove_pairs(input):
    print(len(input))
    new_seq = []
    it = iter(enumerate(input))
    for i, char in it:
        try:
            char2 = input[i+1]
        except IndexError:
            char2 = ''
        if char == char2:
            new_seq.append(char)
        elif str.lower(char) != str.lower(char2):
            new_seq.append(char)
        else:
            next(it)
    if len(new_seq) != len(input):
        return remove_pairs(new_seq)
    else:
        return new_seq


# input = 'dabAcCaCBAcCcaDA'
# input = 'XXABCDEedcbaXX'
# condensed_input = remove_pairs(input)
# print(len(condensed_input))
with open('input.txt', 'r') as input:
    condensed_input = remove_pairs(input.readline())
    print(len(condensed_input))
