def calculate_degree_centrality(G):
    """Calculate degree centrality for each node in the graph."""
    return dict(G.degree())

def calculate_betweenness_centrality(G):
    """Calculate betweenness centrality for each node in the graph."""
    return nx.betweenness_centrality(G)

def calculate_closeness_centrality(G):
    """Calculate closeness centrality for each node in the graph."""
    return nx.closeness_centrality(G)

def calculate_density(G):
    """Calculate the density of the graph."""
    return nx.density(G)

def get_top_n_nodes(centrality_dict, n=5):
    """Get the top N nodes based on centrality measures."""
    return sorted(centrality_dict.items(), key=lambda x: x[1], reverse=True)[:n]