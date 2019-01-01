from collections import namedtuple
test_input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
'NOC NOM NOC NOM MET MET EOC NOC NOM NOC NOM EOC MET MET EOC'
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


class Header:

    def __init__(self, parent, noc) -> None:
        self.parent = parent
        self.noc = noc
        self.nom = 0
        self.metadata = []
        self.children = []

    def calculate_value(self):
        if self.noc == 0:
            return sum(self.metadata)
        else:
            sums = []
            for m in self.metadata:
                try:
                    sums.append(self.children[m-1].calculate_value())
                except IndexError:
                    pass
            return sum(sums)

    def __repr__(self) -> str:
        return f'NOC: {self.noc} NOM: {self.nom} MET: {self.metadata} CHILDREN: \n{self.children}'


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
        raise RuntimeError

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


def label_nodes(input):
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

    return labelled


def build_tree(node, current_header):
    if node.type == 'NOC':
        current_header = Header(current_header, node.value)
    elif node.type == 'NOM':
        current_header.nom = node.value
    elif node.type == 'MET':
        current_header.metadata.append(node.value)
    elif node.type == 'EOC':
        current_header.metadata.append(node.value)
        current_header.parent.children.append(current_header)
        current_header = current_header.parent

    return current_header


def run(input):
    labelled = label_nodes(input)
    return sum([i.value for i in labelled if i.type == 'MET' or i.type == 'EOC'])


def run2(input):
    labelled = label_nodes(input)

    root = Header(None, 1)
    new_header = root
    for i, node in enumerate(labelled):
        new_header = build_tree(node, new_header)
        if i == 0:
            root.children.append(new_header)

    return root.children[0].calculate_value()


assert run(test_input6) is 22, 'test_input 6 failed'
assert run(test_input5) is 13, 'test_input 5 failed'
assert run(test_input4) is 3, 'test_input 4 failed'
assert run(test_input3) is 1, 'test_input 3 failed'
assert run(test_input2) is 26, 'test_input 2 failed'
assert run(test_input) is 138, 'test_input failed'
assert run2(test_input) is 66, 'test_input (run2) failed'

with open('input.txt', 'r') as input:
    line = next(input)
    print(run(line))
    print(run2(line))
