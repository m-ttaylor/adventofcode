import random
from utils import aoc
import networkx as nx


data = aoc.getInput(2023, 25, False)

graph = nx.Graph()

keys = []
for line in data:
    key, r = line.split(":")
    keys.append(key)
    for n in r.strip().split(" "):
        graph.add_edge(key, n, capacity=1)

cut_value = float("inf")
while cut_value > 3:
    cut1 = random.choice(keys)
    cut2 = random.choice(keys)

    cut_value, partition = nx.minimum_cut(graph, cut1, cut2)

print(len(partition[0]) * len(partition[1]))
