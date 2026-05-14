import csv
import networkx as nx
import matplotlib.pyplot as plt

brands = []
models = []

with open("amazon_laptops.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        name = row['Product Name']
        if name != "Title not found":
            brands.append(name.split()[0].upper())
            models.append(name[:20] + "...")

G = nx.Graph()

for i in range(len(brands)):
    G.add_edge(brands[i], models[i])

plt.figure(figsize=(10, 8))

colors = []
for node in G.nodes():
    if node in brands:
        colors.append("lightcoral")
    else:
        colors.append("skyblue")

nx.draw(G, with_labels=True, node_color=colors, node_size=3000, font_size=8)
plt.title("Laptop Brands & Communities")
plt.show()