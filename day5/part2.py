import string


def remove_pairs(input):
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
    return new_seq


def find_problematic_polymer(input):
    lengths = {}
    for letter in string.ascii_lowercase:
        new_input = input.replace(letter, '').replace(letter.upper(), '')
        old_len = len(input)
        new_len = old_len - 1
        new_seq = new_input
        while old_len > new_len > 0:
            old_len = new_len
            new_seq = remove_pairs(new_seq)
            new_len = len(new_seq)
        lengths[letter] = new_len

    problematic_polymer = min(lengths, key=lambda key: lengths.get(key))
    return problematic_polymer, lengths.get(problematic_polymer)


# input = 'dabAcCaCBAcCcaDA'
# condensed_input = find_problematic_polymer(input)
# print(condensed_input)
with open('input.txt', 'r') as input:
    condensed_input = find_problematic_polymer(input.readline())
    print(condensed_input)
