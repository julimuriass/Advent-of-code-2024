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

    # Calculate the total distance
    assert len(left_ids) == len(right_ids)

    zipped = zip(left_ids, right_ids) # I create my objetito.
    distances = [abs(left_ids - right_ids) for left_ids, right_ids in zipped] # I create a list  with the distances from the tuples of the zip.
    total_distance = sum(distances)

    print(total_distance)

resolve_problem()
     

