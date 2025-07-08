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
        for line in f:
            line = line.strip()
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


def topological_sort(graph, in_degree, all_pages):
    queue = deque()
    result = [] 

    for page in all_pages:
        if in_degree[page] == 0:
            queue.append(page)
    
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    '''if len(result) != len(all_pages):
        raise ValueError("Graph has cycles or is not connected")'''
    
    return result



def is_valid_order(pages, graph):
    """Check if a given order respects all rules"""
    #position = {page: i for i, page in enumerate(pages)} #Creates a dictionay that maps each page to its position in the sorted list.
    position = {}
    for i, page in enumerate(pages):
        position[page] = i
    
    for before in graph:
        for after in graph[before]:
            if before in position and after in position:
                if position[before] >= position[after]:
                    return False
    return True


data = creating_file()
updates = collect_updates()
graph, in_degree, all_pages = parse_rules()

sorted_pages = topological_sort(graph, in_degree, all_pages)
print(f"Sorted pages: {sorted_pages}")

sum_middle_page_number = 0
for update in updates:
    #valid_order = is_valid_order(update, graph)
    #print(f"Valid printing order: {valid_order}")   

    if is_valid_order(update, graph):
        middle_index = len(update) // 2
        middle_page = update[middle_index]
        sum_middle_page_number += middle_page
        

print (sum_middle_page_number)

