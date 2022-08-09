from platform import node

from matplotlib.pyplot import connect
import graph

node_num = 16
edge_num = 20

my_graph, my_edge_set = graph.generate_graph(node_num, edge_num)
print(my_edge_set)

connect_BFS = graph.breadth_first_search(6, my_graph)
print(connect_BFS)

connect_DFS = graph.depth_first_search(6, my_graph)
print(connect_DFS)

graph.illustrate_graph(my_edge_set)