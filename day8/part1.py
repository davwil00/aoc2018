from collections import namedtuple
test_input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
'NOC NOM NOC NOM MET MET MET NOC NOM NOC NOM MET MET MET MET'
# 2 3 1 1 2
# 0 3 10 11 12
# 1 1 2
# 0 1 99

test_input2 = '2 3 1 3 0 1 1 3 4 5 0 1 2 5 4 2'  # NOC NOM NOC NOM NOC NOM MET MET MET MET NOC NOM MET MET MET MET
#2 3 5 4 2
#1 3 3 4 5
#0 1 1
#0 1 2

test_input3 = '0 1 1'
test_input4 = '0 2 1 2'
test_input5 = '1 1 0 1 9 4'  # NOC NOM NOC NOM MET MET ## 1 1 9 # 0 1 4
test_input6 = '2 1 0 1 9 0 2 4 5 4'  # NOC NOM NOC NOM MET NOC NOM MET MET MET ## 2 1 4 # 0 1 9 # 0 2 4 5
#                 |     |       |
# i label noc nom
# 2 NOC [2] []
# 1 NOM [2] [1]

# 0 NOC [2 0] [1] x
# 1 NOM [2 0] [1 1] x
# 9 EOC [1] [1]
# 0 NOC [1 0] []
# 2 NOM [1 0] [1 2]
# 4 MET [1 0] [1 1]
# 5 EOC [0] [1]
# 4 EOC [0] [0] <---

Label = namedtuple('Label', ['value', 'type'])


def classify(prv, val, noc, nom):
    if noc[-1] == 0 and len(noc) == 1:
        label = 'MET'
        nom[-1] -= 1
    elif prv == 'NOC':
        label = 'NOM'
        nom.append(val)
    elif prv == 'NOM':
        if noc[-1] == 0:
            label = process_metadata(noc, nom)
        else:
            label = 'NOC'
            noc.append(val)
    elif prv == 'MET':
        # next can be met or noc
        if len(nom) > 0 and nom[-1] > 0:
            label = process_metadata(noc, nom)
        else:
            label = 'NOC'
            noc.append(val)
    elif prv == 'EOC':
        if noc[-1] > 0:
            label = 'NOC'
            noc.append(val)
        else:
            label = process_metadata(noc, nom)
    else:
        print('OOPS')

    return label, noc, nom


def process_metadata(noc, nom):
    if nom[-1] == 1:
        nom.pop()
        if noc[-1] == 0:
            noc.pop()
            noc[-1] -= 1
        return 'EOC'
    else:
        nom[-1] -= 1
        return 'MET'


def run(input):
    labelled = []
    input_iter = iter([int(e) for e in input.split(' ')])
    prv = 'NOM'
    noc = [next(input_iter)]
    nom = [next(input_iter)]

    labelled.append(Label(noc[0], 'NOC'))
    labelled.append(Label(nom[0], 'NOM'))

    for i in input_iter:
        (label, noc, nom) = classify(prv, i, noc, nom)
        labelled.append(Label(i, label))
        prv = label
        # print(str.format('{} {} {}, {}', i, label, noc, nom))

    # for i in labelled:
    #     print(str.format('{} {}', i.value, i.type))

    return sum([i.value for i in labelled if i.type == 'MET' or i.type == 'EOC'])


assert run(test_input6) is 22, 'test_input 6 failed'
assert run(test_input5) is 13, 'test_input 5 failed'
assert run(test_input4) is 3, 'test_input 4 failed'
assert run(test_input3) is 1, 'test_input 3 failed'
assert run(test_input2) is 26, 'test_input 2 failed'
assert run(test_input) is 138, 'test_input failed'

with open('input.txt', 'r') as input:
    print(run(next(input)))
