from collections import defaultdict
import string

NUMBER_OF_ELVES = 5
STEP_DURATION = 60
# NUMBER_OF_ELVES = 2
# STEP_DURATION = 0


class Tree:
    def __init__(self, name):
        self.name = name
        self.parents = {}
        self.children = {}
        self.time_remaining = self.step_duration()

    def __str__(self):
        return self.name

    def step_duration(self):
        return STEP_DURATION + 1 + string.ascii_uppercase.index(self.name)

    def __eq__(self, o):
        return self.name == o.name

    def __hash__(self) -> int:
        return self.name.__hash__()


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


def assign_work(elves_working, nodes_in_progress, tree):
    possible_options = set()
    for node in tree.values():
        if len(node.parents) == 0:
            possible_options.add(node)
    ordered_options = sorted(possible_options, key=lambda option: option.name)
    for elf in range(0, min(len(possible_options), NUMBER_OF_ELVES - elves_working)):
        elves_working += 1
        node = ordered_options[elf]
        nodes_in_progress.add(node)
        del (tree[node.name])
    return elves_working


def remove_node_from_tree(node_to_remove, tree):
    for node in tree.values():
        if node_to_remove.name in node.parents:
            del (node.parents[node_to_remove.name])
        if node_to_remove.name in node.children:
            del (node.children[node_to_remove.name])


def run():
    nodes_in_progress = set()
    elves_working = 0
    time_taken = 0
    nodes_processed = []
    tree = defaultdict(lambda: None)
    with open('input.txt', 'r') as input:
        for instruction in input:
            process_instruction(instruction, tree)
    number_of_instructions = len(tree)
    while len(nodes_processed) < number_of_instructions:
        # assign some work
        elves_working = assign_work(elves_working, nodes_in_progress, tree)

        # process node with smallest time remaining
        ordered_nodes = sorted(nodes_in_progress, key=lambda node: node.time_remaining)
        next_node = ordered_nodes.pop(0)
        nodes_in_progress.remove(next_node)
        time_to_finish_node = next_node.time_remaining
        time_taken += time_to_finish_node
        elves_working -= 1
        nodes_processed.append(next_node.name)
        remove_node_from_tree(next_node, tree)
        # adjust remaining time on other nodes
        for node in nodes_in_progress:
            node.time_remaining -= time_to_finish_node

    print(''.join(nodes_processed))
    print(time_taken)


run()
