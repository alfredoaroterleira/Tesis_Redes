import pytest
from src.networks.build_bipartite import build_bipartite_network

def test_build_bipartite_network():
    # Sample data for testing
    sample_data = {
        'year': [2021, 2021, 2022, 2022],
        'empresa': ['Empresa A', 'Empresa B', 'Empresa A', 'Empresa C'],
        'contrato_id': [1, 2, 3, 4]
    }
    
    # Expected output structure
    expected_output = {
        'nodes': [
            {'id': 'Ancash', 'type': 'region'},
            {'id': 'Empresa A', 'type': 'empresa'},
            {'id': 'Empresa B', 'type': 'empresa'},
            {'id': 'Empresa C', 'type': 'empresa'}
        ],
        'edges': [
            {'from': 'Ancash', 'to': 'Empresa A'},
            {'from': 'Ancash', 'to': 'Empresa B'},
            {'from': 'Ancash', 'to': 'Empresa C'}
        ]
    }
    
    # Build the bipartite network
    output = build_bipartite_network(sample_data)
    
    # Assertions to check if the output matches expected structure
    assert len(output['nodes']) == len(expected_output['nodes'])
    assert len(output['edges']) == len(expected_output['edges'])
    
    for node in expected_output['nodes']:
        assert node in output['nodes']
    
    for edge in expected_output['edges']:
        assert edge in output['edges']