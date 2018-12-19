def read_ids():
    ids = []
    for identifier in open('input.txt', 'r'):
        ids.append(identifier.strip())

    return ids


def similar(id1, id2):
    if len(id1) != len(id2):
        return False

    chars_different = 0

    for idx, char in enumerate(id1):
        if char != id2[idx]:
            chars_different += 1
            if chars_different > 1:
                return False
    return True


def compare_ids(ids):
    for i, id1 in enumerate(ids):
        for j, id2 in enumerate(ids):
            if i != j and similar(id1, id2):
                return id1, id2


def locate_box():
    ids = read_ids()
    id1, id2 = compare_ids(ids)
    print(''.join(id1))
    print(''.join(id2))
    return [char for char in id1 if char in id2]


print(''.join(locate_box()))
