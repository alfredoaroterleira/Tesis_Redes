import pandas as pd
import networkx as nx

def build_bipartite_network(df):
    # Create a bipartite graph
    B = nx.Graph()
    
    # Add nodes for Ancash (as a single node)
    B.add_node('Ancash', bipartite=0)
    
    # Add nodes for each company and edges based on contracts
    for year in df['year'].unique():
        year_data = df[df['year'] == year]
        for _, row in year_data.iterrows():
            companies = row['RUC'] if isinstance(row['RUC'], list) else [row['RUC']]
            for company in companies:
                B.add_node(company, bipartite=1)
                B.add_edge('Ancash', company)
    
    return B

def process_data(file_path):
    # Load the data
    df = pd.read_excel(file_path)
    
    # Process the data to extract relevant columns and years
    df['year'] = pd.to_datetime(df['fecha_contrato']).dt.year
    df = df[['year', 'RUC']]  # Adjust based on actual column names
    df = df.dropna()  # Handle missing values
    
    return df

def main():
    file_path = 'data/raw/contratos_ancash_all.xlsx'
    df = process_data(file_path)
    bipartite_network = build_bipartite_network(df)
    
    # Save or return the network for further analysis
    return bipartite_network

if __name__ == "__main__":
    main()