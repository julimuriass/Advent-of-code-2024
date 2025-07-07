FILE_NAME = "input.txt"

def creating_file ():
    with open(FILE_NAME, "r") as f :  
         data = f.read().replace('\n', '')

    return data



def restoring_file ():
     lines = []
     with open(FILE_NAME) as f:
         for line in f:
             lines.append(list(line)) # Creates a list of lists (the main list has as elements each line, and the elements are lists with each character).

     return lines


def find_horizontal (file):
     pattern1 = r"XMAS"
     pattern2 = r"SAMX"

     appearances = data.count(pattern1)
     appearances += data.count (pattern2)

     return appearances



def find_vertical(lines):
     appearances = 0

     # To find "X\nM\nA\nS". 

     for i in range(len(lines) - 3): # i: list.
          
          for n, elem in enumerate(lines[i]): # elem: char , lines[i]: list.
                
                if elem == "X" and lines[i+1][n] == "M" and lines[i+2][n] == "A" and lines[i+3][n] == "S":
                     appearances += 1

                # To find "S\nA\nM\nX". 
                elif elem == "S" and lines[i+1][n] == "A" and lines[i+2][n] == "M" and lines[i+3][n] == "X":
                    appearances += 1

     return appearances    


def find_diagonal (lines):
     appearances = 0

     rows, cols = len(lines), len(lines[0])

    # Diagonal down-right (↘) and up-left (↖)
     for i in range(rows - 3):  # Start positions for ↘
        for j in range(cols - 3):
            if (
                lines[i][j] == "X"
                and lines[i+1][j+1] == "M"
                and lines[i+2][j+2] == "A"
                and lines[i+3][j+3] == "S"
            ):
                appearances += 1
            elif (
                lines[i][j] == "S"
                and lines[i+1][j+1] == "A"
                and lines[i+2][j+2] == "M"
                and lines[i+3][j+3] == "X"
            ):
                appearances += 1

    # Diagonal down-left (↙) and up-right (↗)
     for i in range(rows - 3):  # Start positions for ↙
        for j in range(3, cols):
            if (
                lines[i][j] == "X"
                and lines[i+1][j-1] == "M"
                and lines[i+2][j-2] == "A"
                and lines[i+3][j-3] == "S"
            ):
                appearances += 1
            elif (
                lines[i][j] == "S"
                and lines[i+1][j-1] == "A"
                and lines[i+2][j-2] == "M"
                and lines[i+3][j-3] == "X"
            ):
                appearances += 1
    
     return appearances


data = creating_file() # Data's got my soup of letters.
file = restoring_file() # Contains a list of lists
total_appearances = 0
total_appearances = find_horizontal(data) + find_vertical(file) + find_diagonal(file)
print (total_appearances)



