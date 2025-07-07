import re

FILE_NAME = "input.txt"

def sum_valid_mul_instructions (file):
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, file)

    result = sum(int(x) * int(y) for x, y in matches)
    
    return result

def creating_file ():
    with open(FILE_NAME, "r") as f :  
         data = f.read().replace('\n', '')
    return data

file = creating_file()
total = sum_valid_mul_instructions(file)
print("Sum of valid mul results:", total)