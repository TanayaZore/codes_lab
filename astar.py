import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue 
def astar(graph, start_node, target, hf):
    visited = set()
    pq=PriorityQueue()
    pq.put((0, start_node))

    while pq.empty()==False:
        current_node = pq.get()[1]
        if current_node not in visited:
            visited.add(current_node)
            print(current_node, end=" ")

        if current_node==target:
            return

        for v,c in graph[current_node]:
            if v not in visited:
                h=hf[v]
                h=int(h)
                c=int(c)
                c=c+h
                pq.put((c, v))

graph = {}
G = nx.Graph()
V = int(input("Enter the number of vertices:"))
E = int(input("Enter the number of edges: "))
hf={}
for i in range(E):
    u, v, cost, hef = input("Enter an edge (u, v) and cost and heuristic value: ").split()
    c=int(cost)
    h=int(hef)
    hf[u]=h
    G.add_edge(u, v, weight=c)
    if u not in graph:  # if u is not a key then assign it
        graph[u] = []
    if v not in graph:  # if v is not a key then assign it
        graph[v] = []
    graph[u].append((v,cost))  # undirected graph/tree so assigning both ways
    graph[v].append((u,cost))

start_node = input("Enter the starting node for A*: ")
target = input("Enter the target node for A*: ")
hf[target]=0
astar(graph, start_node, target, hf)
print()
elarge=[(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=elarge)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.show()
