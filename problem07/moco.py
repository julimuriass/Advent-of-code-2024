import re

FILE_NAME = "input.txt"

def creating_file():
    with open(FILE_NAME, "r") as f:
        data = f.read().replace('\n', '')
    return data

def restoring_file():
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            lines.append(list(line.strip()))  # Strip newline characters
    return lines

def find_horizontal(data):
    pattern1 = r"XMAS"
    pattern2 = r"SAMX"
    appearances = data.count(pattern1)
    appearances += data.count(pattern2)
    return appearances

def find_vertical(lines):
    appearances = 0
    for i in range(len(lines) - 3):
        for n, elem in enumerate(lines[i]):
            if elem == "X" and lines[i+1][n] == "M" and lines[i+2][n] == "A" and lines[i+3][n] == "S":
                appearances += 1
            elif elem == "S" and lines[i+1][n] == "A" and lines[i+2][n] == "M" and lines[i+3][n] == "X":
                appearances += 1
    return appearances

def find_diagonal(lines):
    appearances = 0

    # Diagonal down-right and up-left
    for i in range(len(lines) - 3):
        for n in range(len(lines[i]) - 3):
            if lines[i][n] == "X" and lines[i+1][n+1] == "M" and lines[i+2][n+2] == "A" and lines[i+3][n+3] == "S":
                appearances += 1
            elif lines[i][n] == "S" and lines[i+1][n+1] == "A" and lines[i+2][n+2] == "M" and lines[i+3][n+3] == "X":
                appearances += 1

    # Diagonal down-left and up-right
    for i in range(len(lines) - 3):
        for n in range(3, len(lines[i])):
            if lines[i][n] == "X" and lines[i+1][n-1] == "M" and lines[i+2][n-2] == "A" and lines[i+3][n-3] == "S":
                appearances += 1
            elif lines[i][n] == "S" and lines[i+1][n-1] == "A" and lines[i+2][n-2] == "M" and lines[i+3][n-3] == "X":
                appearances += 1

    return appearances

# Main logic
data = creating_file()  # Flat string for horizontal search
file = restoring_file()  # 2D list for vertical/diagonal searches
total_appearances = find_horizontal(data) + find_vertical(file) + find_diagonal(file)
print(total_appearances)