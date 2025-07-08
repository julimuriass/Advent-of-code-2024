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


def topological_sort(graph, in_degree, update):
    # Only consider pages that are in this update
    update_set = set(update)
    
    # Calculate in_degree only for pages in this update
    local_in_degree = {}
    for page in update: # For each element in the update.
        local_in_degree[page] = 0 #Starts with 0 in-degree for each page in the update.
        for other_page in update: 
            if other_page in graph and page in graph[other_page]:
                local_in_degree[page] += 1
    
    queue = deque()
    result = []
    
    # Start with pages that have no dependencies within this update
    for page in update:
        if local_in_degree[page] == 0:
            queue.append(page)
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        # Only consider neighbors that are in this update
        for neighbor in graph[current]:
            if neighbor in update_set:
                local_in_degree[neighbor] -= 1
                if local_in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    return result


data = creating_file()
updates = collect_updates()
graph, in_degree, all_pages = parse_rules()

incorrect_updates = [update for update in updates if not is_valid_order(update, graph)]
sum_middle_page_number = 0
for update in incorrect_updates:
    fixed_update = topological_sort(graph, in_degree, update)
    print(f"Update: {update}")
    print(f"Fixed update: {fixed_update}")

    middle_page = fixed_update[len(update) // 2]
    sum_middle_page_number += middle_page

print (sum_middle_page_number)



