import pandas as pd
import networkx as nx
import csv


def build_shortest_path():
    # Read the CSV file
    df = pd.read_csv('Network_Database/AdjMatrix.csv')

    # Initialize a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for index, row in df.iterrows():
        city = row['City']
        G.add_node(city)
        for i in range(1, 7):
            connection = row[f'Connection {i}']
            distance = row[f'Distance {i}']
            if pd.notna(connection):
                G.add_edge(city, connection, weight=float(distance))

    # Initialize an empty dictionary to store shortest paths
    shortest_paths = {}

    # Run Dijkstra's algorithm for each node
    for node in G.nodes:
        shortest_paths[node] = nx.single_source_dijkstra_path(G, node)

    # Write shortest paths to a CSV file
    with open('Network_Database/shortest_paths.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['From', 'To', 'Path', 'Distance'])
        # Write shortest paths
        for source, paths in shortest_paths.items():
            for target, path in paths.items():
                if source != target:  # Exclude self-loops
                    distance = nx.shortest_path_length(G, source, target, weight='weight')
                    writer.writerow([source, target, ' -> '.join(path), distance])

build_shortest_path()