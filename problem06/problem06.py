import re

FILE_NAME = "input.txt"

def sum_valid_mul_instructions (file):
    pattern_mul = r"mul\((\d+),(\d+)\)"
    pattern_do = r"do\(\)"
    pattern_dont = r"don't\(\)"

    tokens = re.split(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))" , file) # It splits the file into tokens (a meaningful unit of text) (some with mul(x,y) , do(), don't(), and junk).


    mul_enabled = True 
    result = 0

    for token in tokens:
        token = token.strip()

        if re.match(pattern_mul, token): 
            # If mul is enabled, process the instruction
            if mul_enabled:
                x, y = map(int, re.findall(r"\d+", token))
                result += x * y

        elif re.match(pattern_do, token):
            # Enable mul instructions
            mul_enabled = True
        elif re.match(pattern_dont, token):
            # Disable mul instructions
            mul_enabled = False
    
    return result


def creating_file ():
    with open(FILE_NAME, "r") as f :  
         data = f.read().replace('\n', '')
    return data

file = creating_file()
total = sum_valid_mul_instructions(file)
print("Sum of valid mul results:", total)