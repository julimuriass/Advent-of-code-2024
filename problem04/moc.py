
MIN_DIF = 1
MAX_DIF = 3

def check_distances(line):

    distance_errors = 0
    for distance in line:
        if abs(distance) < MIN_DIF or abs(distance) > MAX_DIF:
            distance_errors += 1
    if distance_errors > 1:
        return False
    
    positives = [distance for distance in line if distance >= 0]
    negatives = [distance for distance in line if distance < 0]
    if len(positives) > 1:
        return len(negatives) <= 1
    if len(negatives) > 1:
        return len(positives) <= 1
    
    return True



print(check_distances([1,2,3])) # t
print(check_distances([1,3,9])) # f
print(check_distances([1,2,-1])) # t
print(check_distances([1,2,-1, -1])) # f

def list_with_ranges(list1 : list) -> list:
    new_list = []
    for i in range(len(list1)-1):
        value = list1[i+1] - list1[i]
        new_list.append(value)

    return new_list



def is_safe (list1 : list) -> bool:
    positives = 0
    negatives = 0
    not_in_range = 0
    aux = 0

    safe = False

    # I check all the conditions.
    for value in list1:
        if value > 0:
            positives =+ 1 
        elif value <= 0:
            negatives =+ 1
        if (value < 1) or (value > 3):
            not_in_range =+ 1
    
    
    # I check if it's safe.

    if positives > negatives: # If it's increasing.
        if (negatives == 0) or (negatives == 1):
            aux =+ 1
        if (not_in_range == 0) or (not_in_range == 1):
            aux =+ 1
        
        if aux == 1:
            safe = True
            return safe
        
    #if negatives > positives :  # If it's decreasing.
    
    elif negatives > positives: # If it's decreasing.
        if (positives == 0) or (positives == 1):
            aux =+ 1
        if (not_in_range == 0) or (not_in_range == 1):
            aux =+ 1
        
        if aux == 1:
            safe = True
            return safe
    
    return safe # If it's false.