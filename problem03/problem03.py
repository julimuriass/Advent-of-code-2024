FILE_NAME = "input.txt"

def is_ordered_increasingly (list1 : list) -> bool:
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]: # If my current value is bigger than the next value then it's not ordered increasingly.
            return False
    return True
        
def is_ordered_decreasingly (list1 : list) -> bool:
    for i in range(len(list1)-1):
        if list1[i] < list1[i+1]: # If my current value is smaller than the next value then it's not ordered decreasingly.
            return False
    return True

def is_safe (list1 : list) -> bool:
    for i in range(len(list1)-1):
        if (1 > (abs(list1[i] - list1[i+1]))) or ((abs(list1[i] - list1[i+1])) > 3) : # If the distance between the numbers is in the range (1<= distance <= 3).
            return False
    return True


def resolve_problem ():
    # Open the file and create a list for the line I'm working with.
    safe_reports = 0

    with open(FILE_NAME) as f: 
        this_line = []

        for line in f:
            this_line = line.split() #this_line is a list with the series of numbers of the line corresponding.
            aux_list = []

            for i in this_line:
                aux_list.append(int(i))
            this_line = aux_list

            # I check if the values are all increasing.
            ordered = is_ordered_increasingly(this_line)
            if ordered :
                # if it's ordered I have to see if it's safe.
                safe = is_safe(this_line)
                if safe:
                    safe_reports += 1
            
            # I check if the values are all increasing.
            else: 
                ordered = is_ordered_decreasingly(this_line)
                if (ordered):
                    safe = is_safe(this_line)
                    if safe:
                        safe_reports += 1
            
            this_line.clear()
        
    print (safe_reports)

            
resolve_problem()

                
                

