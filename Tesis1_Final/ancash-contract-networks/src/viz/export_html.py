import pandas as pd
import networkx as nx
import json
from flask import render_template

def export_network_to_html(network, year):
    # Create a bipartite graph from the network data
    B = nx.Graph()
    
    # Add nodes for Ancash
    B.add_node('Ancash', bipartite=0)
    
    # Add nodes for each company and edges based on contracts
    for company in network['companies']:
        B.add_node(company, bipartite=1)
        B.add_edge('Ancash', company, weight=network['contract_count'][company])
    
    # Generate the HTML visualization
    network_data = nx.node_link_data(B)
    
    # Render the HTML template with the network data
    html_output = render_template('network_template.html', network_data=json.dumps(network_data), year=year)
    
    # Save the output to an HTML file
    with open(f'networks_{year}.html', 'w') as f:
        f.write(html_output)