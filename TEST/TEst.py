import networkx as nx
import matplotlib as plt

network = nx.Graph()
network.add_nodes_from([1,2,3,4,5])
print(f"This is network has now {network.number_of_nodes()} nodes.")

edges = [
    (1,2),(2,3),(3,4),
    (4,5)

]

pos = {
    1:(0,1),
    2:(0.950,0.309),
    3:(0.580, -0.809),
    4:(-0.580, -0.809),
    5:(-0.950,0.309),
}
network.add_edges_from(edges)

color_list = ["gold","grey","red","blue","orange"]

plt.figure(figsize=(8,8))
plt.title('Final graph',size=10)

nx.draw(network,node_color=color_list,with_labels=True)

plt.axis('equal')
plt.show()