from curses import start_color
import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def generate_graph(n, m):        # n:node, m:edge
    graph = [ [0]*n for i in range(n)]
    edge_set = set()

    while len(edge_set) < m:
        i, j = random.sample(range(n), 2)
        if i > j: i, j = j, i
        edge_set.add((i,j))
        graph[i][j] = graph[j][i] = 1
    return graph, edge_set

def illustrate_graph(edge_set):  
    obj = nx.Graph()
    for es in edge_set:
        obj.add_edge(es[0], es[1])
    plt.figure()
    nx.draw_networkx(obj)
    plt.show()

def breadth_first_search(start, W):
    work_queue = deque([])
    visited = set()
    work_queue.append(start)
    visited.add(start)

    while work_queue:
        hear = work_queue.popleft()
        for i, node in enumerate(W[hear]):
            if node == 0:
                continue
            if i not in visited:
                work_queue.append(i)
                visited.add(i)
    return visited


def depth_first_search(start, W):
    work_stack = []
    visited = set()
    work_stack.append(start)
    visited.add(start)

    while work_stack:
        hear = work_stack.pop()
        for i, node in enumerate(W[hear]):
            if node == 0:
                continue
            if i not in visited:
                work_stack.append(i)
                visited.add(i)
    return visited