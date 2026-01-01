import networkx as nx
import json

G = nx.read_graphml("25_12_31_arbol_mat_uy_layout.graphml")

# Ensure numeric positions
for n, d in G.nodes(data=True):
    d["x"] = float(d.get("x", 0))
    d["y"] = float(d.get("y", 0))
    d["size"] = 1

# Compute degree
degrees = dict(G.degree())
nx.set_node_attributes(G, degrees, "degree")

data = {
    "nodes": [
        {
            "id": n,
            "label": d.get("label", n),
            "x": d["x"],
            "y": d["y"],
            "size": 1 + 0.3 * d["degree"],
            "degree": d["degree"]
        }
        for n, d in G.nodes(data=True)
    ],
    "edges": [
        {
            "id": f"e{i}",
            "source": u,
            "target": v
        }
        for i, (u, v) in enumerate(G.edges())
    ]
}

with open("25_12_31_arbol_mat_uy_layout.json", "w") as f:
    json.dump(data, f)

