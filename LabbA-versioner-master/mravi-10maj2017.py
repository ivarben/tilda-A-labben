import math

class Node:
    def __init__(self, number, need):
        self.up = None
        self.down = None
        self.number = number
        self.need = need

class Pipe:
    def __init__(self, up, down, percentage, superpower):
        self.up = up
        self.down = down
        self.fraction = percentage/100
        self.superpower = superpower

def count(root, all_pipes):
    if root.need != -1:
        return root.need
    pipes_down = []
    possible_needs = []
    for pipe in all_pipes:
        if pipe.up == root:
            pipes_down.append(pipe)
    for pipe in pipes_down:
        if pipe.superpower == 1:
            possible_needs.append(math.sqrt(count(pipe.down, all_pipes))/pipe.fraction)
        else:
            possible_needs.append(count(pipe.down, all_pipes)/pipe.fraction)
    return max(possible_needs)

#TEST
all_nodes = []
all_pipes = []

needs = [-1, -1, 1, -1, 1, 2]

pipe_ups = [1, 2, 2, 2, 4]
pipe_downs = [2, 3, 4, 5, 6]
percentages = [100, 20, 20, 60, 100]
superpowers = [1, 0, 0, 0, 1]

for i in range(1,7):
    node = Node(i, needs[i-1])
    all_nodes.append(node)

for i in range(1,6):
    pipe = Pipe(pipe_ups[i-1], pipe_downs[i-1], percentages[i-1], superpowers[i-1])
    all_pipes.append(pipe)

for pipe in all_pipes:
    for node in all_nodes:
        if pipe.up == node.number:
            pipe.up = node
        if pipe.down == node.number:
            pipe.down = node

print(count(all_nodes[0], all_pipes))
