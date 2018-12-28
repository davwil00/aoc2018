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

Label = namedtuple('Label', ['value', 'type'])


def classify(prv, val, noc, nom):
    new_noc = noc[-1]
    new_nom = nom[-1]
    if prv == 'NOC':
        label = 'NOM'
        nom.append(val)
    if prv == 'NOM':
        if new_noc == 0:
            label = 'MET'
            nom[-1] -= 1
            if nom[-1] == 0:
                nom.pop()
                if noc[-1] == 0:
                    noc.pop()
                    if len(noc) > 0:
                        noc[-1] -= 1
        else:
            label = 'NOC'
            noc.append(val)
    elif prv == 'MET':
        if new_nom > 0:
            label = 'MET'
            nom[-1] -= 1
            if nom[-1] == 0:
                nom.pop()
                if noc[-1] == 0:
                    noc.pop()
                    if len(noc) > 0:
                        noc[-1] -= 1
        else:
            if new_noc > 1:
                label = 'NOC'
                noc.append(val)
            else:
                label = 'MET'
                noc[-1] -= 1
                if (noc[-1]) == 0:
                    noc.pop()

    return label, noc, nom


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

    for i in labelled:
        print(str.format('{} {}', i.value, i.type))

    return sum([i.value for i in labelled if i.type == 'MET'])


# print(run(test_input6))
# assert run(test_input5) is 22, 'test_input 6 failed'
assert run(test_input5) is 13, 'test_input 5 failed'
assert run(test_input4) is 3, 'test_input 4 failed'
assert run(test_input3) is 1, 'test_input 3 failed'
# assert run(test_input2) is 26, 'test_input 2 failed'
# assert run(test_input) is 138, 'test_input failed'
#
