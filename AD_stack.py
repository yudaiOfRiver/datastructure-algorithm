from platform import node
import random


# genarate a graph
def generate_graph(n,m):
    """ n nodes, m edges """
    graph_data = [[0] * n for i in range(n)]
    edge_set = set()
    while len(edge_set) < m:
        i,j = random.sample(range(n), 2)
        if i > j: i, j = j, 1
        edge_set.add((i,j))
        graph_data[i][j] = graph_data[j][i] = 1
    return graph_data, edge_set

# search with stack
def depth_first_search(start, W):
    work_stack = []
    visited = set()
    work_stack.append(start)
    visited.add(start)
    while work_stack:
        hear = work_stack.pop()
        for i, nodes in enumerate(W[hear]):
            if nodes == 0:
                continue
            if i not in visited:
                work_stack.append(i)
                visited.add(i)
    return visited

random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)
#print(my_graph)
#print(edge_set)

print(depth_first_search(1, my_graph))