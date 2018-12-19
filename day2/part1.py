def group_letters(identifier):
    grouped_letters = {}
    for char in identifier:
        if char in grouped_letters:
            grouped_letters[char] += 1
        else:
            grouped_letters[char] = 1
    return grouped_letters


def count_doubles_and_triples(grouped_letters_list):
    twos = 0
    threes = 0
    for grouped_letters in grouped_letters_list:
        two_counted = False
        three_counted = False
        for key in grouped_letters.keys():
            if grouped_letters[key] == 2 and not two_counted:
                twos += 1
                two_counted = True
            elif grouped_letters[key] == 3 and not three_counted:
                threes += 1
                three_counted = True

    return twos, threes


def read_ids():
    ids = []
    for identifier in open('input.txt', 'r'):
        ids.append(identifier)

    return ids


def calculate_checksum():
    ids = read_ids()
    grouped_letters_list = []
    for identifier in ids:
        grouped_letters_list.append(group_letters(identifier))
    (twos, threes) = count_doubles_and_triples(grouped_letters_list)
    return twos * threes


print(calculate_checksum())
