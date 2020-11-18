# -*- coding: utf-8 -*-

#%% Homework

# 1. Create a graph in Python that represents a group of people andthe debts between them.

debt_graph = {
    "pepe": [{"destination":"dani", "debt": 5}],
    "dani": [{"destination":"juan", "debt": 6}],
    "juan": []
    }

print(debt_graph)

# 2. Create a graph in Python that represents a subway map.



# 3. Create a graph in Python that represents friendship in Facebook.
# 4. Think of a way of implementing them using either adjacency lists or adjacency matrices

graph_as_adj_matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
    ]


#%% breadth first search

graph = {
    1: [2,3,4],
    2: [5, 6],
    3: [],
    5: [],
    6: [],
    4: [7, 8],
    7: [],
    8: []
}

neighbors_for_1 = graph[1]
neighbors_for_8 = graph[8]
 
def bfs(graph, start):
    queue = [start]
    visited = []
    
    while queue != []:
        current = queue[0]
        queue.pop(0)
        
        neighbors = graph[current]
        
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
            
        visited.append(current)
        

    return visited

print(bfs(graph, 1))









#%% finding all paths from a given node

def find_paths(graph, start):
    queue = [start]
    paths = {start: [start]}
    
    while queue != []:
        current = queue[0]
        queue.pop(0)
        
        neighbors = graph[current]
        
        for neighbor in neighbors:
            if neighbor not in paths:
                queue.append(neighbor)
                paths[neighbor] = paths[current] + [neighbor]

    return paths

#print(find_paths(graph, 1))


def find_path(graph, start, finish):
    all_paths = find_paths(graph, start)
    
    return all_paths[finish]


print(find_path(graph, 1, 7))
    

#%% finding all paths from to a given node
