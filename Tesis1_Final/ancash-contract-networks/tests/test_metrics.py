import pytest
from src.networks.metrics import calculate_degree, calculate_betweenness, calculate_closeness, calculate_density

def test_calculate_degree():
    # Sample input for testing
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['C']
    }
    expected_degrees = {'A': 2, 'B': 2, 'C': 3, 'D': 1}
    degrees = calculate_degree(graph)
    assert degrees == expected_degrees

def test_calculate_betweenness():
    # Sample input for testing
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    expected_betweenness = {'A': 0, 'B': 1, 'C': 1, 'D': 0}
    betweenness = calculate_betweenness(graph)
    assert betweenness == expected_betweenness

def test_calculate_closeness():
    # Sample input for testing
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    expected_closeness = {'A': 1.0, 'B': 1.0, 'C': 1.0, 'D': 1.0}
    closeness = calculate_closeness(graph)
    assert closeness == expected_closeness

def test_calculate_density():
    # Sample input for testing
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['C']
    }
    expected_density = 0.5
    density = calculate_density(graph)
    assert density == expected_density