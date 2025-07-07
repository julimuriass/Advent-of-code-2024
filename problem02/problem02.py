FILE_NAME = "input.txt"

def resolve_problem ():
    # Open the file and build the right and left lists.
    left_ids = []
    right_ids = []
    with open(FILE_NAME) as f:
        for line in f:
            values = line.split()
            left_ids.append(int(values[0]))
            right_ids.append(int(values[1]))

     # Sort the 2 lists.
    left_ids.sort()
    right_ids.sort()

    # Now I have to count how many times each number from the left list appear on the right list.
    similarity_score = 0
    for value in left_ids:
        appearances = right_ids.count(value)
        multiplied_value = value * appearances
        similarity_score += multiplied_value
    
    print(similarity_score)

resolve_problem()
