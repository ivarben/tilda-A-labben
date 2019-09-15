import math
import sys

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

def main():
    i = 0
    all_nodes = []
    all_pipes = []
    for row in sys.stdin:
        if i == 0:
            N = int(row)
        if i > 0 and i < N:
            rowlist = row.strip('\n').split(' ')
            pipe = Pipe(int(rowlist[0]), int(rowlist[1]), int(rowlist[2]), int(rowlist[3]))
            all_pipes.append(pipe)
        if i == N:
            rowlist = row.strip('\n').split(' ')
            for j in range(len(rowlist)):
                node = Node(j+1, int(rowlist[j]))
                all_nodes.append(node)
        i += 1
        if i > N:
            for pipe in all_pipes:
                for node in all_nodes:
                    if pipe.up == node.number:
                        pipe.up = node
                    if pipe.down == node.number:
                        pipe.down = node
            print(count(all_nodes[0], all_pipes))
            i = 0
            all_nodes = []
            all_pipes = []
if __name__ == "__main__":
    main()
