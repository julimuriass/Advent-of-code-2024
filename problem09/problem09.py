import os
FILE_NAME = os.path.join(os.path.dirname(__file__), "input.txt")

from collections import defaultdict, deque #For the directed graph and queue.

def creating_file ():
    with open(FILE_NAME, "r") as f :  
         data = f.read().replace('\n', '')

    return data

def parse_rules():
    """Parse rules from text format like 'X|Y' into a graph"""
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_pages = set() 
    
    with open(FILE_NAME) as f : 
        for line in f.strip().split('\n'):
            if '|' in line: # Check if the line contains a dependency
                before, after = map(int, line.split('|'))
                graph[before].append(after) # Create a directed edge from before to after
                in_degree[after] += 1  # Increment in-degree for the 'after' page
                all_pages.add(before)
                all_pages.add(after)
            
                # Initialize in_degree for pages with no dependencies
                if before not in in_degree:
                    in_degree[before] = 0
    
    
    return graph, in_degree, all_pages

def collect_updates():
    updates = []

    with open(FILE_NAME) as f : 
        for line in f:
            line = line.strip()
            if '|' not in line and line:
                try:
                    numbers = [int(x) for x in line.split(',')]
                    updates.append(numbers)
                except ValueError:
                    continue  # Si algún valor no es entero, lo ignora
    
    return updates

data = creating_file()
updates = collect_updates()
print(updates)