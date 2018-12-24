from collections import defaultdict


class Tree:
    def __init__(self, name):
        self.name = name
        self.parents = {}
        self.children = {}

    def __str__(self):
        return self.name


def process_instruction(instruction, tree):
    before_step = instruction[5]
    after_step = instruction[36]
    before_node = get_or_default(tree, before_step)
    after_node = get_or_default(tree, after_step)
    after_node.parents[before_step] = before_node
    before_node.children[after_step] = after_node


def get_or_default(tree, node_to_find):
    node = tree[node_to_find]
    if node is None:
        node = Tree(node_to_find)
        tree[node_to_find] = node
    return node


def run():
    node_order = []
    tree = defaultdict(lambda: None)
    with open('input.txt', 'r') as input:
        for instruction in input:
            process_instruction(instruction, tree)

    while len(tree) > 0:
        possible_options = []
        for node in tree.items():
            if len(node[1].parents) == 0:
                possible_options.append(node[0])

        possible_options.sort()
        next_node = possible_options[0]
        node_order.append(next_node)
        del(tree[next_node])
        for node in tree.values():
            if next_node in node.parents:
                del(node.parents[next_node])
            if next_node in node.children:
                del(node.children[next_node])
    print(''.join(node_order))


run()
