FILE_NAME = "input.txt"
MIN_DIF = 1
MAX_DIF = 3


def process_line(line):
    
    l = len(line)
    if l <= 1:
        return True, l
    
    dir = None
    for i in range(0, l-1):
        curr = line[i]
        next = line[i+1]
        if curr == next:
            return False, i
        dif = next - curr

        if dif == 0:
            return False, i
        if abs(dif) > MAX_DIF:
            return False, i
        
        if dir is None:
            dir = "asc" if next > curr else "dsc"
        else:
            next_dir = "asc" if next > curr else "dsc"
            if next_dir != dir:
                return False, i
    
    return True, l




def calculate_distances(line):
    l = len(line)
    assert l > 1
    distances = []
    for i in range(1, l):
        distance = line[i] - line[i-1]
        distances.append(distance)
    return distances


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



def list_with_distances(list1 : list) -> list:
    new_list = []
    for i in range(len(list1)-1):
        value = list1[i+1] - list1[i]
        new_list.append(value)

    return new_list

def is_safe (list1 : list) -> bool:
    positives = 0
    negatives = 0
    not_in_range = 0
    errors = 0
    safe = False

    # I check all the conditions.

    positives = sum(1 for value in list1 if value > 0)
    negatives = sum(1 for value in list1 if value <= 0)
    not_in_range = sum(1 for value in list1 if abs(value) < 1 or abs(value) > 3)

    # I check if it's safe.


    # If it's increasing.
    if positives > negatives: 
        print ("increasing")
        if negatives == 1:
            errors += 1
        if not_in_range == 1:
            errors += 1
        print (errors)
        if (errors == 1) or (errors == 0): # It bears only one condition.
            safe = True
            
            return safe
        
    # If it's decreasing.
    elif negatives > positives: 
        print ("decreasing")
        if positives == 1:
            errors += 1
        if  not_in_range == 1:
            errors += 1

        print (errors)
        if (errors == 1) or (errors == 0):           
            safe = True          
            return safe
    
    return safe # If it's false.


def resolve_problem ():
    # Open the file and create a list for the line I'm working with.
    safe_reports = 0

    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            line = [int(s) for s in line.split()] # List with the int values of each line.
            lines.append(line) # List of the lists with the int values of all the lines now.
        
    # I work with each line (with each list (values) on the list lines).
   # lines = [[7 ,6 ,4 ,2 ,1] , [1 ,2 ,7 ,8 ,9], [9, 7, 6, 2, 1], [1 ,3 ,2 ,4 ,5], [8 ,6 ,4, 4, 1], [1 ,3 ,6 ,7 ,9]]
    for line in lines:
        ok, i = process_line(line)
        if not ok:
            del line[i]
            ok, i = process_line(line)
        if ok:
            safe_reports += 1

   #     this_line = []
    ##       print (this_line)
      #      safe = is_safe (this_line)
       #     if safe:
        #        safe_reports += 1
            
         #   this_line.clear()
      
        
    print(safe_reports)

            
resolve_problem()

                
                

